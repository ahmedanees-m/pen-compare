TrueWriterScore Gates (v3.2)
============================

The certification framework applies five pre-registered gates from
``config/gates_v3.yaml``.

Gate 1 - DSB Avoidance (Necessary)
------------------------------------

* **Type:** Necessary - failing auto-classifies as NOT_WRITER regardless of other gates
* **Threshold:** S_DSB >= 0.95
* **Rationale:** Editors that make double-strand breaks (SpCas9, Cas12a) are categorically
  excluded from the Molecular Pen hypothesis

Gate 2 - Programmability (Qualifying)
----------------------------------------

* **Type:** Qualifying
* **Threshold:** S_Prog >= 0.95
* **Rationale:** RNA-programmable targeting is required; site-specific recombinases (Bxb1,
  phiC31) with fixed att sites fail this gate

Gate 3 - Native Cargo Capability (Qualifying)
-----------------------------------------------

* **Type:** Qualifying
* **Threshold:** S_Cargo >= 0.90 AND intrinsic_cargo_mechanism = True
* **Rationale:** Both a high cargo score AND a mechanistic flag for intrinsic (non-template)
  cargo delivery are required

Gate 4 - Deliverability (Qualifying)
--------------------------------------

* **Type:** Qualifying
* **Threshold:** length_aa <= 900 OR split_aav_eligible = True
* **Rationale:** AAV size limit; editors > 900 aa can still qualify if split-AAV packaging
  has been demonstrated

Gate 5 - Experimental Evidence (Qualifying)
---------------------------------------------

* **Type:** Qualifying
* **Threshold:** >= 2 of {biochemical, structural, computational, cell_based}
* **Rationale:** Minimum multi-source evidence required for qualifying status

Tier Ladder
-----------

.. code-block:: text

   G1 FAIL  ->  NOT_WRITER (auto-demote, final)

   G1 PASS  +  4 qualifying  +  cell_based  ->  TRUE_WRITER
   G1 PASS  +  4 qualifying  +  no cell_based  ->  PROBABLE_WRITER
   G1 PASS  +  3 qualifying  +  cell_based  ->  PROBABLE_WRITER
   G1 PASS  +  1-2 qualifying  ->  EMERGING_WRITER
   G1 PASS  +  0 qualifying  ->  NOT_WRITER
