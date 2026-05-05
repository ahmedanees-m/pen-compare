# Cross-Pipeline Triangulation Report - TrueWriterScore v3.2

**Total discrepancy records:** 30

Discrepancies are flagged where claims from GENOME-ATLAS, MECH-CLASS, and
PEN-SCORE are internally inconsistent. These are *findings*, not errors -
they reflect the state of the art and are reported transparently.

No threshold adjustments or data corrections are made in response to these
findings (pre-registration policy).

---

## Summary

### By category

| Category | Count | Severity |
|---|---|---|
| SIZE_INCONSISTENCY | 13 | medium |
| MECH_VS_PFAM | 11 | high |
| EVIDENCE_GAP | 5 | low |
| CARGO_INCONSISTENCY | 1 | medium |

### By severity

| Severity | Count |
|---|---|
| medium | 14 |
| high | 11 |
| low | 5 |

---

## High-severity discrepancies (11 records)

### evoCAST - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.5206

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### CAST_VK - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.7239

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### IS621 - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.9473

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### Cre - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.7462

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### Bxb1 - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.7504

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### Lambda_Int - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.7534

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### phiC31 - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.7271

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### IscB - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.6990

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### CAST_IF - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.7370

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### eePASSIGE_v2 - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.7504

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

### IS621_2 - MECH_VS_PFAM

**Sources involved:** GENOME_ATLAS, MECH_CLASS
  PenScore: 0.9473

**Discrepancy:** tier_a_gate=True (mech-class: IS110 Tier-A) but atlas_system_present=False (genome-atlas has no entry). mech-class calls IS110 without supporting PFAM atlas record.

**note:** This is a confirmed cross-pipeline discordance. It does not
invalidate the TrueWriterScore classification (which uses the pre-registered
gate rules, not the triangulation result) but should be disclosed in the
and flagged for future upstream package review.

---

## Medium-severity discrepancies (14 records)

| Entity | Category | Details |
|---|---|---|
| SpCas9 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| Cas12a | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| Cas12f | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| SpuFz1_V4 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| enNlovFz2 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| evoCAST | CARGO_INCONSISTENCY | intrinsic_cargo_mechanism=True (metadata: native cargo delivery) but S_Cargo=0.500 < 0.60 (pen-score: limited cargo demo... |
| eePASSIGE | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| Tn5 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| PE2 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| PE5max | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| TwinPE | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| ABE7_10 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| BE3 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |
| ISCro4 | SIZE_INCONSISTENCY | atlas_system_present=True (genome-atlas has entry with UniProt record) but length_aa=None in unified universe (pen-score... |

---

## Low-severity discrepancies (5 records)

| Entity | Category | Details |
|---|---|---|
| CAST_VK | EVIDENCE_GAP | tier_a_gate=True AND S_DSB=1.000 (confirmed IS110 bridge recombinase) but cell_based_evidence=False. The Molecular Pen h... |
| IS621 | EVIDENCE_GAP | tier_a_gate=True AND S_DSB=1.000 (confirmed IS110 bridge recombinase) but cell_based_evidence=False. The Molecular Pen h... |
| Lambda_Int | EVIDENCE_GAP | tier_a_gate=True AND S_DSB=1.000 (confirmed IS110 bridge recombinase) but cell_based_evidence=False. The Molecular Pen h... |
| CAST_IF | EVIDENCE_GAP | tier_a_gate=True AND S_DSB=1.000 (confirmed IS110 bridge recombinase) but cell_based_evidence=False. The Molecular Pen h... |
| IS621_2 | EVIDENCE_GAP | tier_a_gate=True AND S_DSB=1.000 (confirmed IS110 bridge recombinase) but cell_based_evidence=False. The Molecular Pen h... |

---

## P3 pre-registered prediction

**Statement:** Cross-pipeline triangulation flags >= 5 mechanism discrepancies.
**Observed:** 30 discrepancy records
**Result:** PASS (threshold: n >= 5)
