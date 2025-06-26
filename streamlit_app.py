import streamlit as st
from utils.prop_logic import get_prop_picks
from PIL import Image

st.set_page_config(page_title="ICT MODULE")
filter_option = st.selectbox("📊 Filter by Prop Type", ["All", "HR", "Ks", "Hits", "TB"])

# Apply filter using the argument your function expects
if filter_option == "All":
    filtered_props = get_prop_picks()
else:
    filtered_props = get_prop_picks(filter_option)

# Then use filtered_props instead of get_prop_picks()
top_5 = filtered_props[:5]
props = filtered_props

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


