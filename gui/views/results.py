import streamlit as st

from gui.charts import grade_chart
from gui.components import show_empty, section_title
from models.student import PASS_MARK


def show_results(student):
    if not student.subjects:
        show_empty()
        return

    table_column, chart_column = st.columns([1.4, 1])
    with table_column:
        with st.container(key="glass_table"):
            st.markdown("#### Subject results")
            rows = [{"Subject": f"{s.id:03d}", "Mark": s.mark, "Grade": s.grade,
                     "Result": "Pass" if s.mark >= PASS_MARK else "Fail"} for s in student.subjects]
            st.dataframe(rows, hide_index=True)
    with chart_column:
        with st.container(key="glass_grades"):
            st.markdown("#### Grade split")
            grade_chart(student)

    result = "PASS" if student.has_passed() else "FAIL"
    section_title(f"Overall: {result} with an average mark of {student.average_mark():.2f}")
