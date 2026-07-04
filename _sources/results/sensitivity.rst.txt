Sensitivity Analysis
====================

Sensitivity analysis evaluated robustness of all tier assignments across an 18,000-combination
parameter grid (15x15x16x5 threshold variations).

Grid definition
---------------

.. list-table::
   :header-rows: 1

   * - Parameter
     - Range
     - N values
   * - G1 threshold (S_DSB)
     - 0.85-0.99 (step 0.01)
     - 15
   * - G2 threshold (S_Prog)
     - 0.85-0.99 (step 0.01)
     - 15
   * - G3 threshold (S_Cargo)
     - 0.80-0.95 (step 0.01)
     - 16
   * - G4 size max (aa)
     - 600, 750, 900, 1050, 1200
     - 5

Key findings
------------

* **ISCro4 robustness = 1.000** - TRUE_WRITER under all 18,000 combinations
* **Zero boundary cases** (robustness < 0.50) - no tier is genuinely ambiguous
* **4 near-boundary editors** (50-80% robustness): Bxb1 (0.5625), eePASSIGE (0.5625),
  eePASSIGE_v2 (0.5625), phiC31 (0.75)
* **1,055 / 1,058 entities** (99.7%): default tier == modal tier
