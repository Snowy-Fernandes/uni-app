import streamlit as st

from gui.actions import change_password
from gui.components import show_html

RULES = ["Starts with a capital letter", "At least 5 letters in total", "Ends with 3 or more digits",
         "Example: Snowy2004"]


def show_password(student):
    form_column, rules_column = st.columns([1.3, 1], gap="large")

    with form_column:
        with st.container(key="glass_password"):
            st.markdown("#### Update your password")
            with st.form("password_form", clear_on_submit=True):
                new_password = st.text_input("New password", type="password")
                confirm = st.text_input("Confirm password", type="password")
                update_pressed = st.form_submit_button("Update password", type="primary")
            if update_pressed:
                error = change_password(student, new_password, confirm)
                if error:
                    st.error(error)
                else:
                    st.success("Password updated")

    with rules_column:
        with st.container(key="glass_rules"):
            st.markdown("#### Password rules")
            show_html("".join(f'<div class="detail-row"><span>{rule}</span></div>' for rule in RULES))
