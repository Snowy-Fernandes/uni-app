import streamlit as st

from gui.actions import check_login, show_message
from gui.components import show_html

LOGIN_HEADER = (
    '<div class="logo-mark">U</div>'
    '<h1 class="login-title">Welcome back</h1>'
    '<p class="login-sub">Please enter your account details</p>'
)

INFO_PANEL = (
    '<div class="info-panel"><span class="ring"></span>'
    '<h2>Your semester,<br>organised.</h2>'
    '<p>Enrol in up to four subjects, watch your marks and follow your progress in one place.</p>'
    '<div class="info-card"><b>New student?</b>'
    '<p>Register first with the command line app: python main_cli.py</p></div></div>'
)


def show_login_page():
    with st.container(key="glass_login"):
        left, right = st.columns(2, gap="large")

        with left:
            show_html(LOGIN_HEADER)
            show_message()
            with st.form("login_form"):
                email = st.text_input("Email", placeholder="firstname.lastname@university.com")
                password = st.text_input("Password", type="password", placeholder="Your password")
                sign_in_pressed = st.form_submit_button("Sign in", type="primary")

            if sign_in_pressed:
                error = check_login(email.strip(), password)
                if error:
                    st.error(error)
                else:
                    st.rerun()

        with right:
            show_html(INFO_PANEL)
