from langchain_core.prompts import PromptTemplate

EdgeCaseTestsPrompt = PromptTemplate(
    input_variables={"functional_requirements"},
    template="""
Generate edge case scenarios based ONLY on the given functional requirements.

Rules:
- Edge cases must be logical boundaries of stated requirements.
- Do NOT invent limits or constraints.
- Consider boundary values, extreme but valid conditions.
- If no boundaries are stated, generate no edge cases.

Functional Requirements:
{functional_requirements}

Output format:
{{
  "edge_cases": [
    "..."
  ]
}}
"""
)