import altair as alt
import pandas as pd
import streamlit as st

from gui.theme import GRADE_COLORS
from models.student import PASS_MARK

BROWN = "#8b5e3c"
DARK = "#4a3428"


def draw(chart):
    chart = chart.properties(height=250).configure(background="transparent", font="Poppins")
    chart = chart.configure_view(strokeWidth=0)
    chart = chart.configure_axis(labelColor=DARK, titleColor=DARK, gridColor="#e6d9c8", domainColor="#d8c6ae")
    chart = chart.configure_legend(labelColor=DARK, titleColor=DARK)
    try:
        st.altair_chart(chart, width="stretch", theme=None)
    except TypeError:
        st.altair_chart(chart, use_container_width=True, theme=None)


def marks_chart(student):
    data = pd.DataFrame({
        "Subject": [f"{s.id:03d}" for s in student.subjects],
        "Mark": [s.mark for s in student.subjects],
    })
    bars = alt.Chart(data).mark_bar(color=BROWN, size=44, cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
        x=alt.X("Subject:N", title=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y("Mark:Q", scale=alt.Scale(domain=[0, 100])),
        tooltip=["Subject", "Mark"],
    )
    line = alt.Chart(pd.DataFrame({"PassMark": [PASS_MARK]})).mark_rule(color="#c0583f", strokeDash=[6, 4]).encode(y="PassMark:Q")
    draw(bars + line)


def progress_chart(student):
    marks = [s.mark for s in student.subjects]
    data = pd.DataFrame({
        "Subjects": list(range(1, len(marks) + 1)),
        "Average": [sum(marks[:i + 1]) / (i + 1) for i in range(len(marks))],
    })
    base = alt.Chart(data).encode(
        x=alt.X("Subjects:O", title="Subjects enrolled", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("Average:Q", scale=alt.Scale(domain=[0, 100])),
        tooltip=["Subjects", "Average"],
    )
    area = base.mark_area(color="#c49a6c", opacity=0.25)
    line = base.mark_line(color=BROWN, strokeWidth=3, point=alt.OverlayMarkDef(color=DARK, size=80))
    draw(area + line)


def grade_chart(student):
    grades = [s.grade for s in student.subjects]
    data = pd.DataFrame({"Grade": sorted(set(grades)), "Count": [grades.count(g) for g in sorted(set(grades))]})
    colors = alt.Scale(domain=list(GRADE_COLORS), range=list(GRADE_COLORS.values()))
    draw(alt.Chart(data).mark_arc(innerRadius=55).encode(
        theta="Count:Q", color=alt.Color("Grade:N", scale=colors), tooltip=["Grade", "Count"]))
