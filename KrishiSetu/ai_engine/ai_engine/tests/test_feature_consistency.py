Tests for feature fusion consistency.

from features.feature_fusion import fuse_features


def test_fuse_features_lengths():
    a = [{"a": 1}, {"a": 2}]
    b = [{"b": 3}, {"b": 4}]
    fused = fuse_features(a, b)
    assert len(fused) == 2
