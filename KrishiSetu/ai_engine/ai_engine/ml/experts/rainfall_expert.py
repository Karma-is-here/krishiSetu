import joblib
import numpy as np
from ml.experts.base_expert import BaseExpert

class RainfallExpert(BaseExpert):
    def __init__(self, model_path="models/rainfall.pkl"):
        self.model = joblib.load(model_path)

    def predict(self, window: np.ndarray):
        """
        Predict rainfall-driven drought probability.
        """
        x = self.aggregate_window(window).reshape(1, -1)

        raw_prob = self.model.predict_proba(x)[0, 1]

        stress = self.normalize_score(raw_prob)
        confidence = self.compute_confidence(window)

        return stress, confidence
