Baseline model stub.

from typing import List, Dict, Any


class BaselineModel:
    """Simple baseline model stub."""

    def predict(self, features: List[Dict[str, Any]]) -> List[float]:
        return [0.5 for _ in features]
