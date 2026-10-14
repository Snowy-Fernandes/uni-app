import streamlit as st

from gui.actions import go_to, logout
from gui.components import show_html

CAP_ICON = (
    '<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5z"/>'
    '<path d="M6 12v5c3 2 9 2 12 0v-5"/><path d="M22 10v6"/></svg>'
)


def show_sidebar(pages):
    if st.session_state.page not in pages:
        st.session_state.page = pages[0]

    with st.sidebar:
        show_html(f'<div class="side-logo">{CAP_ICON}</div>'
                  '<div class="side-name">UniEnrol<small>Student portal</small></div>')
        for name in pages:
            is_current = st.session_state.page == name
            st.button(name, key="nav_" + name.lower().replace(" ", "_"), on_click=go_to, args=(name,),
                      type="primary" if is_current else "secondary")
        show_html('<div class="side-space"></div>')
        st.button("Log out", key="nav_logout", on_click=logout)
    return st.session_state.page
