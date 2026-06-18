from __future__ import annotations

import streamlit as st


st.set_page_config(
    page_title="Coach Knux",
    page_icon="🥊",
    layout="wide",
)

st.title("🥊 Coach Knux")
st.subheader("Your AI striking coach.")

st.write(
    """
    Coach Knux will analyze Muay Thai training videos and help detect:

    - Guard drops
    - Chin exposure
    - Slow hand return
    - Weak hip rotation

    Today, this is the ugly v0.
    Next, we will connect video upload and pose landmark extraction.
    """
)

st.success("Coach Knux v0 is running.")