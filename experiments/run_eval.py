import json
from evaluation.scoring_engine import score_response

def load(file):
    with open(file, "r") as f:
        return json.load(f)

prompts = load("data/prompts/prompts.json")
outputs = load("data/model_outputs/responses.json")
gold = load("data/reference/gold_answers.json")

results = []

for o in outputs:
    ref = next(g for g in gold if g["id"] == o["id"])
    score = score_response(o, ref)

    results.append({
        "id": o["id"],
        "score": score
    })

print(results)
