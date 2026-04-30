def hallucination_rate(evaluations):
    """
    Calculates percentage of hallucinated responses.
    """

    if not evaluations:
        return 0.0

    hallucinations = 0

    for e in evaluations:
        if e["error_type"] == "hallucination":
            hallucinations += 1

    return round(hallucinations / len(evaluations), 4)
