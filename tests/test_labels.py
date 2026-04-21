import numpy as np

from discharge_ml.labels import basic_channel_stats, threshold_channel_mask


def test_threshold_channel_mask():
    field = np.array([0.0, 2.0, 5.0])
    mask = threshold_channel_mask(field, 1.0)
    assert mask.tolist() == [False, True, True]


def test_basic_channel_stats():
    mask = np.array([False, True, True, False])
    stats = basic_channel_stats(mask)
    assert stats["active_cells"] == 2
    assert stats["total_cells"] == 4
    assert stats["active_fraction"] == 0.5

