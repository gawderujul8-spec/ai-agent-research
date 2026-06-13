import random

class AISummarizer:
    """
    Simulates an AI analysis of the semantic impact.
    In a real diploma project, this would call an LLM API (like GPT-4).
    """

    RISK_LEVELS = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

    PERSPECTIVES = [
        "Data Integrity: Modification here might affect how transactions are committed.",
        "User Experience: Changes in this flow could lead to unexpected UI state transitions.",
        "Scalability: This function is in a critical path; small changes might impact throughput.",
        "Security: Ensure that validation logic remains intact after these changes."
    ]

    def summarize(self, modified_func, impacted_funcs):
        risk = random.choice(self.RISK_LEVELS)
        perspective = random.choice(self.PERSPECTIVES)

        impact_list = ", ".join(impacted_funcs)

        return {
            "summary": f"AI analysis suggests a {risk} risk impact. Modifying '{modified_func}' "
                       f"semantically affects: {impact_list}.",
            "insight": perspective,
            "recommendation": f"Focus testing on the integration between {modified_func} and its callers."
        }
