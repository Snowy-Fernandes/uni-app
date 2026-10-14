import streamlit as st

from gui.components import show_html, rows_html
from gui.theme import GRADE_RULES
from models.student import MAX_SUBJECTS, PASS_MARK


def subject_label(subject):
    return f"Subject {subject.id:03d}"


@st.dialog("Subject details")
def subject_dialog(subject):
    result = "Pass" if subject.mark >= PASS_MARK else "Fail"
    show_html(rows_html([
        ("Subject code", f"{subject.id:03d}"),
        ("Mark", f"{subject.mark} out of 100"),
        ("Grade", subject.grade),
        ("Result", result),
        (f"Difference from pass mark ({PASS_MARK})", f"{subject.mark - PASS_MARK:+d}"),
    ]))
    st.progress(subject.mark / 100)


def rows_for(kind, student):
    count = len(student.subjects)
    average = student.average_mark()
    marks = [(subject_label(s), f"{s.mark} (grade {s.grade})") for s in student.subjects]
    result = "PASS" if student.has_passed() else "FAIL"
    if kind == "subjects":
        return [("Enrolled", count), ("Free slots", MAX_SUBJECTS - count), ("Maximum allowed", MAX_SUBJECTS)] + marks
    if kind == "average":
        return marks + [("Average mark", f"{average:.2f}")]
    if kind == "grade":
        return [("Average mark", f"{average:.2f}"), ("Overall grade", student.grade())] + GRADE_RULES
    return [("Average mark", f"{average:.2f}"), ("Pass mark", PASS_MARK),
            ("Difference", f"{average - PASS_MARK:+.2f}"), ("Result", result)]


@st.dialog("Details")
def stat_dialog(kind, student):
    show_html(rows_html(rows_for(kind, student)))
    if kind == "average":
        st.caption("Average mark = total of all marks divided by the number of subjects.")
