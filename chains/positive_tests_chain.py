from langchain_openrouter import ChatOpenRouter
from typing import List
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from prompts.PositiveTestsChain_Prompt import PositiveTestsPrompt
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()

class PositiveTestsSchema(BaseModel):
    positive_tests: List[str] = Field(description="What are the positive test cases of the requirements",default_factory=list)

model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0
)

strPraser = StrOutputParser()

positive_tests_parser = PydanticOutputParser(
    pydantic_object=PositiveTestsSchema
)

PositiveTestsCaseGenerationChain = PositiveTestsPrompt | model | strPraser | positive_tests_parser

