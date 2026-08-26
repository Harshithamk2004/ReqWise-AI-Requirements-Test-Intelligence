from chains.positive_tests_chain import PositiveTestsCaseGenerationChain
from chains.negative_tests_chain import NegativeTestsCaseGenerationChain
from chains.edge_case_tests_chain import EdgeCaseTestsCaseGenerationChain
from schemas.final_output_schema import FinalRequirementAnalysis
from chains.functional_and_ambiguity_chain import parallel_chain
from langchain_core.runnables import RunnableParallel


def run_requirement_analysis(user_requirement: str):
    """
    Orchestrates the full requirement analysis pipeline.
    """

    fa_result = parallel_chain.invoke({
        "user_requirement": user_requirement
    })

    functional_requirements = fa_result[
        "functionalRequirement"
    ].functional_requirements

    ambiguities = fa_result[
        "ambiguities"
    ].ambiguities

    parallel_tests = RunnableParallel(
    positive=PositiveTestsCaseGenerationChain,
    negative=NegativeTestsCaseGenerationChain,
    edge=EdgeCaseTestsCaseGenerationChain
    ).invoke({
    "functional_requirements": functional_requirements
    })

    positive = parallel_tests["positive"]
    negative = parallel_tests["negative"]
    edge = parallel_tests["edge"]

    return FinalRequirementAnalysis(
        functional_requirements=functional_requirements,
        ambiguities=ambiguities,
        positive_tests=positive.positive_tests,
        negative_tests=negative.negative_tests,
        edge_case_tests=edge.edgeCase_tests
    )

if __name__ == "__main__":
    result = run_requirement_analysis()
    print("\n===== FINAL PIPELINE OUTPUT =====\n")
    print(result.model_dump())

    if result.ambiguities:
        print("\n⚠️ WARNING: Ambiguities detected but test cases were still generated.")