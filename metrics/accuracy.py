def compute_accuracy(evaluations):
    """
    Computes simple accuracy based on final grades.
    """

    if not evaluations:
        return 0.0

    correct = 0

    for item in evaluations:
        if item["grade"] == "good":
            correct += 1

    accuracy = correct / len(evaluations)

    return round(accuracy, 4)
