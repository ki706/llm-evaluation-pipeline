import json

from evaluation.evaluator import Evaluator
from metrics.accuracy import compute_accuracy
from metrics.consistency import compute_consistency
from metrics.hallucination_check import hallucination_rate
from metrics.bias_detection import detect_bias


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def main():

    prompts = load_json("data/prompts/prompts.json")
    outputs = load_json("data/model_outputs/responses.json")
    gold = load_json("data/reference/gold_answers.json")

    evaluator = Evaluator()

    evaluations = []

    # 1. Run evaluation loop
    for response in outputs:
        reference = next(g for g in gold if g["id"] == response["id"])

        result = evaluator.evaluate(response, reference)
        evaluations.append(result)

    # 2. Compute metrics
    report = {
        "accuracy": compute_accuracy(evaluations),
        "consistency": compute_consistency(evaluations),
        "hallucination_rate": hallucination_rate(evaluations),
        "bias_signal": detect_bias(evaluations)
    }

    # 3. Save logs
    with open("logs/evaluation_logs.json", "w") as f:
        json.dump(evaluations, f, indent=2)

    # 4. Print summary report
    print("\n=== EVALUATION SUMMARY ===")
    for k, v in report.items():
        print(f"{k}: {v}")

    # 5. Save report
    with open("reports/evaluation_report.json", "w") as f:
        json.dump(report, f, indent=2)


if __name__ == "__main__":
    main()
