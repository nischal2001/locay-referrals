from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END

from services.query_parser import QueryParser
from tools.search_professionals_tool import SearchProfessionalsTool
from services.ranking_engine import RankingEngine


class ReferralState(TypedDict):
    user_input: str
    query: Dict
    candidates: List[Dict]
    results: List[Dict]


def parse_node(state):

    parsed = QueryParser.parse(state["user_input"])

    print("\nParsed Query:", parsed)

    return {"query": parsed}


def search_node(state):

    candidates = SearchProfessionalsTool.run(**state["query"])

    print("\nCandidates Found:", len(candidates))

    return {"candidates": candidates}


def ranking_node(state):

    ranked = RankingEngine.rank_candidates(
        state["query"],
        state["candidates"]
    )

    print("\nRanked Candidates:", len(ranked))

    return {"results": ranked}

def build_workflow():

    graph = StateGraph(ReferralState)

    graph.add_node("parse", parse_node)
    graph.add_node("search", search_node)
    graph.add_node("rank", ranking_node)

    graph.set_entry_point("parse")

    graph.add_edge("parse", "search")
    graph.add_edge("search", "rank")
    graph.add_edge("rank", END)

    return graph.compile()