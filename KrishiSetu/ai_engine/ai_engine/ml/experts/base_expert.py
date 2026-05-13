import numpy as np

class BaseExpert:
    """
    Common logic shared by all modality experts.
    Enforces consistency, safety, and auditability.
    """

    def aggregate_window(self, window: np.ndarray) -> np.ndarray:
        """
        Aggregate a temporal window into a fixed-length vector.
        Uses mean + std to preserve level and volatility.
        """
        mean = window.mean(axis=0)
        std = window.std(axis=0)
        return np.concatenate([mean, std])

    def compute_confidence(self, window: np.ndarray) -> float:
        """
        Confidence inversely related to volatility.
        High volatility → lower confidence.
        """
        volatility = np.mean(np.std(window, axis=0))
        confidence = 1.0 - volatility
        return float(np.clip(confidence, 0.0, 1.0))

    def normalize_score(self, score: float) -> float:
        """
        Clamp stress scores into [0, 1].
        Ensures fusion stability.
        """
        return float(np.clip(score, 0.0, 1.0))
