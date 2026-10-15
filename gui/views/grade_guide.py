import streamlit as st

from gui.components import show_html
from gui.theme import GRADE_RULES
from models.student import PASS_MARK


def show_grade_guide(student):
    with st.container(key="glass_guide"):
        st.markdown("#### How your grade is worked out")
        for grade, rule in GRADE_RULES:
            show_html(f'<div class="detail-row g-{grade}"><span>{rule}</span><span class="badge">{grade}</span></div>')
        st.caption(f"A student passes when the average mark of all subjects is {PASS_MARK} or more.")
