"""P2: Zero pen-assemble designs will be TRUE_WRITER.

Pre-registered threshold: n_design_TRUE == 0
No threshold tuning permitted post-lock.
"""

import json
import sys
from pathlib import Path

import pandas as pd

SCORECARD = Path("results/truewriter_scorecard_v3.2.parquet")
OUTPUT = Path("results/pred_P2.json")

scorecard = pd.read_parquet(SCORECARD)
designs = scorecard[scorecard["source"] == "design"]
design_true = designs[designs["tier"] == "TRUE_WRITER"]

n = len(design_true)
passes = n == 0

result = {
    "prediction": "P2",
    "statement": "Zero pen-assemble designs will be TRUE_WRITER.",
    "measurable_outcome": "n_design_TRUE == 0",
    "observed_n_design_TRUE": n,
    "observed_design_TRUE_ids": design_true["entity_id"].tolist()[:20],  # cap at 20 for readability
    "PASS": passes,
}

print(json.dumps(result, indent=2))
OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2))
print(f"\nResult written to {OUTPUT}")

if not passes:
    print(f"\nSTOPPING RULE: P2 fails ({n} designs are TRUE_WRITER).")
    print("Investigate pen-assemble v0.5.2 cell_based_evidence inheritance bug.")
    sys.exit(1)
