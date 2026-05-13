Pipeline-level validation checks.

from typing import Dict, Any


def validate_pipeline_output(output: Dict[str, Any]) -> bool:
    """Minimal sanity checks on pipeline output."""
    return all(k in output for k in ("region_id", "start_date", "end_date"))
