import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Dashboard Cursos - Pródentis",
    page_icon="📊",
    layout="wide"
)

# Remover padding, margens e fundo preto do Streamlit
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background-color: #f8f4fc !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        [data-testid="stHeader"] { display: none !important; }
        [data-testid="stToolbar"] { display: none !important; }
        [data-testid="stDecoration"] { display: none !important; }
        [data-testid="stStatusWidget"] { display: none !important; }
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Proteção por chave na URL
chave = st.query_params.get("chave", "")

if chave != "prodentis2026":
    st.error("🔒 Acesso restrito. URL inválida.")
    st.stop()

# Carregar o HTML do dashboard
html_content = Path("Dashboard_Cursos_2026.html").read_text(encoding="utf-8")

# Injetar script de auto-resize antes do </body>
auto_resize = """
<script>
(function() {
    function sendHeight() {
        var h = document.body.scrollHeight || document.documentElement.scrollHeight;
        window.parent.postMessage({type: 'streamlit:setFrameHeight', height: h}, '*');
    }
    window.addEventListener('load', function() {
        sendHeight();
        setTimeout(sendHeight, 500);
        setTimeout(sendHeight, 1500);
    });
    window.addEventListener('resize', sendHeight);
    var obs = new MutationObserver(sendHeight);
    obs.observe(document.body, {childList: true, subtree: true, attributes: true});
})();
</script>
"""
html_content = html_content.replace('</body>', auto_resize + '</body>')

# Renderizar o dashboard completo
st.components.v1.html(html_content, height=3800, scrolling=False)

