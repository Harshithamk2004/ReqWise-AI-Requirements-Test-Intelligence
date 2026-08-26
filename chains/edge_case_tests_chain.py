from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from prompts.EdgeCaseTestsChain_Prompt import EdgeCaseTestsPrompt
from langchain_core.output_parsers import StrOutputParser
from schemas.edge_case_tests_schema import EdgeCaseTestsSchema

load_dotenv()

model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0
)

EdgeCaseTestCaseResults = model.with_structured_output(EdgeCaseTestsSchema)

strPraser = StrOutputParser()

EdgeCaseTestsCaseGenerationChain = EdgeCaseTestsPrompt | model | strPraser | EdgeCaseTestCaseResults
