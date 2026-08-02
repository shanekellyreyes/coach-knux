import tempfile
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Knux",
    page_icon="🥊",
    layout="wide",
)

st.title("Knux")
st.subheader("AI Muay Thai striking coach")

uploaded_file = st.file_uploader(
    "Upload a Muay Thai training video",
    type=["mp4", "mov", "avi"],
)

if uploaded_file is None:
    st.info("Upload a short training clip to start analysis.")
else:
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as temp_file:
        temp_file.write(uploaded_file.read())
        video_path = temp_file.name

    st.video(video_path)

    st.success("Video uploaded successfully.")

    st.write("Next milestone: extract pose landmarks and generate a coaching report.")