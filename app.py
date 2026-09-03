"""Aplicación Streamlit HCC-PI Monitor — prototipo académico."""
from typing import Any

import pandas as pd
import plotly.express as px
import streamlit as st

from components.cards import tarjeta_kpi
from components.charts import donut, forest, radar_hospital, tendencia
from components.styles import aplicar_estilos, encabezado, pie
from data.sample_data import (BASELINE_INSTITUCIONAL, CALIDAD_DATOS, ETIQUETA_DATOS_DEMO, FACTORES_ASOCIADOS,
    HISTORICO, HOSPITALES_SIMULADOS, NOTA_BASELINE, PRACTICAS, RAZONES_SIN_ACOMPANANTE)
from utils.hccpi import calcular_hccpi, clasificar_hccpi, evaluar_alertas
from utils.simulations import siguiente_id

st.set_page_config(page_title="HCC-PI Monitor", page_icon="🏥", layout="wide", initial_sidebar_state="expanded")
aplicar_estilos()
encabezado()

PAGINAS = ["🏠 Resumen ejecutivo", "📈 Tendencias", "🩺 Registrar parto", "🔎 Factores asociados",
           "🏥 Comparación hospitalaria", "📋 Calidad de datos", "ℹ️ Metodología"]
st.sidebar.markdown("## HCC-PI Monitor")
pagina = st.sidebar.radio("Navegación", PAGINAS, label_visibility="collapsed")
st.sidebar.caption("Solo datos ficticios o demostrativos. Sin identificadores personales.")
st.sidebar.markdown("[Proyecto open source](https://github.com/santiagopediatra/hcc-pi-monitor)")

def etiqueta_dashboard() -> None:
    """Identifica los paneles que presentan información demostrativa."""
    st.caption(f"🧪 {ETIQUETA_DATOS_DEMO}")

def resumen() -> None:
    """Página de indicadores ejecutivos."""
    st.title("Resumen ejecutivo")
    etiqueta_dashboard()
    cols = st.columns(3)
    with cols[0]: tarjeta_kpi("Adherencia institucional de referencia", f"{BASELINE_INSTITUCIONAL:.1f}%", "Partos con HCC-PI ≥ 0.80")
    for i, practica in enumerate(PRACTICAS.values(), start=1):
        with cols[i % 3]:
            prioridad = practica["corto"] == "Acompañamiento"
            tarjeta_kpi(practica["nombre"], f'{practica["valor"]:.1f}%', "BRECHA PRIORITARIA" if prioridad else "Práctica documentada", prioridad)
    izquierda, derecha = st.columns([1, 1.5])
    with izquierda:
        st.plotly_chart(donut(BASELINE_INSTITUCIONAL), width="stretch", key="donut_resumen")
        st.caption(NOTA_BASELINE)
    with derecha:
        df = pd.DataFrame([{"Práctica": p["corto"], "Porcentaje": p["valor"]} for p in PRACTICAS.values()]).sort_values("Porcentaje")
        fig = px.bar(df, x="Porcentaje", y="Práctica", orientation="h", text_auto=".1f", color="Porcentaje", color_continuous_scale=["#F4B942", "#16A085"])
        fig.update_layout(template="plotly_white", height=330, coloraxis_showscale=False, xaxis_range=[0,100])
        st.plotly_chart(fig, width="stretch", key="barras_practicas")
    alertas = evaluar_alertas(BASELINE_INSTITUCIONAL, acompanamiento=PRACTICAS["LAB_COMP"]["valor"])
    if alertas: st.error(" ".join(alertas) + " Revisión por el equipo institucional de Calidad.")
    st.markdown('<div class="info"><b>¿Qué aporta HCC-PI?</b><br>Convierte cinco procesos clínicos documentados en una señal institucional simple para vigilancia, comparación temporal e identificación de brechas.</div>', unsafe_allow_html=True)

def tendencias() -> None:
    """Página temporal interactiva."""
    st.title("Tendencias 2018–2023")
    etiqueta_dashboard()
    c1,c2 = st.columns(2)
    metrica = c1.selectbox("Indicador", [c for c in HISTORICO if c != "Año"])
    tipo = c2.radio("Visualización", ["Línea", "Barras"], horizontal=True)
    st.plotly_chart(tendencia(HISTORICO, metrica, tipo), width="stretch", key="tendencia")
    valores = HISTORICO[metrica]
    menor = min((p for p in PRACTICAS.values()), key=lambda p: p["valor"])["corto"]
    cambio = valores[-1] - valores[0]
    direccion = "aumentó" if cambio > 0 else "disminuyó" if cambio < 0 else "se mantuvo"
    st.info(f"Interpretación descriptiva: {metrica} {direccion} {abs(cambio):.1f} puntos porcentuales entre 2018 y 2023. {menor} muestra la mayor brecha relativa entre las prácticas monitorizadas. No se infiere causalidad.")

def registrar() -> None:
    """Formulario local y cálculo individual."""
    st.title("Registrar parto demostrativo")
    registros: list[dict[str, Any]] = st.session_state.setdefault("registros_demo", [])
    identificador = siguiente_id(registros)
    st.info(f"ID automático: **{identificador}** · No ingrese datos personales.")
    with st.form("form_parto"):
        a,b,c = st.columns(3)
        clinicos = {
            "edad_materna": a.selectbox("Edad materna", ["<20", "20–34", ">=35"]),
            "educacion": b.selectbox("Educación", ["Primaria o menos", "Secundaria o superior"]),
            "prenatales": c.selectbox("Visitas prenatales", ["0", "1–4", ">=5"]),
            "gestacional": a.selectbox("Edad gestacional", ["<37", "37–41", ">=42"]),
            "peso": b.selectbox("Peso neonatal", ["<2500 g", "2500–3999 g", ">=4000 g"]),
            "apgar": c.selectbox("Apgar minuto 1", ["<7", ">=7"]),
            "hpp": a.selectbox("HPP", ["No", "Sí"]),
        }
        st.markdown("#### Prácticas documentadas")
        practicas = {codigo: st.checkbox(datos["nombre"], key=f"registro_{codigo}") for codigo,datos in PRACTICAS.items()}
        calcular = st.form_submit_button("CALCULAR HCC-PI", width="stretch")
    if calcular:
        try:
            indice, score = calcular_hccpi(practicas)
            st.session_state["ultimo_calculo"] = {"id": identificador, **clinicos, **practicas, "indice": indice, "score": score}
        except ValueError as error: st.error(str(error))
    resultado = st.session_state.get("ultimo_calculo")
    if resultado:
        clasificacion = clasificar_hccpi(resultado["indice"])
        st.success(f'HCC-PI = **{resultado["indice"]:.2f}** · **{clasificacion}** · {resultado["score"]}/5 prácticas cumplidas')
        for codigo, datos in PRACTICAS.items(): st.write(("✅" if resultado[codigo] else "❌") + " " + datos["nombre"])
        if st.button("Guardar registro de demostración", type="primary", key="guardar_demo"):
            if any(r["id"] == resultado["id"] for r in registros): st.warning("Este registro ya fue guardado en la sesión.")
            else:
                registros.append(resultado.copy()); st.success("Registro ficticio guardado únicamente en esta sesión.")
    st.caption("Este registro es ficticio/demostrativo y se elimina al cerrar la sesión.")

def factores() -> None:
    """Forest plot de asociaciones de referencia."""
    st.title("Factores asociados")
    etiqueta_dashboard()
    c1,c2 = st.columns([2,1])
    categoria = c1.selectbox("Práctica", list(FACTORES_ASOCIADOS))
    log = c2.toggle("Eje logarítmico", value=True)
    st.plotly_chart(forest(FACTORES_ASOCIADOS[categoria], log), width="stretch", key="forest")
    st.warning("Las asociaciones estadísticas no implican causalidad.")
    st.caption("Los valores presentados corresponden al conjunto de referencia utilizado para esta demostración y deberán verificarse contra la publicación científica antes de difusión formal.")

def hospitales() -> None:
    """Comparación explícitamente simulada."""
    st.title("Comparación hospitalaria")
    etiqueta_dashboard()
    st.warning("Hospital A, Hospital B y Hospital C: DATOS SIMULADOS para fines académicos. No representan instituciones reales ni evidencia institucional.")
    ranking = pd.DataFrame([{"Hospital": h, **v} for h,v in HOSPITALES_SIMULADOS.items()]).sort_values("Adherencia institucional", ascending=False)
    st.dataframe(ranking[["Hospital","Adherencia institucional"]], hide_index=True, width="stretch")
    st.plotly_chart(radar_hospital(HOSPITALES_SIMULADOS), width="stretch", key="radar")
    hospital = st.selectbox("Destacar hospital", list(HOSPITALES_SIMULADOS))
    largo = ranking.melt(id_vars="Hospital", value_vars=[c for c in ranking if c not in ("Hospital","Adherencia institucional")], var_name="Práctica", value_name="Porcentaje")
    fig = px.bar(largo, x="Práctica", y="Porcentaje", color="Hospital", barmode="group", opacity=.95)
    fig.for_each_trace(lambda t: t.update(opacity=1 if t.name == hospital else .35))
    fig.update_layout(template="plotly_white", yaxis_range=[0,100], height=420)
    st.plotly_chart(fig, width="stretch", key="hospital_barras")

def calidad() -> None:
    """Dashboard ficticio de calidad de datos."""
    st.title("Calidad de datos")
    etiqueta_dashboard()
    cols = st.columns(4)
    for col,(nombre,valor) in zip(cols,CALIDAD_DATOS.items()):
        with col: tarjeta_kpi(nombre, f"{valor:.1f}%", "● " + ("Verde" if (nombre=="Completitud registros" and valor>=95) or (nombre!="Completitud registros" and valor<=5) else "Amarillo"))
    df = pd.DataFrame({"Indicador": CALIDAD_DATOS.keys(), "Porcentaje": CALIDAD_DATOS.values()})
    st.plotly_chart(px.bar(df, x="Indicador", y="Porcentaje", color="Porcentaje", color_continuous_scale=["#C0392B","#F4B942","#27AE60"], text_auto=".1f"), width="stretch", key="calidad_barras")
    st.subheader("Posibles razones de ausencia de acompañante")
    razones = pd.DataFrame({"Razón": RAZONES_SIN_ACOMPANANTE.keys(), "Porcentaje": RAZONES_SIN_ACOMPANANTE.values()})
    st.plotly_chart(px.bar(razones, x="Porcentaje", y="Razón", orientation="h", color_discrete_sequence=["#2471A3"]), width="stretch", key="razones")
    st.warning("La ausencia de registro no debe interpretarse automáticamente como ausencia de la práctica.")

def metodologia() -> None:
    """Definiciones, fórmula y limitaciones."""
    st.title("Metodología")
    st.markdown('<div class="formula">HCC-PI = prácticas cumplidas / 5</div>', unsafe_allow_html=True)
    for codigo,p in PRACTICAS.items(): st.markdown(f'**{codigo} · {p["nombre"]}**  \n{p["definicion"]}')
    st.markdown("#### Clasificación\n- **0.80–1.00:** ALTA\n- **0.60–0.79:** MEDIA\n- **0.00–0.59:** BAJA")
    st.info("Adherencia institucional = partos con HCC-PI >=0.80 / total de partos elegibles ×100. Es distinta del índice individual de un parto.")
    st.markdown("#### Limitaciones")
    for texto in ["No mide consentimiento informado real", "No mide dignidad percibida", "No mide privacidad percibida", "No mide comunicación clínica", "No mide satisfacción materna", "No sustituye evaluación clínica", "No sustituye auditoría", "No sustituye encuesta postparto"]: st.write("❌ " + texto)
    st.markdown("#### Complementos propuestos")
    st.write("Encuesta postparto · Auditoría cualitativa · Grupos focales · Auditoría de historias · Registro de barreras")
    st.caption(NOTA_BASELINE)

RUTAS = {PAGINAS[0]: resumen, PAGINAS[1]: tendencias, PAGINAS[2]: registrar, PAGINAS[3]: factores,
         PAGINAS[4]: hospitales, PAGINAS[5]: calidad, PAGINAS[6]: metodologia}
try:
    RUTAS[pagina]()
except Exception as error:
    st.error(f"No fue posible renderizar la página: {error}")
pie()
