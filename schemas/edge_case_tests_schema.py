from typing import List
from pydantic import Field, BaseModel

class EdgeCaseTestsSchema(BaseModel):
    edgeCase_tests: List[str] = Field(description="What are the positive test cases of the requirements",default_factory=list)