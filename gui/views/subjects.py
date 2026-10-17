import streamlit as st

from gui.actions import enrol_click
from gui.cards import show_subject_cards
from gui.components import section_title
from models.student import MAX_SUBJECTS


def show_subjects(student):
    title_column, button_column = st.columns([3, 1])
    with title_column:
        section_title(f"Enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects")
    with button_column:
        st.write("")
        st.button("Enrol in a subject", type="primary", on_click=enrol_click)

    st.progress(len(student.subjects) / MAX_SUBJECTS)
    show_subject_cards(student, allow_drop=True)
