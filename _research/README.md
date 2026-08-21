# _research

This directory holds standalone research-only modules that came from the
upstream hermes-agent fork. They are **not** imported by the core runtime and
are not needed to start `hermes`.

- `batch_runner.py` — batch/scale-out experiment runner.
- `trajectory_compressor.py` — trajectory compression experiments.
- `toolset_distributions.py` — toolset distribution analysis.
- `mini_swe_runner.py` — minimal SWE-bench style runner.

> Note: these modules are still registered in the editable-install finder
> (`__editable___hermes_agent_0_20_4_finder.py`), so they were moved here
> rather than deleted to avoid a stale `sys.path` mapping. They can be removed
> at any time; nothing in the runtime imports them. If you remove them, you
> should also drop the corresponding entries from the editable finder and
> re-run `pip install -e .` to rebuild it.
