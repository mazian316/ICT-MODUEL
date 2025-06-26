import streamlit as st
from utils.prop_logic import get_prop_picks
from PIL import Image

st.set_page_config(page_title="ICT MODULE")

top_5 = get_prop_picks()[:5]
props = get_prop_picks()

# Top 5 Picks
for prop in top_5:
    st.markdown(
        f"**{prop['player']}** — _{prop['prop_type']}_  \n"
        f"🎯 Confidence: **{prop['confidence']}%** \n"
        f"_Reason: {prop['reason']}_"
    )
    st.markdown("———")

# All Props Table
st.markdown("## 📊 All Prop Picks")
for prop in props:
    st.markdown(f"**{prop['player']}** — _{prop['prop_type']}_")
    st.markdown(f"🧠 Confidence: {prop['confidence']}%")
    st.markdown(f"📌 {prop['reason']}")
    st.markdown("———")


