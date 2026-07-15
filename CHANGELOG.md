# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-05-26

### Added - Framework
- 5-gate TrueWriterScore certification framework v3.2 (`pen_compare/core/gates.py`, `certify.py`)
- Unified editor universe assembly: 1,058 entities (29 natural + 1,029 pen-assemble designs)
- Pre-registration YAMLs deposited at [OSF/4kdvy](https://osf.io/4kdvy)
- Full scorecard: 1 TRUE_WRITER, 4 PROBABLE_WRITER, 1,037 EMERGING_WRITER, 16 NOT_WRITER
- P1 PASS: ISCro4 (D2TGM5) is the sole TRUE_WRITER among natural editors
- P2 PASS: Zero computational designs are TRUE_WRITER

### Added - Sensitivity Analysis
- `pen_compare/core/sensitivity.py`: 18,000-combo threshold grid (15x15x16x5)
- ISCro4 robustness = 1.000 across all combinations; zero boundary cases
- 4 near-boundary editors: Bxb1, eePASSIGE, eePASSIGE_v2, phiC31

### Added - Triangulation
- `pen_compare/triangulation/triangulator.py`: 5 cross-pipeline discrepancy rules
- 30 discrepancy records across 29 natural editors; P3 PASS (threshold >= 5)
- Rule breakdown: SIZE_INCONSISTENCY (13), MECH_VS_PFAM (11), EVIDENCE_GAP (5), CARGO_INCONSISTENCY (1), AXIS_VS_TIER (0)

### Added - RAG LLM Q&A
- `pen_compare/rag/qa.py`: PenStackQA class (ChromaDB + sentence-transformers + Ollama)
- 77-chunk vector index from repo docs; llama3.1:8b-instruct-q4_K_M backend
- P4 PASS: 44/50 benchmark questions correct (88% accuracy, threshold >= 80%)


### Added - Tests, Docs, Release
- 139 unit tests across 9 test modules; 98.8% code coverage
- Sphinx documentation with API autodoc, framework description, and MODEL_CARD
- GitHub Pages deployment via `.github/workflows/docs.yml`
- PyPI release: `pip install pen-compare`; tag `v0.1.0`
- CI: ruff lint + pytest unit tests + codecov upload

## [Unreleased -> 0.1.0a1] - 2026-05-26 (scaffolding)

### Added
- Repository scaffolding: `pyproject.toml` with v3-compat upstream pins
- CLI skeleton: `pen-compare compare` and `pen-compare list-writers`
- CITATION.cff, CHANGELOG.md, LICENSE, MANIFEST.in
- Directory structure for the full pipeline
- CI workflow (`ci.yml`) and docs workflow (`docs.yml`)
