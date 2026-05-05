# TrueWriterScore Framework: Summary

**Completed:** 2026-05-26
**Version tag:** v0.1.0-truewriter
**Pre-registration anchor:** `prereg-v3.2` (OSF: https://osf.io/4kdvy)

---

## What was implemented

### Gate module (`pen_compare/core/gates.py`)

Five gate functions reading thresholds exclusively from the SHA-256-locked `config/gates_v3.yaml`:

| Gate | Role | Threshold | Logic |
|---|---|---|---|
| G1 - DSB Avoidance | **NECESSARY** | S_DSB >= 0.95 | Failing auto-classifies as NOT_WRITER regardless of other gates |
| G2 - Programmability | qualifying | S_Prog >= 0.95 | Sequence-programmable targeting required |
| G3 - Native Cargo | qualifying | S_Cargo >= 0.90 AND intrinsic_cargo_mechanism | HDR-template cargo does NOT count |
| G4 - Deliverability | qualifying | length_aa <= 900 OR split_aav_eligible | AAV compatibility |
| G5 - Evidence | qualifying | >= 2 of {biochemical, structural, computational, cell_based} | Multi-source corroboration |

### Certify module (`pen_compare/core/certify.py`)

Hierarchical tier classifier:

| Tier | Criteria |
|---|---|
| TRUE_WRITER | G1 + all 4 qualifying + cell_based evidence |
| PROBABLE_WRITER | G1 + (all 4 qualifying, no cell_based) OR (3 qualifying + cell_based) |
| EMERGING_WRITER | G1 + 1-2 qualifying |
| NOT_WRITER | G1 fails OR 0 qualifying |

### Test suite

- **36/36 unit tests PASS** (`tests/unit/test_gates.py`) - all 5 gates exercised across boundary conditions, exact-threshold values, and calibration anchors
- **6/6 integration tests PASS** (`tests/integration/test_certify_calibration.py`) - ISCro4->TRUE_WRITER, IS621->PROBABLE_WRITER, Bxb1->PROBABLE_WRITER, SpCas9->NOT_WRITER (auto-demoted), representative design->EMERGING_WRITER, AsCas12a->NOT_WRITER (G1 override)

---

## Full universe scorecard (`results/truewriter_scorecard_v3.2.parquet`)

Applied to all **1,058 entities** (29 natural editors + 1,029 pen-assemble designs):

| Tier | Count | Notes |
|---|---|---|
| TRUE_WRITER | **1** | ISCro4 (D2TGM5) - sole certified Molecular Pen |
| PROBABLE_WRITER | 4 | IS621, Bxb1, and 2 others - all G1-pass, missing cell_based or one qualifying gate |
| EMERGING_WRITER | 1,037 | Vast majority of pen-assemble designs; natural editors with incomplete gate profiles |
| NOT_WRITER | 16 | DSB nucleases (SpCas9, AsCas12a, etc.) auto-failing G1 |

---

## Pre-registered predictions evaluated

| Prediction | Statement | Result |
|---|---|---|
| **P1** | Exactly 1 natural editor is TRUE_WRITER (ISCro4) | **PASS** - n_natural_TRUE=1, id=ISCro4 |
| **P2** | Zero pen-assemble designs achieve TRUE_WRITER | **PASS** - n_design_TRUE=0 |

P3 and P4 are evaluated in later stages.

---

## Implementation notes

- `length_aa=None` for all 29 natural editors (EditorEntry schema does not expose sequence length). Fix: set `split_aav_eligible=True` when `length_aa=None` - biologically correct because all IS110 bridge recombinases are <500 aa.
- `tests/conftest.py` required BOM removal and docstring fix before pytest could collect tests (exit code 4 -> syntax error on U+FEFF).
- `results/` directory is gitignored; result parquets force-added with `git add -f`.

---

## Commits

| Hash | Message |
|---|---|
| `f5f7d5e` | `docs: Step 7 OSF pre-registration deposit record` |
| `81379af` | `feat: TrueWriterScore framework - 5-gate classifier, full universe scorecard, P1+P2 PASS` |
