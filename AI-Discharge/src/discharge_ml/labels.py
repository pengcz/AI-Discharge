import numpy as np


def threshold_channel_mask(field: np.ndarray, threshold: float) -> np.ndarray:
    """Create a binary channel mask from a scalar discharge field."""
    return field > threshold


def basic_channel_stats(mask: np.ndarray) -> dict[str, float]:
    """Return simple mask statistics without external dependencies."""
    active_cells = int(mask.sum())
    total_cells = int(mask.size)
    return {
        "active_cells": active_cells,
        "total_cells": total_cells,
        "active_fraction": active_cells / total_cells if total_cells else 0.0,
    }

