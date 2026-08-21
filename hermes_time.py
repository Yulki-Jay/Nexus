"""Backward-compatible imports for Hermes timezone helpers.

The canonical implementation lives in :mod:`hermes_core.time`.
"""

from hermes_core.time import get_timezone, now, reset_cache

__all__ = ["get_timezone", "reset_cache", "now"]
