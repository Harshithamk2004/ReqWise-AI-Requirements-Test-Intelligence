from langchain_openrouter import ChatOpenRouter
from typing import List
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from prompts.NegativeTestsChain_Prompt import NegativeTestsPrompt
from langchain_core.output_parsers import StrOutputParser
from schemas.negative_tests_schema import NegativeTestsSchema

load_dotenv()

model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0
)
NegativeTestCaseResults = model.with_structured_output(NegativeTestsSchema)

strPraser = StrOutputParser()

NegativeTestsCaseGenerationChain = NegativeTestsPrompt | model | strPraser | NegativeTestCaseResults


