from pathlib import Path

import streamlit as st

CSS_FOLDER = Path(__file__).parent / "css"
CSS_FILES = ["base.css", "cards.css", "menu.css"]


def load_styles():
    css = "".join((CSS_FOLDER / name).read_text(encoding="utf-8") for name in CSS_FILES)
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
