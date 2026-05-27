# PEN-COMPARE

<p align="center">
  <strong>Programmable Editor Nominee - Comparative Outcome Metrics via Pre-registration and Axis-based Ranking Evaluation</strong>
</p>

<p align="center">
  <a href="https://github.com/ahmedanees-m/pen-compare/actions"><img src="https://github.com/ahmedanees-m/pen-compare/workflows/CI/badge.svg" alt="CI"></a>
  <a href="https://github.com/ahmedanees-m/pen-compare/releases"><img src="https://img.shields.io/github/v/release/ahmedanees-m/pen-compare?label=version" alt="Version"></a>
  <a href="https://pypi.org/project/pen-compare/"><img src="https://img.shields.io/pypi/pyversions/pen-compare.svg" alt="Python versions"></a>
  <a href="https://codecov.io/gh/ahmedanees-m/pen-compare"><img src="https://codecov.io/gh/ahmedanees-m/pen-compare/branch/main/graph/badge.svg" alt="Coverage"></a>
  <a href="https://ahmedanees-m.github.io/pen-compare"><img src="https://img.shields.io/badge/docs-GitHub%20Pages-blue" alt="Docs"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://osf.io/4kdvy"><img src="https://img.shields.io/badge/Pre--registration-OSF%204kdvy-lightblue" alt="OSF"></a>
  <a href="https://github.com/ahmedanees-m/genome-atlas"><img src="https://img.shields.io/badge/genome--atlas-v0.7.2-8A2BE2" alt="genome-atlas"></a>
  <a href="https://github.com/ahmedanees-m/mech-class"><img src="https://img.shields.io/badge/mech--class-v0.5.4-8A2BE2" alt="mech-class"></a>
  <a href="https://github.com/ahmedanees-m/pen-score"><img src="https://img.shields.io/badge/pen--score-v0.1.3-8A2BE2" alt="pen-score"></a>
  <a href="https://github.com/ahmedanees-m/pen-assemble"><img src="https://img.shields.io/badge/pen--assemble-v0.5.2-8A2BE2" alt="pen-assemble"></a>
</p>

---

**PEN-COMPARE** is the capstone of [PEN-STACK](https://github.com/ahmedanees-m/genome-atlas) - a five computational infrastructure for programmable genome integration design. It answers the defining question of the framework:

> *Which genome editors are genuine "Molecular Pens" - writers that insert DNA without cutting it - and how robustly can we certify that distinction?*

PEN-COMPARE integrates all four upstream PEN-STACK datasets into a **5-gate hierarchical certification system** (TrueWriterScore v3.2), evaluates 1,058 editors and designs, and delivers its conclusions through a local-LLM RAG Q&A layer. All four pre-registered predictions passed validation.

---

## The PEN-STACK Pipeline

PEN-COMPARE sits at the end of the PEN-STACK evidence chain. Each upstream package provides critical inputs:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PEN-STACK  (Papers 1-5)                      │
│                                                                     │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐            │
│  │ GENOME-ATLAS │   │  MECH-CLASS  │   │  PEN-SCORE   │            │
│  │   │   │   │   │   │            │
│  │              │   │              │   │              │            │
│  │ Knowledge    │   │ Mechanism    │   │ 8-axis multi-│            │
│  │ graph of 28  │   │ classifier:  │   │ criteria     │            │
│  │ editing sys- │   │ IS110 bridge │   │ scoring of   │            │
│  │ tems + PFAM  │   │ vs nuclease  │   │ 29 natural   │            │
│  │ domain atlas │   │ vs transpo-  │   │ editors      │            │
│  │              │   │ sase (F1=    │   │ (S_DSB,      │            │
│  │ → 28 curated │   │ 0.9862)      │   │ S_Prog, etc) │            │
│  │   systems    │   │              │   │              │            │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘            │
│         │                  │                  │                     │
│         └──────────────────┴──────────────────┘                    │
│                            │                                        │
│                    ┌───────▼────────┐                               │
│                    │  PEN-ASSEMBLE  │                               │
│                    │    │                               │
│                    │                │                               │
│                    │ 1,029 IS110    │                               │
│                    │ designs across │                               │
│                    │ 4 strategies   │                               │
│                    │ (deimmunized,  │                               │
│                    │ ortholog, etc) │                               │
│                    └───────┬────────┘                               │
│                            │                                        │
│          ┌─────────────────▼──────────────────────┐                │
│          │              PEN-COMPARE                │                │
│          │                 │                │
│          │                                         │                │
│          │  Unified Universe: 1,058 entities       │                │
│          │  (29 natural + 1,029 designs)           │                │
│          │                                         │                │
│          │  ┌─────────────────────────────────┐   │                │
│          │  │   5-Gate TrueWriterScore v3.2   │   │                │
│          │  │  G1 DSB Avoidance  (Necessary)  │   │                │
│          │  │  G2 Programmability             │   │                │
│          │  │  G3 Native Cargo                │   │                │
│          │  │  G4 Deliverability              │   │                │
│          │  │  G5 Experimental Evidence       │   │                │
│          │  └──────────────┬──────────────────┘   │                │
│          │                 │                       │                │
│          │    ┌────────────┴──────────────┐        │                │
│          │    ▼                           ▼        │                │
│          │  Sensitivity Analysis    Cross-Pipeline │                │
│          │  18,000 combos/entity    Triangulation  │                │
│          │  ISCro4 robustness=1.0   30 discrepancies│               │
│          │    ┌────────────┴──────────────┘        │                │
│          │    ▼                                    │                │
│          │  RAG LLM Q&A (88% accuracy)             │                │
│          └─────────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Key Results

| Metric | Value |
|---|---|
| Universe size | 1,058 entities (29 natural + 1,029 designs) |
| **TRUE_WRITER** | **1** - ISCro4 (IS110 bridge recombinase, D2TGM5) |
| PROBABLE_WRITER | 4 (IS621, Bxb1, phiC31, eePASSIGE_v2) |
| EMERGING_WRITER | 1,037 |
| NOT_WRITER | 16 |
| ISCro4 robustness | **1.000** across 18,000 threshold combinations |
| LLM RAG accuracy | **88%** (44/50 questions, llama3.1:8b) |
| Pre-registered predictions | **5 / 5 PASS** |

---

## What Makes an Editor a "Molecular Pen"?

Genome editors fall into two fundamental categories:

- **Molecular Scissors** (Cas9, Cas12a, meganucleases) - make double-strand DNA breaks, relying on the cell's error-prone repair machinery. Efficient but imprecise and immunogenic.
- **Molecular Pens** (IS110 bridge recombinases) - insert large DNA payloads at specific sites *without* cutting both strands. No DSBs means lower mutagenesis risk and reduced immune activation.

PEN-COMPARE's 5-gate framework formalises this distinction with pre-registered, threshold-locked criteria applied to a universe of 1,058 entities (all known IS110-family editors + 1,029 computationally designed variants).

---

## 5-Gate TrueWriterScore Framework (v3.2)

Certification flows through one **necessary** gate and four **qualifying** gates. Failing the necessary gate immediately assigns NOT_WRITER regardless of all other gates.

| Gate | Type | Criterion | Threshold |
|------|------|-----------|-----------|
| **G1 - DSB Avoidance** | **Necessary** | S_DSB axis (pen-score) | >= 0.95 |
| **G2 - Programmability** | Qualifying | S_Prog axis (pen-score) | >= 0.95 |
| **G3 - Native Cargo** | Qualifying | S_Cargo AND intrinsic_cargo_mechanism | >= 0.85 AND True |
| **G4 - Deliverability** | Qualifying | Protein length (pen-score) | <= 900 aa OR split-AAV |
| **G5 - Evidence** | Qualifying | Multi-source experimental support | >= 2 sources |

### Tier Ladder

```
  G1 FAILS  ──────────────────────────────────────────►  NOT_WRITER
                                                         (auto-demote)
  G1 PASSES
      │
      ├── 4/4 qualifying + cell-based evidence  ────────►  TRUE_WRITER
      │
      ├── 4/4 qualifying, no cell-based  ─────────────►  PROBABLE_WRITER
      ├── 3/4 qualifying + cell-based  ──────────────►  PROBABLE_WRITER
      │
      ├── 1-2/4 qualifying  ───────────────────────►  EMERGING_WRITER
      │
      └── 0/4 qualifying  ────────────────────────►  NOT_WRITER
```

All thresholds were SHA-256 locked before analysis in `SHA256_LOCK_v3.json` and deposited at [OSF/4kdvy](https://osf.io/4kdvy).

---

## Pre-Registration Outcomes

All four predictions were registered at [OSF/4kdvy](https://osf.io/4kdvy) on 2026-05-26, prior to any data analysis.

| ID | Pre-registered Statement | Result |
|----|--------------------------|--------|
| **P1** | Among natural editors, exactly 1 will be TRUE_WRITER (ISCro4) | **PASS** |
| **P2** | Zero pen-assemble designs will be TRUE_WRITER | **PASS** |
| **P3** | Cross-pipeline triangulation flags >= 5 mechanism discrepancies | **PASS** (30 found) |
| **P4** | Local-LLM RAG correctly answers >= 80% of 50-question benchmark | **PASS** (88%) |


---

## Upstream Packages

PEN-COMPARE depends on all four prior PEN-STACK papers. Each is independently installable and documented:

| Package | PyPI | GitHub | Role in PEN-COMPARE |
|---------|------|--------|---------------------|
| [**GENOME-ATLAS**](https://github.com/ahmedanees-m/genome-atlas) | `pip install genome-atlas` | [ahmedanees-m/genome-atlas](https://github.com/ahmedanees-m/genome-atlas) | Provides `atlas_system_present` PFAM evidence flag for Gate 5 and SIZE_INCONSISTENCY triangulation |
| [**MECH-CLASS**](https://github.com/ahmedanees-m/mech-class) | `pip install mech-class` | [ahmedanees-m/mech-class](https://github.com/ahmedanees-m/mech-class) | Provides `tier_a_gate` (IS110 Tier-A classification) used in Gate 1 interpretation and AXIS_VS_TIER + MECH_VS_PFAM triangulation rules |
| [**PEN-SCORE**](https://github.com/ahmedanees-m/pen-score) | `pip install pen-score` | [ahmedanees-m/pen-score](https://github.com/ahmedanees-m/pen-score) | Provides all 8 axis scores (S_DSB, S_Prog, S_Cargo ...) for Gates 1-3, `get_editor_metadata()` for cell-based evidence and intrinsic cargo flags |
| [**PEN-ASSEMBLE**](https://github.com/ahmedanees-m/pen-assemble) | `pip install pen-assemble` | [ahmedanees-m/pen-assemble](https://github.com/ahmedanees-m/pen-assemble) | Contributes 1,029 computational IS110 designs to the unified universe; catalog inherits cargo/cell-based flags from pen-score |

### Cross-Pipeline Triangulation - What Was Found

By comparing claims across all four packages, PEN-COMPARE identified 30 discrepancy records across 29 natural editors:

| Category | Severity | Count | Meaning |
|---|---|---|---|
| SIZE_INCONSISTENCY | Medium | 13 | Atlas entry exists but sequence length is unknown in pen-score |
| MECH_VS_PFAM | High | 11 | Atlas confirms DSB-free PFAM domains, but mech-class does not call IS110 Tier-A |
| EVIDENCE_GAP | Low | 5 | IS110 confirmed, S_DSB >= 0.95, but no mammalian cell-based evidence yet |
| CARGO_INCONSISTENCY | Medium | 1 | `intrinsic_cargo=True` but S_Cargo < 0.60 (evoCAST) |
| AXIS_VS_TIER | High | 0 | No editors found where pen-score and mech-class flatly contradict each other |

---

## Sensitivity Analysis

To quantify how robust the tier assignments are to threshold choices, every entity was re-certified across **18,000 parameter combinations** (15 x 15 x 16 x 5 grid):

| Parameter | Range | Values |
|-----------|-------|--------|
| G1 threshold | 0.85 - 0.99 | 15 |
| G2 threshold | 0.85 - 0.99 | 15 |
| G3 threshold | 0.80 - 0.95 | 16 |
| G4 size max | 600, 750, 900, 1050, 1200 aa | 5 |

**Findings:** ISCro4 is **TRUE_WRITER in 100% of combinations** (robustness = 1.000). Zero entities were boundary cases (robustness < 50%). Only four near-boundary editors (50-80%): Bxb1, eePASSIGE, eePASSIGE_v2, phiC31 - all site-specific recombinases that pass G2 only under loose thresholds.

---

## Installation

```bash
# Minimal (certification core only)
pip install pen-compare

# With local LLM RAG Q&A
pip install "pen-compare[rag]"

# Full (all extras)
pip install "pen-compare[rag,literature]"
```

**Requires Python >= 3.10.** All four upstream PEN-STACK packages are installed automatically.

### Docker (recommended for full pipeline)

```bash
docker run --rm \
  -v ~/pen-assemble:/workspace/pen-assemble \
  -p 8501:8501 \
  pen-stack/compare:0.1.0
```

The Docker image bundles Ollama (llama3.1:8b + phi3.5:3.8b) and a pre-built ChromaDB vector index.

---

## Quick Start

### Certify a single editor

```python
from pen_compare.core.certify import certify

result = certify(
    editor_id="ISCro4",
    s_dsb=1.0,
    s_prog=1.0,
    s_cargo=0.95,
    length_aa=326,
    evidence_sources=["biochemical", "structural", "computational", "cell_based"],
    intrinsic_cargo_mechanism=True,
)

print(result.tier)                    # TRUE_WRITER
print(result.qualifying_gates_passed) # 4
print(result.has_cell_based_evidence) # True
```

### CLI

```bash
pen-compare --version
pen-compare compare ISCro4 IS621
pen-compare list-writers
```

### Triangulate an editor

```python
import pandas as pd
from pen_compare.triangulation import Triangulator

universe = pd.read_parquet("data/unified_editor_universe.parquet")
tri = Triangulator()
discrepancies = tri.run_full(universe)
print(discrepancies.groupby("category").size())
```

### Ask the RAG system

```python
from pen_compare.rag import PenStackQA

qa = PenStackQA()
print(qa.ask("Why is ISCro4 a TRUE_WRITER?"))
```

---

## Repository Structure

```
pen-compare/
├── pen_compare/
│   ├── core/
│   │   ├── gates.py          # 5 gate functions (G1-G5), threshold-locked
│   │   ├── certify.py        # TrueWriterResult classifier
│   │   ├── sensitivity.py    # 18,000-combo sensitivity grid
│   │   └── universe.py       # Unified editor universe assembly
│   ├── triangulation/
│   │   └── triangulator.py   # 5 cross-pipeline discrepancy rules
│   ├── rag/
│   │   └── qa.py             # PenStackQA: ChromaDB + Ollama RAG pipeline
│   ├── server/
│   │   └── cache.py          # JSON cache builder for Cloud deployment
│   └── cli.py                # `pen-compare` CLI entry point
├── config/
│   ├── gates_v3.yaml         # Pre-registered gate thresholds (SHA-256 locked)
│   └── triangulation_rules_v3.yaml
├── prereg/
│   ├── predictions_v3.yaml   # 4 pre-registered predictions
│   ├── methodology_v3.md     # Analysis methodology
│   └── OSF_RECORD.txt        # OSF deposit confirmation
├── results/
│   ├── truewriter_scorecard_v3.2.parquet
│   ├── triangulation_discrepancies.parquet
│   ├── pred_P{1..5}.json     # Per-prediction outcomes
│   └── PREREG_OUTCOME.json   # 4/4 PASS summary
├── data/
│   ├── unified_editor_universe.parquet
├── tests/
│   ├── unit/                 # 155 tests, 98.8% coverage
│   └── integration/          # Calibration anchors + smoke tests (require Docker)
├── docs/                     # Sphinx source → https://ahmedanees-m.github.io/pen-compare
├── scripts/                  # Numbered execution scripts
├── .github/workflows/
│   ├── ci.yml                # Lint + unit tests + PyPI release
│   └── docs.yml              # Sphinx → GitHub Pages
├── SHA256_LOCK_v3.json       # Pre-registration integrity record
└── pyproject.toml
```

---

## Development

```bash
git clone https://github.com/ahmedanees-m/pen-compare.git
cd pen-compare
pip install -e ".[dev]"
pytest tests/unit/ -q
```

Coverage report:

```bash
pytest tests/unit/ --cov=pen_compare --cov-report=term-missing
```

Docs (local preview):

```bash
pip install -e ".[docs]"
sphinx-build -b html docs docs/_build/html
open docs/_build/html/index.html
```

---

## Verified Biological Anchors

All key biological identifiers were independently verified on 2026-05-26:

| Entity | UniProt | Organism | Length | Status |
|--------|---------|----------|--------|--------|
| ISCro4 | D2TGM5 | *C. rodentium* ICC168 | 326 aa | Confirmed TRUE_WRITER |
| IS621 | A0A2X3M8B0 | *E. coli* NCTC8009/8333 | 342 aa | Confirmed PROBABLE_WRITER |
| SpCas9 | Q99ZW2 | *S. pyogenes* serotype M1 | 1368 aa | Confirmed NOT_WRITER |

| Paper | DOI | Status |
|-------|-----|--------|
| Durrant 2024 *Nature* | [10.1038/s41586-024-07552-4](https://doi.org/10.1038/s41586-024-07552-4) | Confirmed |
| Hiraizumi 2024 *Nature* | [10.1038/s41586-024-07570-2](https://doi.org/10.1038/s41586-024-07570-2) | Confirmed |
| Pelea 2026 *Science* | [10.1126/science.adz1884](https://doi.org/10.1126/science.adz1884) | Confirmed |
| Perry 2025 *Science* | [10.1126/science.adz0276](https://doi.org/10.1126/science.adz0276) | Confirmed |

---

## Reproducibility

| Artefact | Location |
|----------|----------|
| Pre-registration | [OSF/4kdvy](https://osf.io/4kdvy) (public 2026-05-26) |
| SHA-256 lock | `SHA256_LOCK_v3.json` |
| Pre-reg tag | [`prereg-v3.2`](https://github.com/ahmedanees-m/pen-compare/releases/tag/prereg-v3.2) |
| v0.1.0 release | [`v0.1.0`](https://github.com/ahmedanees-m/pen-compare/releases/tag/v0.1.0) |
| Sensitivity grid | `pen_compare/core/sensitivity.py` (SENSITIVITY_GRID constant) |
| Biological ID verification | `memory/project_pen_compare.md` (session log) |

All thresholds in `config/gates_v3.yaml` are SHA-256 locked prior to data analysis. Scores are computed using frozen upstream package versions (`pen-score==0.1.3`, `pen-assemble==0.5.2`, `genome-atlas==0.7.2`, `mech-class==0.5.4`).

---

## Citation

```bibtex
@software{pen_compare_2026,
  author    = {Mahaboob Ali, Anees Ahmed},
  title     = {{PEN-COMPARE}: Hierarchical Certification Framework for
               Non-Destructive Genome Editors},
  version   = {0.1.0},
  year      = {2026},
  url       = {https://github.com/ahmedanees-m/pen-compare},
  note      = {Pre-registration: \url{https://osf.io/4kdvy}}
}
```

If PEN-COMPARE's results depend on an upstream package, please also cite it:

- **GENOME-ATLAS** → [github.com/ahmedanees-m/genome-atlas](https://github.com/ahmedanees-m/genome-atlas)
- **MECH-CLASS** → [github.com/ahmedanees-m/mech-class](https://github.com/ahmedanees-m/mech-class)
- **PEN-SCORE** → [github.com/ahmedanees-m/pen-score](https://github.com/ahmedanees-m/pen-score)
- **PEN-ASSEMBLE** → [github.com/ahmedanees-m/pen-assemble](https://github.com/ahmedanees-m/pen-assemble)

---

## License

MIT - see [LICENSE](LICENSE).

---

<p align="center">
  <a href="https://github.com/ahmedanees-m/genome-atlas">GENOME-ATLAS</a> ·
  <a href="https://github.com/ahmedanees-m/mech-class">MECH-CLASS</a> ·
  <a href="https://github.com/ahmedanees-m/pen-score">PEN-SCORE</a> ·
  <a href="https://github.com/ahmedanees-m/pen-assemble">PEN-ASSEMBLE</a> ·
  <strong>PEN-COMPARE</strong>
</p>
