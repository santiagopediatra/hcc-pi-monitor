"""Tarjetas HTML del dashboard."""
import html
import streamlit as st

def tarjeta_kpi(titulo: str, valor: str, nota: str = "", prioritaria: bool = False) -> None:
    """Muestra una tarjeta KPI escapando texto dinámico."""
    clase = "priority" if prioritaria else "label"
    st.markdown(f'<div class="card"><div class="label">{html.escape(titulo)}</div><div class="kpi">{html.escape(valor)}</div><div class="{clase}">{html.escape(nota)}</div></div>', unsafe_allow_html=True)

