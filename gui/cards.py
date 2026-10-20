import streamlit as st

from gui.actions import drop_click
from gui.components import show_html, clickable
from gui.dialogs import stat_dialog, subject_dialog
from models.student import MAX_SUBJECTS, PASS_MARK


def stat_card_html(label, value, color=""):
    return (f'<div class="stat-card"><div class="stat-label">{label}</div>'
            f'<div class="stat-value {color}">{value}</div><div class="hint">View details</div></div>')


def subject_card_html(subject):
    result = "Pass" if subject.mark >= PASS_MARK else "Fail"
    return (
        f'<div class="subject-card g-{subject.grade}">'
        f'<div class="subject-top"><span class="subject-code">Subject {subject.id:03d}</span>'
        f'<span class="badge">{subject.grade}</span></div>'
        f'<div class="subject-mark">{subject.mark}<small> / 100</small></div>'
        f'<div class="bar"><div class="bar-fill" style="width:{subject.mark}%"></div></div>'
        f'<div class="hint" style="margin-top:10px">{result} - view details</div></div>'
    )


def show_stat_cards(student):
    count = len(student.subjects)
    has_subjects = count > 0
    cards = [
        ("subjects", "Subjects", f"{count} / {MAX_SUBJECTS}", ""),
        ("average", "Average mark", f"{student.average_mark():.2f}" if has_subjects else "-", ""),
        ("grade", "Overall grade", student.grade() if has_subjects else "-", ""),
        ("result", "Result", ("PASS" if student.has_passed() else "FAIL") if has_subjects else "-",
         ("good" if student.has_passed() else "bad") if has_subjects else ""),
    ]
    for column, (kind, label, value, color) in zip(st.columns(4), cards):
        with column:
            if clickable(f"stat_{kind}", stat_card_html(label, value, color)):
                stat_dialog(kind, student)


def show_subject_cards(student, allow_drop=False):
    columns = st.columns(MAX_SUBJECTS)
    for number in range(MAX_SUBJECTS):
        with columns[number]:
            if number >= len(student.subjects):
                show_html(f'<div class="slot"><div>Free slot {number + 1}</div></div>')
                continue
            subject = student.subjects[number]
            if clickable(f"sub_{subject.id}", subject_card_html(subject)):
                subject_dialog(subject)
            if allow_drop:
                st.button("Drop", key=f"drop_{subject.id}", on_click=drop_click, args=(subject.id,))
