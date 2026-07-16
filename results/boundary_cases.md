# Boundary Case Investigation - TrueWriterScore v3.2

**Boundary (robustness < 0.50):** fewer than half of the 20,480 threshold
combinations agree on the modal tier - tier assignment is genuinely ambiguous.

**Near-boundary (robustness 50-80%):** majority agree on modal tier but a
substantial fraction flip - threshold-sensitive findings worth reporting.

**Boundary cases (<0.50):** 0
**Near-boundary (50-80%):** 4

These cases are transparently reported in the Discussion.
No threshold tuning is performed in response to these findings.

---

## Section A: Zero true boundary cases (robustness < 0.50)

All 1,058 entities have robustness >= 0.50. The 5-gate hierarchical framework
is stable: no entity's tier is genuinely ambiguous under the pre-registered
threshold ranges. This is a reportable positive finding.

---

## Section B: Near-boundary cases (robustness 50-80%)

These entities have a majority of threshold combinations agreeing on the modal tier,
but a substantial minority flips the tier. Reported transparently; no action taken.

### Bxb1 (source: natural)

- **Default tier:** EMERGING_WRITER
- **Modal tier:** PROBABLE_WRITER
- **Robustness:** 0.562 (11520/20,480 combos)
- **Tier distribution:** EMERGING_WRITER=8960, PROBABLE_WRITER=11520

**Key axis values:**
- S_Cargo = 0.883
- intrinsic_cargo = True
- cell_based = True

**Interpretation:** At G3 threshold <= observed S_Cargo value, G3 passes and
qualifying count rises, potentially reaching PROBABLE_WRITER with cell_based evidence.
Default threshold (0.90) places this editor just at the EMERGING/PROBABLE boundary.

### eePASSIGE (source: natural)

- **Default tier:** EMERGING_WRITER
- **Modal tier:** PROBABLE_WRITER
- **Robustness:** 0.562 (11520/20,480 combos)
- **Tier distribution:** EMERGING_WRITER=8960, PROBABLE_WRITER=11520

**Key axis values:**
- S_Cargo = 0.883
- intrinsic_cargo = True
- cell_based = True

**Interpretation:** At G3 threshold <= observed S_Cargo value, G3 passes and
qualifying count rises, potentially reaching PROBABLE_WRITER with cell_based evidence.
Default threshold (0.90) places this editor just at the EMERGING/PROBABLE boundary.

### eePASSIGE_v2 (source: natural)

- **Default tier:** EMERGING_WRITER
- **Modal tier:** PROBABLE_WRITER
- **Robustness:** 0.562 (11520/20,480 combos)
- **Tier distribution:** EMERGING_WRITER=8960, PROBABLE_WRITER=11520

**Key axis values:**
- S_Cargo = 0.883
- intrinsic_cargo = True
- cell_based = True

**Interpretation:** At G3 threshold <= observed S_Cargo value, G3 passes and
qualifying count rises, potentially reaching PROBABLE_WRITER with cell_based evidence.
Default threshold (0.90) places this editor just at the EMERGING/PROBABLE boundary.

### phiC31 (source: natural)

- **Default tier:** EMERGING_WRITER
- **Modal tier:** EMERGING_WRITER
- **Robustness:** 0.750 (15360/20,480 combos)
- **Tier distribution:** EMERGING_WRITER=15360, PROBABLE_WRITER=5120

**Key axis values:**
- S_Cargo = 0.833
- intrinsic_cargo = True
- cell_based = True

**Interpretation:** At G3 threshold <= observed S_Cargo value, G3 passes and
qualifying count rises, potentially reaching PROBABLE_WRITER with cell_based evidence.
Default threshold (0.90) places this editor just at the EMERGING/PROBABLE boundary.
