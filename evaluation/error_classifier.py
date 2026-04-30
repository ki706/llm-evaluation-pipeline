class ErrorClassifier:

    def __init__(self):
        self.error_types = [
            "hallucination",
            "incorrect_reasoning",
            "missing_key_info",
            "off_prompt",
            "partially_correct"
        ]

    def classify(self, response, reference):
        """
        Returns the most likely error type for a model response.
        """

        response_text = response["response"].lower()
        reference_text = reference["answer"].lower()

        # 1. Off-topic / irrelevant response
        if len(response_text) < 10:
            return "off_prompt"

        # 2. Simple overlap heuristic (baseline logic)
        overlap = any(word in response_text for word in reference_text.split())

        if not overlap:
            return "hallucination"

        # 3. Partial match check
        if len(response_text.split()) < len(reference_text.split()) * 0.6:
            return "missing_key_info"

        # 4. Default case
        if overlap:
            return "partially_correct"

        return "incorrect_reasoning"
