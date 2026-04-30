
def score_response(response, reference):
    score = 0

    # simple evaluation logic (baseline system)
    if response["id"] == reference["id"]:
        score += 1

    if len(response["response"]) > 20:
        score += 0.5

    return round(score, 2)
