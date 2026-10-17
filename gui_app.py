import streamlit as st

from gui.actions import start_session, current_student, show_message
from gui.components import show_topbar, footer
from gui.login_page import show_login_page
from gui.sidebar import show_sidebar
from gui.styles import load_styles
from gui.views.dashboard import show_dashboard
from gui.views.grade_guide import show_grade_guide
from gui.views.password import show_password
from gui.views.results import show_results
from gui.views.subjects import show_subjects

st.set_page_config(page_title="UniEnrol - Student Portal", layout="wide", initial_sidebar_state="expanded")

PAGES = {
    "Dashboard": show_dashboard,
    "My Subjects": show_subjects,
    "Results": show_results,
    "Grade Guide": show_grade_guide,
    "Change Password": show_password,
}

load_styles()
start_session()
student = current_student()

if student is None:
    show_login_page()
else:
    page = show_sidebar(list(PAGES))
    show_topbar(student, page)
    show_message()
    PAGES[page](student)
    footer()
