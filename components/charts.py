"""Constructores centralizados de figuras Plotly."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

COLORES = ["#2471A3", "#16A085", "#27AE60", "#F4B942", "#C0392B"]

def donut(valor: float) -> go.Figure:
    fig = go.Figure(go.Pie(values=[valor, 100-valor], hole=.72, marker_colors=["#16A085", "#e7edf2"], textinfo="none"))
    fig.add_annotation(text=f"<b>{valor:.1f}%</b>", showarrow=False, font_size=28, font_color="#163A5F")
    fig.update_layout(height=300, margin=dict(l=10,r=10,t=20,b=10), showlegend=False)
    return fig

def tendencia(datos: dict[str, list], metrica: str, tipo: str) -> go.Figure:
    df = pd.DataFrame(datos)
    fig = px.line(df, x="Año", y=metrica, markers=True, color_discrete_sequence=["#2471A3"]) if tipo == "Línea" else px.bar(df, x="Año", y=metrica, color_discrete_sequence=["#2471A3"])
    fig.add_vrect(x0=2019.5, x1=2021.5, fillcolor="#C0392B", opacity=.10, line_width=0, annotation_text="Periodo COVID-19")
    fig.update_layout(template="plotly_white", height=430, yaxis_title="Porcentaje (%)", hovermode="x unified")
    return fig

def forest(filas: list[tuple], log: bool) -> go.Figure:
    nombres, valores, bajos, altos, ps = zip(*filas)
    fig = go.Figure(go.Scatter(x=valores, y=nombres, mode="markers", marker=dict(size=11,color="#2471A3"),
        error_x=dict(type="data", symmetric=False, array=[a-v for a,v in zip(altos,valores)], arrayminus=[v-b for v,b in zip(valores,bajos)]),
        text=[f"aOR {v:.2f} · IC95% {b:.2f}–{a:.2f} · p {p}" for v,b,a,p in zip(valores,bajos,altos,ps)], hovertemplate="%{y}<br>%{text}<extra></extra>"))
    fig.add_vline(x=1, line_dash="dash", line_color="#C0392B")
    fig.update_layout(template="plotly_white", height=max(330, 55*len(filas)), xaxis_type="log" if log else "linear", xaxis_title="Razón de odds ajustada (aOR)", margin=dict(l=20))
    return fig

def radar_hospital(datos: dict[str, dict[str,float]]) -> go.Figure:
    categorias = [c for c in next(iter(datos.values())) if c != "Adherencia institucional"]
    fig = go.Figure()
    for i,(hospital,valores) in enumerate(datos.items()):
        fig.add_trace(go.Scatterpolar(r=[valores[c] for c in categorias]+[valores[categorias[0]]], theta=categorias+[categorias[0]], fill="toself", name=hospital, line_color=COLORES[i]))
    fig.update_layout(polar=dict(radialaxis=dict(range=[0,100],visible=True)), height=470, margin=dict(t=35,b=25))
    return fig
