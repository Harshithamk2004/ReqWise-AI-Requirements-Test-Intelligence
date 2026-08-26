FunctionalRequirementPrompt = """
Analyze the following requirement and extract ONLY explicit functional requirements.

Rules:
- Extract only what is clearly stated.
- Do NOT assume validations, limits, or behaviors.
- If the requirement already contains explicit functional requirements, rewrite each one as a separate functional requirement statement.

Requirement:
{user_requirement}
"""
