from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from prompts.System_Prompt import SystemPrompt
from prompts.FunctionalRequirement_Prompt import FunctionalRequirementPrompt
from prompts.AmbiguityChain_Prompt import FindAmbiguityPrompt
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from schemas.functional_results_schema import RequirementResults

load_dotenv()

model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0
)

RequirementResultsChain = model.with_structured_output(RequirementResults)

combinedPromptForFunctionalRequirement = ChatPromptTemplate.from_messages([
    ("system", SystemPrompt),
    ("human", FunctionalRequirementPrompt)
])

ambiguity_prompt = ChatPromptTemplate.from_messages([
    ("system", SystemPrompt),
    ("human", FindAmbiguityPrompt)
])

parallel_chain = RunnableParallel({
    'functionalRequirement': combinedPromptForFunctionalRequirement | RequirementResultsChain,
    'ambiguities': ambiguity_prompt | RequirementResultsChain
})