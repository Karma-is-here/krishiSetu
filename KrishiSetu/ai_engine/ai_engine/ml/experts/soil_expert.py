import joblib
import numpy as np
from ml.experts.base_expert import BaseExpert

class SoilExpert(BaseExpert):
    def __init__(self, model_path="models/soil.pkl"):
        self.model = joblib.load(model_path)

    def predict(self, window: np.ndarray):
        """
        Predict persistent soil moisture stress.
        """
        x = self.aggregate_window(window).reshape(1, -1)

        raw_score = self.model.predict(x)[0]

        stress = self.normalize_score(raw_score)
        confidence = self.compute_confidence(window)

        return stress, confidence
