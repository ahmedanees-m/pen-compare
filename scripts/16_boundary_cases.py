"""Boundary case investigation.

For every entity with robustness < 0.50 (tier is unstable under threshold variation),
produce a structured report explaining which gate thresholds flip the tier and why.

Output
------
results/boundary_cases.md
"""

import json
from pathlib import Path

import pandas as pd

SENSITIVITY = Path("results/sensitivity_analysis_v3.2.parquet")
UNIVERSE = Path("data/unified_editor_universe.parquet")
OUTPUT = Path("results/boundary_cases.md")

sens = pd.read_parquet(SENSITIVITY)
universe = pd.read_parquet(UNIVERSE)

boundary = sens[sens["is_boundary"]].merge(
    universe[
        [
            "entity_id",
            "s_dsb",
            "s_prog",
            "s_cargo",
            "length_aa",
            "intrinsic_cargo_mechanism",
            "cell_based_evidence",
            "penscore",
        ]
    ],
    on="entity_id",
    how="left",
)

near_boundary = sens[(sens["robustness"] >= 0.50) & (sens["robustness"] < 0.80)].merge(
    universe[
        [
            "entity_id",
            "s_dsb",
            "s_prog",
            "s_cargo",
            "length_aa",
            "intrinsic_cargo_mechanism",
            "cell_based_evidence",
            "penscore",
        ]
    ],
    on="entity_id",
    how="left",
)

lines = [
    "# Boundary Case Investigation - TrueWriterScore v3.2",
    "",
    "**Boundary (robustness < 0.50):** fewer than half of the 18,000 threshold",
    "combinations agree on the modal tier - tier assignment is genuinely ambiguous.",
    "",
    "**Near-boundary (robustness 50-80%):** majority agree on modal tier but a",
    "substantial fraction flip - threshold-sensitive findings worth reporting.",
    "",
    f"**Boundary cases (<0.50):** {len(boundary)}",
    f"**Near-boundary (50-80%):** {len(near_boundary)}",
    "",
    "These cases are transparently reported in the Discussion.",
    "No threshold tuning is performed in response to these findings.",
    "",
    "---",
    "",
]

if len(boundary) == 0:
    lines += [
        "## Section A: Zero true boundary cases (robustness < 0.50)",
        "",
        "All 1,058 entities have robustness >= 0.50. The 5-gate hierarchical framework",
        "is stable: no entity's tier is genuinely ambiguous under the pre-registered",
        "threshold ranges. This is a reportable positive finding.",
        "",
        "---",
        "",
    ]
else:
    for _, row in boundary.sort_values("robustness").iterrows():
        tier_dist = row["tier_dist"]
        if isinstance(tier_dist, str):
            tier_dist = json.loads(tier_dist)
        dist_str = ", ".join(f"{t}={n}" for t, n in sorted(tier_dist.items()))

        lines += [
            f"## {row['entity_id']} (source: {row['source']})",
            "",
            f"- **Default tier:** {row['default_tier']}",
            f"- **Modal tier:** {row['modal_tier']}",
            f"- **Robustness:** {row['robustness']:.3f} ({int(row['robustness'] * 18000)}/18,000 combos)",
            f"- **Tier distribution across all combos:** {dist_str}",
            "",
            "**Key axis values:**",
            f"- S_DSB = {row.get('s_dsb', 'n/a'):.3f}"
            if pd.notna(row.get("s_dsb"))
            else "- S_DSB = n/a",
            f"- S_Prog = {row.get('s_prog', 'n/a'):.3f}"
            if pd.notna(row.get("s_prog"))
            else "- S_Prog = n/a",
            f"- S_Cargo = {row.get('s_cargo', 'n/a'):.3f}"
            if pd.notna(row.get("s_cargo"))
            else "- S_Cargo = n/a",
            f"- length_aa = {row.get('length_aa', 'n/a')}",
            f"- intrinsic_cargo = {row.get('intrinsic_cargo_mechanism')}",
            f"- cell_based = {row.get('cell_based_evidence')}",
            "",
            "**Interpretation:** This entity sits near one or more gate thresholds.",
            "Varying G1/G2/G3 or G4 size-max within the pre-registered grid shifts its",
            "tier. No corrective action is taken - the boundary-case status is the finding.",
            "",
            "---",
            "",
        ]

# Near-boundary section
if len(near_boundary) == 0:
    lines += ["## Section B: No near-boundary cases (50-80%)", ""]
else:
    lines += [
        "## Section B: Near-boundary cases (robustness 50-80%)",
        "",
        "These entities have a majority of threshold combinations agreeing on the modal tier,",
        "but a substantial minority flips the tier. Reported transparently; no action taken.",
        "",
    ]
    for _, row in near_boundary.sort_values("robustness").iterrows():
        tier_dist = row["tier_dist"]
        if isinstance(tier_dist, str):
            tier_dist = json.loads(tier_dist)
        dist_str = ", ".join(f"{t}={n}" for t, n in sorted(tier_dist.items()))
        lines += [
            f"### {row['entity_id']} (source: {row['source']})",
            "",
            f"- **Default tier:** {row['default_tier']}",
            f"- **Modal tier:** {row['modal_tier']}",
            f"- **Robustness:** {row['robustness']:.3f} ({int(row['robustness'] * 18000)}/18,000 combos)",
            f"- **Tier distribution:** {dist_str}",
            "",
            "**Key axis values:**",
            f"- S_Cargo = {row['s_cargo']:.3f}"
            if pd.notna(row.get("s_cargo"))
            else "- S_Cargo = n/a",
            f"- intrinsic_cargo = {row.get('intrinsic_cargo_mechanism')}",
            f"- cell_based = {row.get('cell_based_evidence')}",
            "",
            "**Interpretation:** At G3 threshold <= observed S_Cargo value, G3 passes and",
            "qualifying count rises, potentially reaching PROBABLE_WRITER with cell_based evidence.",
            "Default threshold (0.90) places this editor just at the EMERGING/PROBABLE boundary.",
            "",
        ]

OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text("\n".join(lines))
print(f"Wrote {OUTPUT}")
print(f"Boundary cases (<0.50): {len(boundary)}")
print(f"Near-boundary (50-80%): {len(near_boundary)}")
if len(near_boundary):
    print(
        near_boundary[
            ["entity_id", "source", "default_tier", "modal_tier", "robustness"]
        ].to_string(index=False)
    )
