Deterministic inference pipeline.

from typing import List, Dict, Any
from ..models.fusion_model import FusionModel
from .decision_vector import to_decision_vector


def run_inference(features: List[Dict[str, Any]], model_path: str | None = None) -> Dict[str, Any]:
    """Run deterministic inference and return scores and decisions."""
    model = FusionModel(model_path or "models/model_weights/fusion_v1.pkl")
    scores = model.predict(features)
    decisions = to_decision_vector(scores)
    return {"scores": scores, "decisions": decisions}
