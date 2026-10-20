import streamlit as st

from gui.cards import show_stat_cards
from gui.charts import marks_chart, progress_chart
from gui.components import show_banner, section_title, show_empty


def show_dashboard(student):
    first_name = student.name.split(" ")[0] if student.name else "student"
    show_banner(f"Welcome back, {first_name}", "Track your enrolment, marks and progress in your student portal.")

    section_title("Overview")
    show_stat_cards(student)

    section_title("Your progress")
    if not student.subjects:
        show_empty()
        return

    left, right = st.columns(2)
    with left:
        with st.container(key="glass_marks"):
            st.markdown("#### Marks by subject")
            marks_chart(student)
    with right:
        with st.container(key="glass_progress"):
            st.markdown("#### Average mark progress")
            progress_chart(student)
