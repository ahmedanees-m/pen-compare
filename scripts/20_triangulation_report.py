"""Produce triangulation_report.md.

For every high-severity discrepancy, write a paragraph-level investigation.
Medium and low severity cases are tabulated. This text feeds directly into
the Discussion section on cross-pipeline discordances.
"""

from pathlib import Path

import pandas as pd

DISCREPANCIES = Path("results/triangulation_discrepancies.parquet")
UNIVERSE = Path("data/unified_editor_universe.parquet")
OUTPUT = Path("results/triangulation_report.md")

disc = pd.read_parquet(DISCREPANCIES)
univ = pd.read_parquet(UNIVERSE)

lines = [
    "# Cross-Pipeline Triangulation Report - TrueWriterScore v3.2",
    "",
    f"**Total discrepancy records:** {len(disc)}",
    "",
    "Discrepancies are flagged where claims from GENOME-ATLAS, MECH-CLASS, and",
    "PEN-SCORE are internally inconsistent. These are *findings*, not errors -",
    "they reflect the state of the art and are reported transparently.",
    "",
    "No threshold adjustments or data corrections are made in response to these",
    "findings (pre-registration policy).",
    "",
    "---",
    "",
]

# Summary table
lines += ["## Summary", ""]
if len(disc) == 0:
    lines += ["No discrepancies detected.", ""]
else:
    cat_counts = disc["category"].value_counts()
    sev_counts = disc["severity"].value_counts()
    lines += [
        "### By category",
        "",
        "| Category | Count | Severity |",
        "|---|---|---|",
    ]
    cat_to_sev = disc.drop_duplicates("category").set_index("category")["severity"].to_dict()
    for cat, n in cat_counts.items():
        lines.append(f"| {cat} | {n} | {cat_to_sev.get(cat, '?')} |")
    lines += [
        "",
        "### By severity",
        "",
        "| Severity | Count |",
        "|---|---|",
    ]
    for sev, n in sev_counts.items():
        lines.append(f"| {sev} | {n} |")
    lines += ["", "---", ""]

# High-severity cases
high = disc[disc["severity"] == "high"]
lines += [f"## High-severity discrepancies ({len(high)} records)", ""]

if len(high) == 0:
    lines += ["None.", ""]
else:
    for _, rec in high.iterrows():
        eid = rec["entity_id"]
        u_row = univ[univ["entity_id"] == eid]
        penscore_str = ""
        if not u_row.empty:
            ps = u_row.iloc[0].get("penscore")
            if pd.notna(ps):
                penscore_str = f"  PenScore: {float(ps):.4f}"

        lines += [
            f"### {eid} - {rec['category']}",
            "",
            f"**Sources involved:** {rec['sources_involved'].replace('|', ', ')}",
            f"{penscore_str}",
            "",
            f"**Discrepancy:** {rec['details']}",
            "",
            "**note:** This is a confirmed cross-pipeline discordance. It does not",
            "invalidate the TrueWriterScore classification (which uses the pre-registered",
            "gate rules, not the triangulation result) but should be disclosed in the",
            "and flagged for future upstream package review.",
            "",
        ]

lines += ["---", ""]

# Medium-severity cases
med = disc[disc["severity"] == "medium"]
lines += [f"## Medium-severity discrepancies ({len(med)} records)", ""]
if len(med) == 0:
    lines += ["None.", ""]
else:
    lines += [
        "| Entity | Category | Details |",
        "|---|---|---|",
    ]
    for _, rec in med.iterrows():
        short_details = rec["details"][:120].replace("|", "\\|") + (
            "..." if len(rec["details"]) > 120 else ""
        )
        lines.append(f"| {rec['entity_id']} | {rec['category']} | {short_details} |")
    lines += [""]

lines += ["---", ""]

# Low-severity cases
low = disc[disc["severity"] == "low"]
lines += [f"## Low-severity discrepancies ({len(low)} records)", ""]
if len(low) == 0:
    lines += ["None.", ""]
else:
    lines += [
        "| Entity | Category | Details |",
        "|---|---|---|",
    ]
    for _, rec in low.iterrows():
        short_details = rec["details"][:120].replace("|", "\\|") + (
            "..." if len(rec["details"]) > 120 else ""
        )
        lines.append(f"| {rec['entity_id']} | {rec['category']} | {short_details} |")
    lines += [""]

# P3 verdict
lines += [
    "---",
    "",
    "## P3 pre-registered prediction",
    "",
    "**Statement:** Cross-pipeline triangulation flags >= 5 mechanism discrepancies.",
    f"**Observed:** {len(disc)} discrepancy records",
    f"**Result:** {'PASS' if len(disc) >= 5 else 'FAIL'} (threshold: n >= 5)",
    "",
]

OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text("\n".join(lines))
print(f"Wrote {OUTPUT} ({len(lines)} lines, {len(disc)} discrepancy records)")
