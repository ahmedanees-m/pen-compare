Quick Start
===========

Certify a single editor
-----------------------

.. code-block:: python

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
   print(result.tier)              # TRUE_WRITER
   print(result.qualifying_gates_passed)  # 4

CLI usage
---------

.. code-block:: bash

   pen-compare --version
   pen-compare compare ISCro4 IS621
   pen-compare list-writers

Run sensitivity analysis
------------------------

.. code-block:: python

   from pen_compare.core.sensitivity import run_sensitivity_parallel
   import pandas as pd

   universe = pd.read_parquet("data/unified_editor_universe.parquet")
   scorecard = pd.read_parquet("results/truewriter_scorecard_v3.2.parquet")
   sensitivity_df = run_sensitivity_parallel(universe, scorecard, n_jobs=24)
   print(sensitivity_df[sensitivity_df["entity_id"] == "ISCro4"][["robustness"]])

Triangulation
-------------

.. code-block:: python

   from pen_compare.triangulation import Triangulator

   tri = Triangulator()
   universe = pd.read_parquet("data/unified_editor_universe.parquet")
   discrepancies = tri.run_full(universe)
   print(discrepancies.groupby("category").size())
