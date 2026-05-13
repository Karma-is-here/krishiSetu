import joblib
import numpy as np

class FusionModel:
    def __init__(self):
        self.model = joblib.load("models/fusion.pkl")

    def fuse(self, modal_scores):
        x = np.array([list(modal_scores.values())])
        return float(self.model.predict(x)[0])
