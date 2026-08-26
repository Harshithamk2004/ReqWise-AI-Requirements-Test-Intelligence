from langchain_core.prompts import PromptTemplate

PositiveTestsPrompt = PromptTemplate(
    input_variables=["functional_requirements"],
    template="""
Generate positive (happy path) test scenarios based ONLY on the given functional requirements.

Rules:
- Use only the provided functional requirements.
- Do NOT introduce new rules or assumptions.
- Tests should represent valid and successful usage.
- Each test case should be clear and concise.

Functional Requirements:
{functional_requirements}

Output format:
{{
  "positive_tests": [
    "..."
  ]
}}
"""
)