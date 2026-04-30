"""P1: Among natural editors, exactly 1 will be TRUE_WRITER (ISCro4).

Pre-registered threshold: n_natural_TRUE == 1 AND "ISCro4" in true_writer_natural_editors
No threshold tuning permitted post-lock.
"""

import json
import sys
from pathlib import Path

import pandas as pd

SCORECARD = Path("results/truewriter_scorecard_v3.2.parquet")
OUTPUT = Path("results/pred_P1.json")

scorecard = pd.read_parquet(SCORECARD)
natural = scorecard[scorecard["source"] == "natural"]
natural_true = natural[natural["tier"] == "TRUE_WRITER"]

n = len(natural_true)
ids = natural_true["entity_id"].tolist()

passes = (n == 1) and ("ISCro4" in ids)

result = {
    "prediction": "P1",
    "statement": "Among natural editors, exactly 1 will be TRUE_WRITER (ISCro4).",
    "measurable_outcome": "n_natural_TRUE == 1 AND ISCro4 in true_writer_natural_editors",
    "observed_n_natural_TRUE": n,
    "observed_true_writer_ids": ids,
    "PASS": passes,
}

print(json.dumps(result, indent=2))
OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2))
print(f"\nResult written to {OUTPUT}")

if not passes:
    if n == 0:
        print("\nSTOPPING RULE: P1 fails (0 natural TRUE_WRITERs). No threshold tuning permitted.")
        print("Report ISCro4 gate-level failure and investigate.")
    elif n > 1:
        print(f"\nSTOPPING RULE: P1 fails ({n} natural TRUE_WRITERs). Report all; no tuning.")
    sys.exit(1)
