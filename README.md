# AI-Discharge

AI-Discharge is a machine-learning workspace for studying electrical discharge
processes that are difficult to predict with deterministic simulation alone.
The long-term goal is to combine physical simulation, experimental data, and AI
models to better understand streamer discharges, long sparks, lightning, and
plasma-gas interaction.

Electrical discharges contain many strongly coupled and partly stochastic
processes. Examples include random photoionization, branching, leader/streamer
channel formation, gas heating, gas-density change, shock or pressure-wave
formation, and feedback between plasma chemistry and gas flow. These effects
make discharge evolution hard to predict, especially in 2D/3D simulations and
in large systems such as long sparks and lightning.

This project is intended to organize data and tools for applying AI methods to
these problems.

## Clone and Update

To clone this repository from GitHub:

```bash
git clone https://github.com/pengcz/AI-Discharge.git
cd AI-Discharge
```

To update an existing local copy with the newest code from GitHub:

```bash
cd AI-Discharge
git pull origin main
```

To check which branch you are using:

```bash
git branch
```

The main development branch is expected to be:

```text
main
```

## Research Motivation

Classical discharge simulation solves the governing equations directly. This is
essential, but it can be expensive and sensitive to small perturbations. AI can
help by learning patterns from large simulation and experimental datasets.

We are interested in questions such as:

- Can AI recognize discharge channels, branching, and streamer heads from field
  data?
- Can AI predict likely discharge development when photoionization introduces
  randomness?
- Can AI learn reduced models for plasma-gas coupling, gas heating, and gas
  expansion?
- Can AI connect different discharge regimes, such as streamer discharge, long
  spark discharge, and lightning discharge?
- Can AI build fast surrogate models for parameter studies that would be too
  expensive with full simulations?

There is already a large amount of data available from long sparks, lightning,
and streamer discharges. This repository is a place to convert that data into
machine-learning-ready formats, define labels and physical diagnostics, and
train baseline models.

## Basic Workflow

```text
1. Collect discharge data
      Simulation data, Silo files, images, diagnostics, experiment records

2. Convert physical fields
      Electron density, electric field, potential, gas temperature, pressure

3. Build ML datasets
      NumPy/NPZ arrays, image slices, 3D volumes, channel masks, CSV statistics

4. Define learning tasks
      Segmentation, prediction, surrogate modeling, uncertainty estimation

5. Train and evaluate models
      Compare AI predictions with physical simulation and known diagnostics

6. Use the model scientifically
      Identify mechanisms, speed up studies, and discover patterns in data
```

## Project Structure

```text
AI-Discharge/
├── configs/              Experiment and dataset configuration files
├── data/
│   ├── raw_silo/         Raw Silo files from simulations
│   ├── interim_npz/      Converted arrays before cleaning
│   └── processed/        ML-ready datasets
├── labels/               Channel masks and statistics
├── models/               Trained model checkpoints
├── notebooks/            Exploration notebooks
├── reports/
│   └── figures/          Plots and visual summaries
├── scripts/              Command-line scripts
├── src/
│   └── discharge_ml/     Reusable Python package
└── tests/                Small tests for scripts and utilities
```

## Discharge Processes Of Interest

### Random Photoionization

Photoionization can create seed electrons ahead of a discharge front. The exact
location of these electrons can influence streamer propagation and branching.
AI methods may help learn statistical patterns and predict possible evolution
paths rather than only one deterministic trajectory.

### Streamer Branching and Channel Growth

Streamer channels grow in high electric fields and may split into branches.
Important ML tasks include detecting channel heads, measuring channel length,
identifying branching points, and predicting the next growth direction.

### Gas Heating and Gas Fluid Motion

Discharges deposit energy into the gas through Joule heating and plasma
chemistry. The heated gas can expand, reduce gas density, drive pressure waves,
and influence later discharges. AI can help learn reduced models for this
plasma-gas feedback.

### Long Sparks and Lightning

Long sparks and lightning involve larger spatial and temporal scales, multiple
channels, leader development, and strong coupling to the surrounding gas. Data
from these discharges can be used to train models that recognize discharge
structure and compare regimes across scales.

## First ML Targets

- Channel segmentation from electron density or optical emission.
- Streamer length, radius, and branching statistics.
- Prediction of maximum electric field and electron density.
- Gas heating analysis using temperature, pressure, and density fields.
- Fast surrogate models for parameter studies.
- Uncertainty-aware prediction of possible discharge paths.
- Classification of discharge regimes from field or image data.

## Recommended Data Fields

Useful simulation variables include:

```text
e
electric_fld
phi
rhs
M
gas_rho
u
v
w
pressure
temperature
N2_B3
N2_C3
```

Useful high-level labels or diagnostics include:

```text
channel mask
streamer head location
branching point location
maximum electric field
maximum electron density
total ionized volume
heated gas volume
maximum gas temperature
pressure-wave position
discharge length
number of channels
```

## Suggested Starting Point

Start simple:

1. Convert one field such as `e` or `electric_fld` from Silo to NPZ.
2. Build a threshold-based channel mask.
3. Compute connected components and basic channel statistics.
4. Train a small baseline model for channel segmentation.
5. Add gas fields such as `temperature`, `pressure`, and `M`.
6. Test whether gas information improves prediction of later discharge growth.

## Near-Term Repository Goals

- Organize existing streamer, long spark, and lightning discharge data.
- Build conversion scripts from Silo and other data formats to ML-ready arrays.
- Define baseline labels for channels, heads, branches, and gas-heated regions.
- Train interpretable baseline models before moving to larger neural networks.
- Keep physical validation central: AI results should be compared with
  conservation laws, known discharge behavior, and simulation diagnostics.
