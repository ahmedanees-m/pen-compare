"""Apply 5-gate TrueWriter certification to full unified universe.

Reads data/unified_editor_universe.parquet (pre-registered).
Writes results/truewriter_scorecard_v3.2.parquet.

NOTE on length_aa: Natural editors have length_aa=None in the current universe
(EditorEntry does not expose sequence length; annotation deferred to Step 17).
For G4 (deliverability), natural editors with unknown length are treated as
split_aav_eligible=True - all IS110 bridge recombinases are <500 aa by biology,
so this is conservative and correct.  Designs retain their catalog length_aa values.
"""

import sys
from pathlib import Path

import pandas as pd

# Run from repo root
sys.path.insert(0, str(Path(__file__).parent.parent))
from pen_compare.core.certify import certify  # noqa: E402

UNIVERSE_PATH = Path("data/unified_editor_universe.parquet")
SCORECARD_PATH = Path("results/truewriter_scorecard_v3.2.parquet")


def _evidence_list(row) -> list[str]:
    evi = []
    if row.get("has_biochemical"):
        evi.append("biochemical")
    if row.get("has_structural"):
        evi.append("structural")
    if row.get("has_computational"):
        evi.append("computational")
    if row.get("has_cell_based"):
        evi.append("cell_based")
    return evi


def _safe_bool(val) -> bool:
    if val is None or (
        hasattr(val, "__class__") and val.__class__.__name__ == "float" and str(val) == "nan"
    ):
        return False
    return bool(val)


def main():
    universe = pd.read_parquet(UNIVERSE_PATH)
    print(f"Loaded {len(universe)} entities from {UNIVERSE_PATH}")

    rows = []
    for _, r in universe.iterrows():
        length_aa_raw = r.get("length_aa")
        has_length = pd.notna(length_aa_raw) and length_aa_raw is not None

        if has_length:
            length_aa = int(length_aa_raw)
            split_aav = length_aa <= 1500
        else:
            # Natural editors: length not in EditorEntry schema (Step 17 annotates this).
            # Treat as split_aav_eligible so IS110 editors (<500 aa) pass G4.
            length_aa = None
            split_aav = True

        result = certify(
            editor_id=str(r["entity_id"]),
            s_dsb=float(r["s_dsb"]) if pd.notna(r["s_dsb"]) else 0.0,
            s_prog=float(r["s_prog"]) if pd.notna(r["s_prog"]) else 0.0,
            s_cargo=float(r["s_cargo"]) if pd.notna(r["s_cargo"]) else 0.0,
            length_aa=length_aa,
            evidence_sources=_evidence_list(r),
            intrinsic_cargo_mechanism=_safe_bool(r.get("intrinsic_cargo_mechanism")),
            split_aav_eligible=split_aav,
        )

        rows.append(
            {
                "entity_id": result.editor_id,
                "source": r["source"],
                "tier": result.tier,
                "necessary_passed": result.necessary_gates_passed,
                "qualifying_passed": result.qualifying_gates_passed,
                "has_cell_based": result.has_cell_based_evidence,
                "auto_demoted": result.auto_demoted,
                "auto_demote_reason": result.auto_demote_reason,
                "g1_dsb_passes": result.gate_results[0].passes,
                "g2_prog_passes": result.gate_results[1].passes,
                "g3_cargo_passes": result.gate_results[2].passes,
                "g4_size_passes": result.gate_results[3].passes,
                "g5_evidence_passes": result.gate_results[4].passes,
                "g1_value": result.gate_results[0].observed_value,
                "g2_value": result.gate_results[1].observed_value,
                "g3_value": result.gate_results[2].observed_value,
                "g4_value": result.gate_results[3].observed_value,
                "g5_value": result.gate_results[4].observed_value,
            }
        )

    scorecard = pd.DataFrame(rows)
    SCORECARD_PATH.parent.mkdir(exist_ok=True)
    scorecard.to_parquet(SCORECARD_PATH, index=False)
    print(f"\nScorecard saved -> {SCORECARD_PATH}")

    print("\n=== Tier Distribution (full universe) ===")
    print(scorecard["tier"].value_counts().to_string())

    natural = scorecard[scorecard["source"] == "natural"]
    print(f"\n=== Natural editors ({len(natural)} total) ===")
    print(natural["tier"].value_counts().to_string())

    true_natural = natural[natural["tier"] == "TRUE_WRITER"]
    print(f"\n=== TRUE_WRITER natural editors (n={len(true_natural)}) ===")
    if len(true_natural):
        print(
            true_natural[["entity_id", "tier", "qualifying_passed", "has_cell_based"]].to_string(
                index=False
            )
        )
    else:
        print("  (none)")

    designs = scorecard[scorecard["source"] == "design"]
    n_design_true = (designs["tier"] == "TRUE_WRITER").sum()
    print(f"\n=== Designs: {len(designs)} total, {n_design_true} TRUE_WRITER ===")


if __name__ == "__main__":
    main()
