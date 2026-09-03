"""Estilos globales del prototipo."""
import streamlit as st

CSS = """
<style>
[data-testid="stAppViewContainer"]{background:#F5F7FA}.block-container{padding-top:1.2rem;max-width:1400px}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#163A5F,#102C49)}[data-testid="stSidebar"] *{color:#fff}
.hero{background:linear-gradient(120deg,#163A5F,#2471A3);color:white;padding:24px 30px;border-radius:14px;box-shadow:0 8px 24px #163a5f30;margin-bottom:12px}
.hero h1{margin:0;font-size:2.1rem}.hero p{margin:5px 0}.badge{display:inline-block;background:#F4B942;color:#263238;font-weight:800;padding:5px 11px;border-radius:99px;font-size:.75rem}
.academic-label{display:inline-block;background:#e8f6f3;color:#117864;border:1px solid #16A085;padding:4px 10px;border-radius:99px;font-size:.75rem;font-weight:800;margin-bottom:10px}
.safety{background:#fff3f1;border:1px solid #C0392B;color:#8e2a20;padding:9px 14px;border-radius:10px;font-weight:700;margin:10px 0 20px}
.card{background:#fff;border-radius:14px;padding:18px;box-shadow:0 3px 14px #163a5f14;height:100%;border:1px solid #e9eef3}.kpi{font-size:2rem;font-weight:800;color:#163A5F}.label{color:#60717c;font-size:.88rem}.priority{color:#C0392B;font-weight:800;font-size:.75rem}
.info{background:#eaf5f8;border-left:5px solid #16A085;padding:16px;border-radius:10px}.formula{font-size:1.8rem;text-align:center;font-weight:800;color:#163A5F;background:white;padding:22px;border-radius:14px}
.footer{text-align:center;color:#60717c;border-top:1px solid #dce4ea;margin-top:35px;padding:22px;font-size:.85rem}
div[data-testid="stForm"]{background:#fff;padding:20px;border-radius:14px;border:1px solid #e2e9ee}
@media(max-width:700px){.hero h1{font-size:1.6rem}.block-container{padding:1rem}.kpi{font-size:1.55rem}}
</style>"""

def aplicar_estilos() -> None:
    """Inyecta estilos CSS globales."""
    st.markdown(CSS, unsafe_allow_html=True)

def encabezado() -> None:
    """Renderiza cabecera y advertencia ética permanentes."""
    st.markdown('<div class="hero"><span class="badge">DEMO / INVESTIGACIÓN</span><h1>🏥 HCC-PI Monitor</h1><p>Sistema de monitoreo de adherencia institucional a prácticas de parto humanizado</p><small>Prototipo académico para vigilancia de procesos documentados</small></div><div class="safety">DEMO DE INVESTIGACIÓN — No utilizar para decisiones clínicas.</div><span class="academic-label">DEMO ACADÉMICA — Datos demostrativos</span>', unsafe_allow_html=True)

def pie() -> None:
    """Renderiza el pie institucional."""
    st.markdown('<div class="footer"><b>HCC-PI Monitor</b> · Prototipo académico de investigación · Versión Congreso 1.0<br>Los resultados presentados ilustran un sistema potencial de vigilancia institucional y no constituyen recomendaciones clínicas.</div>', unsafe_allow_html=True)
