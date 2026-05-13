Feature fusion utilities.

from typing import List, Dict, Any


def fuse_features(*feature_sets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Naive feature fusion by zipping dicts (mock)."""
    if not feature_sets:
        return []
    fused: List[Dict[str, Any]] = []
    for items in zip(*feature_sets):
        merged: Dict[str, Any] = {}
        for d in items:
            merged.update(d)
        fused.append(merged)
    return fused
