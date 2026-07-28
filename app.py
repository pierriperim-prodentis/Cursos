import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Dashboard Cursos - Pródentis",
    page_icon="📊",
    layout="wide"
)

# Proteção por chave na URL
chave = st.query_params.get("chave", "")

if chave != "prodentis2026":
    st.error("🔒 Acesso restrito. URL inválida.")
    st.stop()

# Carregar o HTML do dashboard
html_content = Path("dashboard.html").read_text(encoding="utf-8")

# Renderizar o dashboard completo
st.components.v1.html(html_content, height=3200, scrolling=True)
