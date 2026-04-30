"""Run cross-pipeline triangulation on the full universe and test P3.

P3 prediction: triangulation flags >= 5 mechanism discrepancies.
"""

import json
import sys
from pathlib import Path

import pandas as pd

from pen_compare.triangulation.triangulator import Triangulator

UNIVERSE = Path("data/unified_editor_universe.parquet")
OUTPUT_PQ = Path("results/triangulation_discrepancies.parquet")
OUTPUT_P3 = Path("results/pred_P3.json")

universe = pd.read_parquet(UNIVERSE)
print(f"Loaded universe: {len(universe):,} entities")

t = Triangulator()
discrepancies = t.run_full(universe)
OUTPUT_PQ.parent.mkdir(exist_ok=True)
discrepancies.to_parquet(OUTPUT_PQ, index=False)
print(f"Saved {len(discrepancies):,} discrepancy records -> {OUTPUT_PQ}")

print("\n=== Discrepancy summary by category ===")
if len(discrepancies):
    print(discrepancies["category"].value_counts().to_string())
    print("\n=== By severity ===")
    print(discrepancies["severity"].value_counts().to_string())
    print("\n=== Natural vs design ===")
    print(discrepancies["source"].value_counts().to_string())
else:
    print("(none)")

# P3 evaluation
n = len(discrepancies)
passes = n >= 5
result = {
    "prediction": "P3",
    "statement": "Cross-pipeline triangulation flags >= 5 mechanism discrepancies.",
    "measurable_outcome": "n_discrepancies >= 5",
    "observed_n_discrepancies": int(n),
    "discrepancy_by_category": (
        discrepancies["category"].value_counts().to_dict() if len(discrepancies) else {}
    ),
    "discrepancy_by_severity": (
        discrepancies["severity"].value_counts().to_dict() if len(discrepancies) else {}
    ),
    "PASS": passes,
}
print("\n=== P3 result ===")
print(json.dumps(result, indent=2))
OUTPUT_P3.write_text(json.dumps(result, indent=2))
print(f"\nResult written to {OUTPUT_P3}")

if not passes:
    print(f"\nP3 FAILS: only {n} discrepancies found (need >= 5).")
    sys.exit(1)
