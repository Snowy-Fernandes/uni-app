import secrets

import streamlit as st

from models.database import Database
from models.student import MAX_SUBJECTS
from utils.validation import is_valid_email, is_valid_password

DEFAULT_PAGE = "Dashboard"

db = Database()


@st.cache_resource
def get_sessions():
    return {}


def start_session():
    if "student_id" not in st.session_state:
        st.session_state.student_id = get_sessions().get(st.query_params.get("session"))
    if "page" not in st.session_state:
        st.session_state.page = st.query_params.get("page", DEFAULT_PAGE)
    if "message" not in st.session_state:
        st.session_state.message = None


def current_student():
    if st.session_state.student_id is None:
        return None
    student = db.find_by_id(st.session_state.student_id)
    if student is None:
        st.session_state.student_id = None
    return student


def set_message(kind, text):
    st.session_state.message = (kind, text)


def show_message():
    if st.session_state.message is not None:
        kind, text = st.session_state.message
        if kind == "success":
            st.success(text)
        else:
            st.error(text)
        st.session_state.message = None


def check_login(email, password):
    if email == "" or password == "":
        return "Email and password cannot be empty"
    if not is_valid_email(email) or not is_valid_password(password):
        return "Incorrect email or password format"
    student = db.find_login(email, password)
    if student is None:
        return "Student does not exist"
    token = secrets.token_urlsafe(16)
    get_sessions()[token] = student.id
    st.query_params["session"] = token
    st.query_params["page"] = st.session_state.page
    st.session_state.student_id = student.id
    return None


def logout():
    get_sessions().pop(st.query_params.get("session"), None)
    st.query_params.clear()
    st.session_state.student_id = None
    st.session_state.page = DEFAULT_PAGE


def go_to(page):
    st.session_state.page = page
    st.query_params["page"] = page


def enrol_click():
    student = db.find_by_id(st.session_state.student_id)
    subject = student.enrol()
    if subject is None:
        set_message("error", f"Students are allowed to enrol in {MAX_SUBJECTS} subjects only")
        return
    db.update(student)
    set_message("success", f"Enrolled in Subject-{subject.id:03d}. "
                           f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects")


def drop_click(subject_id):
    student = db.find_by_id(st.session_state.student_id)
    if student.drop(subject_id):
        db.update(student)
        set_message("success", f"Dropped Subject-{subject_id:03d}. "
                               f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects")


def change_password(student, new_password, confirm):
    if not is_valid_password(new_password):
        return "Incorrect password format"
    if new_password != confirm:
        return "Password does not match - try again"
    student.password = new_password
    db.update(student)
    return None
