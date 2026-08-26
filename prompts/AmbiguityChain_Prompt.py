FindAmbiguityPrompt = """
Review the following requirement and identify ambiguities, unclear areas, or missing information.

Rules:
- Do NOT assume any behavior.
- If a detail is normally expected in software systems but not specified, list it as ambiguity.
- Focus on validations, limits, error handling, roles, permissions, and constraints.
- Phrase ambiguities as clarification points or questions.

Requirement:
{user_requirement}

If no ambiguities are found, return an empty list.

Return the result as plain text or JSON-like list of ambiguities.
"""