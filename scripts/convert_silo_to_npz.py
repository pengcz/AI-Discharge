#!/usr/bin/env python3
"""Convert Silo discharge output to NPZ arrays.

This script is a placeholder wrapper. The actual Silo reading is usually done
with AFIVO's tools, for example:

    afivo/tools/plot_raw_data.py input.silo -variable e -save_npz output.npz

Keep this file as the project-level entry point for later automation.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_silo", type=Path)
    parser.add_argument("variable", type=str)
    parser.add_argument("output_npz", type=Path)
    parser.add_argument(
        "--plot-raw-data",
        type=Path,
        default=Path("../afivo-streamer/afivo/tools/plot_raw_data.py"),
        help="Path to AFIVO plot_raw_data.py",
    )
    parser.add_argument("--min-pixels", type=int, default=512)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_npz.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(args.plot_raw_data),
        str(args.input_silo),
        "-variable",
        args.variable,
        "-min_pixels",
        str(args.min_pixels),
        "-save_npz",
        str(args.output_npz),
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

