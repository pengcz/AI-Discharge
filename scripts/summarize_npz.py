#!/usr/bin/env python3
"""Print basic statistics for one or more NPZ discharge arrays."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--key", default="uniform_data")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for path in args.files:
        with np.load(path) as data:
            field = data[args.key]
        print(
            f"{path}: shape={field.shape} "
            f"min={field.min():.6e} max={field.max():.6e} "
            f"mean={field.mean():.6e}"
        )


if __name__ == "__main__":
    main()

