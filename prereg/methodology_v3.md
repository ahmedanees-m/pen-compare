# PEN-COMPARE Pre-Registration Methodology (v3.2)

**Pre-registration date:** 2026-05-26
**Author:** Anees Ahmed Mahaboob Ali (VIT University, Vellore)
**Pairs with:** `pen_compare/config/gates_v3.yaml`, `prereg/predictions_v3.yaml`

---

## Hypothesis under test

**H1:** The 5-gate hierarchical TrueWriterScore framework as specified in
`pen_compare/config/gates_v3.yaml` will satisfy all 4 pre-registered predictions in
`prereg/predictions_v3.yaml`, with publication-ladder outcomes determined by
the number of passes.

---

## Upstream data sources (frozen at pre-registration)

| Source | Version | SHA | What PEN-COMPARE consumes |
|---|---|---|---|
| genome-atlas | v0.7.2 | (from PREFLIGHT_SHA_RECORD_v3.json) | Knowledge graph: PFAM evidence, system memberships, orthologs |
| mech-class | v0.5.4 | (from PREFLIGHT_SHA_RECORD_v3.json) | DSB classification per editor, Tier-A gate decisions, confidence |
| pen-score | v0.1.3 | (from PREFLIGHT_SHA_RECORD_v3.json) | 8-axis values per editor, PenScore composite, get_editor_metadata() booleans |
| pen-assemble | v0.5.2 | (from PREFLIGHT_SHA_RECORD_v3.json) | 1,029-design catalog with intrinsic_cargo + cell_based fields |

**Commitment:** No upstream changes after pre-registration. If a bug is
discovered in upstream packages, it is documented as a finding; the models
are NOT retrained or re-patched after lock.

---

## Analytical procedure (36 steps, 12 weeks)

1. **Steps 1-3:** Repository scaffolding; Docker container; cross-package smoke test.
2. **Steps 4-8:** Source-universe inventory; unified editor universe assembly; write pre-registration YAMLs; OSF deposit.
3. **Steps 9-13:** 5-gate functions implemented; TrueWriter classifier; full universe certified; P1 and P2 evaluated.
4. **Steps 14-16:** Sensitivity analysis: 20,480 threshold-combination grid x ~60 editors = 1.08M certifications; robustness fractions computed per editor.
5. **Steps 17-20:** Literature evidence cache built from PFAM, DOI, and mech-class outputs; triangulation runs; P3 evaluated.
6. **Steps 21-24:** Ollama local LLM set up; RAG index built from Papers 1-4 docs (~150 sources); 50-question benchmark curated and evaluated; P4 evaluated.
7. **Steps 31-33:** Test suite >= 85% coverage; Sphinx docs; GitHub Actions CI; PyPI release.
8. **Steps 34-36:** drafted (Bioinformatics Application Note); bioRxiv preprint; journal submission.

---

## What is pre-registered

- Gate thresholds and tier rules (`pen_compare/config/gates_v3.yaml`)
- 4 predictions with measurable outcomes (`prereg/predictions_v3.yaml`)
- This methodology document (`prereg/methodology_v3.md`)
- Upstream package versions (frozen at pre-registration)
- The unified editor universe (`data/unified_editor_universe.parquet`)

## What is NOT pre-registered

- LLM benchmark exact wording (only the 50-question count and the 80% accuracy threshold are pre-registered)
- Sphinx documentation organization
- Figure layout and captions

---

## Stopping rules

| Scenario | Rule |
|---|---|
| P1 fails (n !=  1 TRUE_WRITER) | Report actual count and identity; no threshold tuning |
| P2 fails (n_design_TRUE > 0) | Investigate pen-assemble v0.5.2 bug; file issue |
| P3 fails low (< 5 discrepancies) | Report as "ecosystem well-calibrated"; reframe contribution |
| P4 fails (< 80%) | Evaluate Phi-3.5 Mini and Llama 3.3 70B; report all 3 |
| <= 2/4 PASS | Halt and rework before submission |

---

## Statistical approach

**Sensitivity analysis** (not bootstrap) is the primary uncertainty quantification.
Bootstrap with arbitrary σ is inappropriate here because the inputs are not
stochastic - they are deterministic scores from upstream packages. Instead,
we vary each gate threshold over a systematic grid (20,480 combinations) and
report the **robustness fraction**: the proportion of grid points where an editor
receives the same tier as under default thresholds.

- robustness_fraction >= 0.80 -> "robust" classification
- robustness_fraction 0.50-0.80 -> "moderate robustness"
- robustness_fraction < 0.50 -> "boundary case" (informative finding, not an error)

No multiple-testing correction is applied to sensitivity analysis because it
is exploratory, not confirmatory.

---

## Compute realism

| Workload | Hardware | Estimated wall time |
|---|---|---|
| Universe assembly | VM (24 CPU, 64 GB RAM) | ~30 min |
| TrueWriterScore on ~60 editors | Single CPU | < 5 min |
| Sensitivity analysis (20,480 x ~60) | 24-CPU parallel via joblib | ~1 hour |
| Triangulation full universe | Single CPU | ~15 min |
| LLM RAG indexing (~150 sources) | CPU (sentence-transformers) | ~30 min |
| LLM benchmark (50 Q x 3 models) | VM GPU (Llama 3.1 8B via Ollama) | ~30 min |
| Total marginal compute cost | - | ~3 hours |

**Total marginal financial cost: $0.00.** All compute on VM (existing HPC
workstation) or free-tier cloud services. No paid APIs.
