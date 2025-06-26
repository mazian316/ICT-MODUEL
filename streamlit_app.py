import streamlit as st
from utils.prop_logic import get_prop_picks
from PIL import Image

st.set_page_config(page_title="ICT MODULE", layout="wide", page_icon="⚾")

# Load logo
logo = Image.open("static/logo.png")
st.image(logo, width=200)
st.markdown("### _MLB Prop Betting Picks - Powered by ICT MODULE_")

# Top 5 Picks
for prop in top_5:
    st.markdown(
        f"**{prop['player']}** — _{prop['prop_type']}_  \n"
        f"🎯 Confidence: **{prop['confidence']}%**  \n"
        f"_Reason: {prop['reason']}_"
    )
    st.markdown("———")

for prop in top_5:
    st.markdown(f"**{prop['player']}** — _{prop['prop_type']}_  
🎯 Confidence: **{prop['confidence']}%**  
_Reason: {prop['reason']}_")
    st.markdown("---")

# All Props Table
st.markdown("## 📊 All Prop Picks")
for prop in props:
    st.markdown(f"**{prop['player']}** — _{prop['prop_type']}_")
    st.markdown(f"🧠 Confidence: {prop['confidence']}%")
    st.markdown(f"📌 {prop['reason']}")
    st.markdown("---")
