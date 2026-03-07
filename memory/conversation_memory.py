class ConversationMemory:

    memory_store = {}

    @classmethod
    def save_results(cls, user_id, query, results):

        cls.memory_store[user_id] = {
            "last_query": query,
            "last_results": results
        }

    @classmethod
    def get_results(cls, user_id):

        return cls.memory_store.get(user_id, {}).get("last_results")

    @classmethod
    def get_query(cls, user_id):

        return cls.memory_store.get(user_id, {}).get("last_query")

    # ⭐ Helper for MCP tools
    @classmethod
    def get_top_candidates(cls, user_id, n=2):

        results = cls.get_results(user_id)

        if not results:
            return []

        return results[:n]