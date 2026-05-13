def estimate(confidences):
    """
    Aggregate expert confidences into a single confidence score.
    Simple mean — deterministic and auditable.
    """
    if not confidences:
        return 0.0
    return float(sum(confidences) / len(confidences))
