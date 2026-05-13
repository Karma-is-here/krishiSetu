IMD alert loader stub.

from typing import Any, Dict

def load_imd_alerts(region_id: str, start_date: str, end_date: str) -> Dict[str, Any]:
    """Return IMD weather alerts per tile between dates (mock)."""
    return {"alerts": [], "meta": {"region_id": region_id, "start_date": start_date, "end_date": end_date}}
