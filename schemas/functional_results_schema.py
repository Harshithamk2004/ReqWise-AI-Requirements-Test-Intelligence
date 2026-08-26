from typing import List
from pydantic import Field, BaseModel

class RequirementResults(BaseModel):
    functional_requirements: List[str] = Field(description="What are the functional requirements",default_factory=list)
    ambiguities: List[str] = Field(description="What are the ambiguities in requirements",default_factory=list)