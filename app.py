import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TV En Vivo P2P", layout="wide")

st.title("📡 CANAL 8 TV ONLINE")

# --- CONFIGURACIÓN ---
# Pega aquí el enlace que copiaste de VDO.Ninja (Viewer Link)
# Debería verse algo como: https://vdo.ninja/?view=xxxxxx
VDO_NINJA_LINK = st.secrets["VDO_NINJA_LINK"]
# --- VISUALIZACIÓN ---
# Usamos un iframe para mostrar el video. 
# height=500 es la altura en pixeles.
components.iframe(VDO_NINJA_LINK, height=500, scrolling=False)
