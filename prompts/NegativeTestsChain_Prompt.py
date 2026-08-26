from langchain_core.prompts import PromptTemplate

NegativeTestsPrompt = PromptTemplate(
    input_variables={"functional_requirements"},
    template="""
Generate negative test scenarios based ONLY on the given functional requirements.

Rules:
- Create negative tests only for explicitly stated rules.
- Do NOT create tests for missing or assumed validations.
- Focus on invalid inputs, missing mandatory actions, or rule violations.
- Do NOT include edge cases here.

Functional Requirements:
{functional_requirements}

Output format:
{{
  "negative_tests": [
    "..."
  ]
}}
"""
)