from evaluation.scoring_engine import score_response
from evaluation.error_classifier import ErrorClassifier


class Evaluator:

    def __init__(self):
        self.error_classifier = ErrorClassifier()

    def evaluate(self, response, reference):
        """
        Full evaluation of a model response against reference answer.
        Returns structured evaluation result.
        """

        # 1. Compute score
        score = score_response(response, reference)

        # 2. Detect error type
        error_type = self.error_classifier.classify(response, reference)

        # 3. Determine final grade
        if score >= 1.5:
            grade = "good"
        elif score >= 1.0:
            grade = "acceptable"
        else:
            grade = "poor"

        # 4. Build evaluation result
        result = {
            "id": response["id"],
            "score": score,
            "error_type": error_type,
            "grade": grade
        }

        return result
