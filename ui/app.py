import streamlit as st
from pipeline.mainPipeline import run_requirement_analysis

st.set_page_config(
    page_title="AI Requirements Analyzer and Test Case Generator",
    layout="wide"
)

st.title("📘 AI-Based Requirements Analyzer")
st.markdown("Analyze software requirements and auto-generate test cases.")

# User Input
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
            result = run_requirement_analysis(user_input)  # slight change needed

        st.success("Analysis completed!")

        # ---------------- Functional Requirements ----------------
        st.subheader("✅ Functional Requirements")
        for i, fr in enumerate(result.functional_requirements, 1):
            st.markdown(f"**FR-{i}:** {fr}")

        # ---------------- Ambiguities ----------------
        st.subheader("⚠️ Ambiguities")
        if result.ambiguities:
            for i, amb in enumerate(result.ambiguities, 1):
                st.markdown(f"- {amb}")
        else:
            st.info("No ambiguities detected.")

        # ---------------- Positive Tests ----------------
        st.subheader("🟢 Positive Test Cases")
        for i, tc in enumerate(result.positive_tests, 1):
            st.markdown(f"- **TC-P-{i}:** {tc}")

        # ---------------- Negative Tests ----------------
        st.subheader("🔴 Negative Test Cases")
        for i, tc in enumerate(result.negative_tests, 1):
            st.markdown(f"- **TC-N-{i}:** {tc}")

        # ---------------- Edge Cases ----------------
        st.subheader("🟡 Edge Case Test Cases")
        for i, tc in enumerate(result.edge_case_tests, 1):
            st.markdown(f"- **TC-E-{i}:** {tc}")