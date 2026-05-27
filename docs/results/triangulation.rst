Triangulation Report
====================

Triangulation cross-referenced the four PEN-STACK pipelines to identify mechanism
discrepancies in the natural editor universe.

Summary (30 discrepancy records, 29 natural editors)
-----------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Category
     - Severity
     - Count
     - Description
   * - SIZE_INCONSISTENCY
     - Medium
     - 13
     - Atlas entry present but length_aa=None in pen-score
   * - MECH_VS_PFAM
     - High
     - 11
     - Atlas + high S_DSB but tier_a_gate=False (site-specific recombinases)
   * - EVIDENCE_GAP
     - Low
     - 5
     - IS110 confirmed, S_DSB >= 0.95, but cell_based=False
   * - CARGO_INCONSISTENCY
     - Medium
     - 1
     - intrinsic_cargo=True but S_Cargo < 0.60 (evoCAST)
   * - AXIS_VS_TIER
     - High
     - 0
     - No editors with tier_a_gate=False and S_DSB < 0.80 in IS110 direction

P3 outcome
----------

**P3 PASS:** 30 discrepancy records across 29 natural editors (threshold: >= 5).
Zero discrepancies in the 1,029 computational designs (by construction - designs
inherit evidence flags from pen-assemble catalog).
