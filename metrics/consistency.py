def compute_consistency(evaluations):
    """
    Measures how consistent model outputs are in quality.
    """

    if len(evaluations) < 2:
        return 1.0

    grades = [e["grade"] for e in evaluations]

    stable = 0
    for i in range(1, len(grades)):
        if grades[i] == grades[i - 1]:
            stable += 1

    consistency = stable / (len(grades) - 1)

    return round(consistency, 4)
