import streamlit as st
from excel_utils import generate_excel
from pipeline.mainPipeline import run_requirement_analysis

st.set_page_config(
    page_title="AI Requirements Analyzer and Test Case Generator",
    layout="wide"
)

st.title("📘 AI-Based Requirements Analyzer")
st.markdown("Analyze software requirements and auto-generate test cases.")

# -------- Session State --------
if "result" not in st.session_state:
    st.session_state.result = None

# -------- User Input --------
user_input = st.text_area(
    "Enter Software Requirement",
    height=180,
    placeholder="Paste your requirement here..."
)

if st.button("Analyze Requirements"):
    if not user_input.strip():
        st.warning("Please enter a requirement.")
    else:
        with st.spinner("Analyzing requirements..."):
            st.session_state.result = run_requirement_analysis(user_input)

        st.success("Analysis completed!")

# -------- Show Result --------
if st.session_state.result:

    result = st.session_state.result

    st.markdown(f"""
        ### 📊 Summary
        - **Functional Requirements:** {len(result.functional_requirements)}
        - **Ambiguities:** {len(result.ambiguities)}
        - **Positive Test Cases:** {len(result.positive_tests)}
        - **Negative Test Cases:** {len(result.negative_tests)}
        - **Edge Case Test Cases:** {len(result.edge_case_tests)}
        """)

    # -------- Excel Download --------
    st.divider()
    st.subheader("📥 Export Report")

    file_path = generate_excel(result)

    with open(file_path, "rb") as f:
        st.download_button(
            label="Download Excel Report",
            data=f,
            file_name="Requirement_Analysis.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
