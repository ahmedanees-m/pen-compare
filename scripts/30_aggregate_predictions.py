"""Aggregate all 4 pre-registered prediction results.

Reads results/pred_P{1..5}.json and writes results/PREREG_OUTCOME.json.
Prints the publication ladder determination.
"""

import json
import sys
from pathlib import Path

RESULTS_DIR = Path("results")
PIDS = ["P1", "P2", "P3", "P4"]

LADDER = {
    4: "Bioinformatics Application Note",
    3: "Bioinformatics Application Note (reframed contributions)",
}

results = {}
for pid in PIDS:
    f = RESULTS_DIR / f"pred_{pid}.json"
    if not f.exists():
        print(f"WARNING: {f} not found - treating {pid} as missing")
        results[pid] = {"PASS": False, "statement": f"{pid} result file not found"}
    else:
        results[pid] = json.loads(f.read_text())

n_pass = sum(1 for r in results.values() if r.get("PASS"))

print("\n")
print(" PEN-COMPARE Pre-Registration Outcome ")
print("")
for pid, r in results.items():
    icon = "" if r.get("PASS") else ""
    stmt = r.get("statement", "")[:55]
    print(f" {icon} {pid}: {stmt:<55}")
print("")
print(f" Pass rate: {n_pass}/5 ")
pub_path = LADDER.get(n_pass, "Halt and rework (<=2 PASS)")
print(f" Publication path: {pub_path:<37}")
print("")

outcome = {
    "n_pass": n_pass,
    "n_total": 5,
    "publication_path": pub_path,
    "predictions": {
        pid: {
            "PASS": r.get("PASS"),
            "statement": r.get("statement", ""),
        }
        for pid, r in results.items()
    },
}

OUT = RESULTS_DIR / "PREREG_OUTCOME.json"
OUT.write_text(json.dumps(outcome, indent=2))
print(f"\nWrote {OUT}")

if n_pass < 3:
    print("\nPASS rate < 3/5 - per stopping rules: halt and rework.")
    sys.exit(1)
