from concurrent.futures import ThreadPoolExecutor, as_completed
from services.compatibility_engine import CompatibilityEngine


class RankingEngine:

    @staticmethod
    def score_candidate(user_query, candidate):

        score_data = CompatibilityEngine.evaluate(user_query, candidate)

        return {
            "candidate": candidate,
            "score": score_data.get("score", 0),
            "reason": score_data.get("reason", "")
        }

    @staticmethod
    def rank_candidates(user_query, candidates, top_k=3):

        ranked_candidates = []

        # Run LLM scoring in parallel
        with ThreadPoolExecutor(max_workers=5) as executor:

            futures = [
                executor.submit(
                    RankingEngine.score_candidate,
                    user_query,
                    candidate
                )
                for candidate in candidates
            ]

            for future in as_completed(futures):
                ranked_candidates.append(future.result())

        # Sort candidates by score
        ranked_candidates.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked_candidates[:top_k]