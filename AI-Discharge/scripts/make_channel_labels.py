#!/usr/bin/env python3
"""Create simple threshold channel labels from NPZ field data."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from discharge_ml.labels import basic_channel_stats, threshold_channel_mask


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_npz", type=Path)
    parser.add_argument("output_mask_npz", type=Path)
    parser.add_argument("--threshold", type=float, default=1.0e18)
    parser.add_argument("--stats-csv", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with np.load(args.input_npz) as data:
        field = data["uniform_data"]

    mask = threshold_channel_mask(field, args.threshold)
    args.output_mask_npz.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.output_mask_npz, channel_mask=mask)

    if args.stats_csv:
        stats = basic_channel_stats(mask)
        args.stats_csv.parent.mkdir(parents=True, exist_ok=True)
        with args.stats_csv.open("w", newline="") as fp:
            writer = csv.DictWriter(fp, fieldnames=stats.keys())
            writer.writeheader()
            writer.writerow(stats)


if __name__ == "__main__":
    main()

