import json
from evaluation.judgment_engine import JudgmentEngine

def load(file):
    with open(file, "r") as f:
        return json.load(f)

cases = load("data/ambiguous/judgment_cases.json")

engine = JudgmentEngine()

results = []

for c in cases:
    result = engine.decide(c)
    results.append({
        "id": c["id"],
        **result
    })

print(json.dumps(results, indent=2))
