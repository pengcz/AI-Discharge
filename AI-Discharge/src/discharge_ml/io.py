from pathlib import Path

import numpy as np


def load_npz_field(path: str | Path, key: str = "uniform_data") -> np.ndarray:
    """Load a field array from an NPZ file created from discharge output."""
    with np.load(path) as data:
        return data[key]


def save_npz_field(path: str | Path, field: np.ndarray, **metadata) -> None:
    """Save one field plus optional metadata into an NPZ file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path, uniform_data=field, **metadata)

