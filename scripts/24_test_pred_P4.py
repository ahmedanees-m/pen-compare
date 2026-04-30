"""Evaluate prediction P4: RAG LLM accuracy >= 80% on 50-question benchmark.

Scoring: CORRECT if any gold_keyword appears (case-insensitive) in the LLM answer.
Writes results/pred_P4.json and results/llm_benchmark_full.json.
"""

import json
import sys
import time
from pathlib import Path

import yaml

from pen_compare.rag.qa import PenStackQA

REPO_ROOT = Path("/workspace/pen-compare")
BENCHMARK = REPO_ROOT / "prereg" / "llm_qa_benchmark_v1.0.yaml"
DB_PATH = REPO_ROOT / "data" / "rag_db"
OUT_SUMMARY = REPO_ROOT / "results" / "pred_P4.json"
OUT_FULL = REPO_ROOT / "results" / "llm_benchmark_full.json"

bench = yaml.safe_load(BENCHMARK.read_text())
questions = bench["questions"]
threshold = float(bench["pass_threshold"])
n_total = len(questions)
print(f"Benchmark: {n_total} questions, pass_threshold={threshold:.0%}")

qa = PenStackQA(db_path=DB_PATH)
print(f"ChromaDB vectors: {qa.collection_count()}")

records = []
n_correct = 0

for i, q in enumerate(questions):
    qid = q["id"]
    question = q["question"]
    keywords = q["gold_keywords"]

    t0 = time.time()
    answer = qa.ask(question)
    elapsed = time.time() - t0

    answer_lower = answer.lower()
    correct = any(kw.lower() in answer_lower for kw in keywords)
    if correct:
        n_correct += 1

    records.append(
        {
            "id": qid,
            "category": q.get("category", ""),
            "question": question,
            "gold_keywords": keywords,
            "answer": answer,
            "correct": correct,
            "latency_s": round(elapsed, 2),
        }
    )

    status = "OK" if correct else "FAIL"
    kw_hit = next((kw for kw in keywords if kw.lower() in answer_lower), "-")
    print(f"  [{status}] {qid} | kw_hit={kw_hit!r} | {elapsed:.1f}s")

accuracy = n_correct / n_total
passes = accuracy >= threshold

print("\n=== P4 result ===")
print(f"Correct: {n_correct}/{n_total} = {accuracy:.1%}")
print(f"Threshold: {threshold:.0%}")
print(f"Result: {'PASS' if passes else 'FAIL'}")

# Per-category breakdown
by_cat: dict[str, dict[str, int]] = {}
for r in records:
    cat = r["category"]
    by_cat.setdefault(cat, {"correct": 0, "total": 0})
    by_cat[cat]["total"] += 1
    if r["correct"]:
        by_cat[cat]["correct"] += 1

print("\nPer-category:")
for cat, d in sorted(by_cat.items()):
    print(f"  {cat}: {d['correct']}/{d['total']}")

summary = {
    "prediction": "P4",
    "statement": "Local-LLM RAG (llama3.1:8b-instruct-q4_K_M) correctly answers >= 80% of 50-question benchmark.",
    "model": bench.get("model", ""),
    "n_questions": n_total,
    "n_correct": n_correct,
    "accuracy": round(accuracy, 4),
    "threshold": threshold,
    "PASS": passes,
    "by_category": {
        cat: {
            "correct": d["correct"],
            "total": d["total"],
            "accuracy": round(d["correct"] / d["total"], 4),
        }
        for cat, d in by_cat.items()
    },
}

OUT_SUMMARY.parent.mkdir(exist_ok=True)
OUT_SUMMARY.write_text(json.dumps(summary, indent=2))
OUT_FULL.write_text(json.dumps(records, indent=2))
print(f"\nWrote {OUT_SUMMARY}")
print(f"Wrote {OUT_FULL}")

if not passes:
    print(f"\nP4 FAILS: accuracy={accuracy:.1%} < {threshold:.0%}")
    sys.exit(1)
