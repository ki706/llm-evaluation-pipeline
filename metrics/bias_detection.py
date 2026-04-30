def detect_bias(evaluations):
    """
    Simple placeholder bias detection logic.
    """

    bias_flags = 0

    for e in evaluations:
        if e["grade"] == "poor" and e["error_type"] == "off_prompt":
            bias_flags += 1

    return {
        "bias_score": round(bias_flags / len(evaluations), 4) if evaluations else 0.0
    }
