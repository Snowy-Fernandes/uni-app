from html import escape

import streamlit as st


def show_html(text):
    st.markdown(text, unsafe_allow_html=True)


def section_title(text):
    show_html(f'<div class="section-title">{text}</div>')


def show_topbar(student, title):
    show_html(
        f'<div class="topbar"><h2>{title}</h2><div class="user-chip">'
        f'<div class="avatar">{escape(student.name[:1].upper())}</div>'
        f'<div>{escape(student.name)}<small>Student ID {student.id_text()}</small></div></div></div>'
    )


def show_banner(title, text):
    show_html(f'<div class="banner"><h1>{escape(title)}</h1><p>{text}</p></div>')


def show_empty():
    show_html('<div class="notice">You are not enrolled in any subject yet. Open My Subjects to enrol.</div>')


def rows_html(rows):
    items = "".join(f'<div class="detail-row"><span>{label}</span><b>{value}</b></div>' for label, value in rows)
    return f"<div>{items}</div>"


def clickable(key, card_html):
    with st.container(key=f"card_{key}"):
        show_html(card_html)
        return st.button("Open", key=f"open_{key}")


def footer():
    show_html('<div class="site-footer">32555 Fundamentals of Software Development - Group 10</div>')
