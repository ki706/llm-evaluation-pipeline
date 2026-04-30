class JudgmentEngine:

    def decide(self, case):
        """
        Simulates human evaluation decision making.
        """

        a = case["response_a"]
        b = case["response_b"]

        reasoning = {}

        # Example reasoning logic (NOT ML, HUMAN STYLE SIMULATION)

        if len(a) > len(b):
            reasoning["length_bias"] = "A is more detailed"

        if "both" in b.lower():
            reasoning["balance"] = "B is more balanced"

        # Final decision (simulated human judgment)
        decision = "B" if "balanced" in b.lower() else "A"

        return {
            "winner": decision,
            "reasoning": reasoning
        }
