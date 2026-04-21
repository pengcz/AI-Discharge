from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_SILO_DIR = DATA_DIR / "raw_silo"
INTERIM_NPZ_DIR = DATA_DIR / "interim_npz"
PROCESSED_DIR = DATA_DIR / "processed"
LABELS_DIR = PROJECT_ROOT / "labels"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"

