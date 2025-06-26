import streamlit as st
from utils.prop_logic import get_prop_picks

st.set_page_config(page_title="ICT MODULE", layout="wide", page_icon="⚾")

st.markdown("""# 🧢 ICT MODULE: MLB Prop Bet Picks\n\nGet today's top picks based on total bases, hits, home runs, and strikeouts.\n""")

game = st.selectbox("Filter by Game Matchup:", ["All Games", "Yankees vs Red Sox", "Dodgers vs Giants", "Cubs vs Cardinals"])

props = get_prop_picks(game)

for prop in props:
    st.markdown(f"### {prop['player']} — {prop['prop_type']}")
    st.markdown(f"**Confidence:** {prop['confidence']}%")
    st.markdown(f"📝 _{prop['reason']}_")
    st.markdown("---")
