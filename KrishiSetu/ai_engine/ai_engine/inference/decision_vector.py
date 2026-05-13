Decision vector utilities.

from typing import List


def to_decision_vector(scores: List[float], threshold: float = 0.5) -> List[int]:
    """Convert scores to binary decisions using a threshold."""
    return [int(s >= threshold) for s in scores]
