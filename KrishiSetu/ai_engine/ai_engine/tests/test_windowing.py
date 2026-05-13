Tests for temporal windowing.

from temporal.window_builder import build_windows


def test_build_windows_basic():
    seq = list(range(5))
    windows = build_windows(seq, 3)
    assert windows == [seq[0:3], seq[1:4], seq[2:5]]
