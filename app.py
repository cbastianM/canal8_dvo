import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TV En Vivo P2P", layout="wide")

st.title("📡 Transmisión Directa (WebRTC)")
st.caption("Señal directa desde OBS Studio con latencia sub-segundo")

# --- CONFIGURACIÓN ---
# Pega aquí el enlace que copiaste de VDO.Ninja (Viewer Link)
# Debería verse algo como: https://vdo.ninja/?view=xxxxxx

# --- VISUALIZACIÓN ---
# Usamos un iframe para mostrar el video. 
# height=500 es la altura en pixeles.
components.iframe(VDO_NINJA_LINK, height=500, scrolling=False)
