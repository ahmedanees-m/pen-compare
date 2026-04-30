"""Run sensitivity analysis on the full 1,058-entity universe.

18,000 threshold combinations x 1,058 entities = 19,044,000 certifications.
Parallelised with joblib across 24 CPU cores (~1 hour wall time on VM).

Outputs
-------
results/sensitivity_analysis_v3.2.parquet
"""

import sys
from pathlib import Path

import pandas as pd

from pen_compare.core.sensitivity import run_sensitivity_parallel

UNIVERSE = Path("data/unified_editor_universe.parquet")
SCORECARD = Path("results/truewriter_scorecard_v3.2.parquet")
OUTPUT = Path("results/sensitivity_analysis_v3.2.parquet")

print("Loading universe and scorecard ...")
universe = pd.read_parquet(UNIVERSE)
scorecard = pd.read_parquet(SCORECARD)
print(f"  Universe : {len(universe):,} entities")
print(f"  Scorecard: {len(scorecard):,} entities")

print("\nRunning sensitivity analysis (18,000 combos per entity) ...")
sens = run_sensitivity_parallel(universe, scorecard, n_jobs=24)

sens.to_parquet(OUTPUT, index=False)
print(f"\nSaved -> {OUTPUT}")

print("\n=== Robustness summary ===")
print(sens["robustness"].describe().round(3))
print(f"\nRobust   (>=80 % agreement) : {sens['is_robust'].sum():,}")
print(f"Boundary (<50 % agreement) : {sens['is_boundary'].sum():,}")
print(f"Between 50-80 %            : {(~sens['is_robust'] & ~sens['is_boundary']).sum():,}")

print("\n=== Modal tier distribution ===")
print(sens["modal_tier"].value_counts())

print("\n=== Default vs modal tier agreement ===")
agree = (sens["default_tier"] == sens["modal_tier"]).sum()
print(f"  {agree}/{len(sens)} entities agree ({100 * agree / len(sens):.1f} %)")

# Flag entities where default tier and modal tier diverge
diverge = sens[sens["default_tier"] != sens["modal_tier"]][
    ["entity_id", "source", "default_tier", "modal_tier", "robustness"]
]
if len(diverge):
    print(f"\n  Tier divergences ({len(diverge)}):")
    print(diverge.to_string(index=False))
else:
    print("  No tier divergences - default thresholds are modal for all entities.")

sys.exit(0)
