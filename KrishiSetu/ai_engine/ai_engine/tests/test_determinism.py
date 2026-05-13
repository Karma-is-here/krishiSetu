Tests for deterministic inference.

from inference.deterministic_inference import run_inference


def test_run_inference_deterministic():
    features = [{"x": 1}, {"y": 2}]
    out1 = run_inference(features)
    out2 = run_inference(features)
    assert out1 == out2
