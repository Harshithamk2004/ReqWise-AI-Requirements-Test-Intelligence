from pydantic import BaseModel, Field
from typing import List

class FinalRequirementAnalysis(BaseModel):
    """
    Final combined output of the requirement analysis pipeline.
    """

    functional_requirements: List[str] = Field(
        default_factory=list,
        description="Extracted functional requirements from the user input"
    )

    ambiguities: List[str] = Field(
        default_factory=list,
        description="Ambiguities found in the requirements"
    )

    positive_tests: List[str] = Field(
        default_factory=list,
        description="Positive (happy path) test cases"
    )

    negative_tests: List[str] = Field(
        default_factory=list,
        description="Negative test cases"
    )

    edge_case_tests: List[str] = Field(
        default_factory=list,
        description="Edge case test scenarios"
    )
