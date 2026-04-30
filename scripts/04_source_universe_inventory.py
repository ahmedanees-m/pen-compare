#!/usr/bin/env python3
"""Inventory every editor referenced by Papers 1-4.

Run inside the Docker container:
    python /workspace/pen-compare/scripts/04_source_universe_inventory.py

Expected output:
    genome_atlas: ~28 systems
    pen_score: ~29 editors (with overlap with atlas)
    pen_assemble: 1029 designs
    Unified universe target: ~1060 entries (after deduplication)
"""

from pathlib import Path

import genome_atlas  # type: ignore
import pandas as pd
from pen_score import get_editor_metadata  # type: ignore
from pen_score.data.loader import load_editor_universe  # type: ignore

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

inventories: dict[str, pd.DataFrame] = {}

print("=" * 60)
print("STEP 4: SOURCE UNIVERSE INVENTORY")
print("=" * 60)

# 1. genome-atlas foundational_systems
print("\n[1/3] genome-atlas foundational_systems...")
atlas_systems = genome_atlas.load_systems()
rows_ga = []
for sid, s in atlas_systems.items():
    # SystemEntry may use .uniprot or .proteins (list)
    uniprot = getattr(s, "uniprot", None)
    if uniprot is None:
        proteins = getattr(s, "proteins", None) or []
        uniprot = proteins[0] if proteins else None

    rows_ga.append(
        {
            "id": sid,
            "source": "genome_atlas",
            "uniprot": uniprot,
            "organism": getattr(s, "organism", None),
            "length_aa": getattr(s, "length_aa", None),
            "mechanism_class": getattr(s, "mechanism_bucket", getattr(s, "mechanism_class", None)),
            "pfam": str(getattr(s, "pfam", [])),
        }
    )
inventories["genome_atlas"] = pd.DataFrame(rows_ga)
print(f"  genome_atlas: {len(inventories['genome_atlas'])} systems")

# 2. pen-score editor_universe
print("\n[2/3] pen-score editor_universe...")
pen_editors = load_editor_universe()  # returns list[EditorEntry]
rows_ps = []
for e in pen_editors:
    try:
        md = get_editor_metadata(e.id)
        canonical = md.canonical_name
        cell_based = md.cell_based_evidence
        intrinsic = md.intrinsic_cargo_mechanism
    except Exception:
        canonical = e.id
        cell_based = None
        intrinsic = None

    rows_ps.append(
        {
            "id": e.id,
            "source": "pen_score",
            "canonical_name": canonical,
            "uniprot": e.canonical_accession,
            "organism": e.organism,
            "length_aa": None,  # not in EditorEntry schema
            "intrinsic_cargo_mechanism": intrinsic,
            "cell_based_evidence": cell_based,
        }
    )
inventories["pen_score"] = pd.DataFrame(rows_ps)
print(f"  pen_score: {len(inventories['pen_score'])} editors")

# 3. pen-assemble v0.5.2 catalog
print("\n[3/3] pen-assemble v0.5.2 catalog...")
catalog_candidates = [
    # VM layout: pen-assemble repo is at ~/pen-assemble/
    Path.home() / "pen-assemble/data/catalog_v0.5.2_current.parquet",
    # Docker volume mount (mount ~/pen-assemble as /workspace/pen-assemble)
    Path("/workspace/pen-assemble/data/catalog_v0.5.2_current.parquet"),
    # Legacy/fallback paths
    Path.home() / "repos/pen-assemble/data/catalog_v0.5.2_current.parquet",
]
catalog = None
for p in catalog_candidates:
    if p.exists():
        catalog = pd.read_parquet(p)
        print(f"  Loaded from: {p}")
        break

if catalog is None:
    print("  WARNING: catalog not found -- creating empty placeholder")
    catalog = pd.DataFrame(
        columns=[
            "design_id",
            "parent_editor",
            "strategy",
            "length_aa",
            "intrinsic_cargo_mechanism",
            "cell_based_evidence",
            "penscore_v012",
        ]
    )

design_cols = [
    "design_id",
    "parent_editor",
    "strategy",
    "length_aa",
    "intrinsic_cargo_mechanism",
    "cell_based_evidence",
]
available = [c for c in design_cols if c in catalog.columns]
inv_pa = catalog[available].copy() if available else catalog.copy()
inv_pa["id"] = catalog["design_id"] if "design_id" in catalog.columns else range(len(catalog))
inv_pa["source"] = "pen_assemble"
inventories["pen_assemble"] = inv_pa
print(f"  pen_assemble: {len(inventories['pen_assemble'])} designs")

# Save per-source inventories
print("\nSaving per-source inventories...")
for src, df in inventories.items():
    out = DATA_DIR / f"source_inventory_{src}.parquet"
    df.to_parquet(out, index=False)
    print(f"  Saved {out.name} ({len(df)} rows)")

# Deduplication preview
print("\n=== Deduplication preview ===")
all_uniprots = []
for src, df in inventories.items():
    if "uniprot" in df.columns:
        all_uniprots.extend(df["uniprot"].dropna().unique().tolist())

unique_uniprots = set(all_uniprots)
n_designs = len(inventories.get("pen_assemble", pd.DataFrame()))
total = sum(len(df) for df in inventories.values())

print(f"  Total raw rows: {total}")
print(f"  Unique UniProt accessions across sources: {len(unique_uniprots)}")
print(f"  Computational designs (no UniProt): {n_designs}")
print(f"  Expected unified universe size: ~{len(unique_uniprots) + n_designs}")

print("\n[OK] Step 4 COMPLETE -- Run Step 5 to assemble unified universe")
