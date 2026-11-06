# Project Structure

```
diabetes-risk-prediction/
│
├── data/                           # Dataset directory
│   └── CDC Diabetes Dataset.csv   # CDC BRFSS 2015 diabetes dataset
│
├── notebooks/                      # Jupyter notebooks for development
│   ├── classification_model.ipynb # Supervised learning experiments
│   ├── clustering_analysis.ipynb  # Unsupervised learning experiments
│   └── data_exploration.ipynb     # Initial data exploration
│
├── outputs/                        # Generated outputs
│   ├── figures/                   # All visualization outputs (13 figures)
│   │   ├── class_distribution.png
│   │   ├── cluster_profiles.png
│   │   ├── clustering_comparison.png
│   │   ├── confusion_matrix.png
│   │   ├── diabetes_by_cluster.png
│   │   ├── elbow_curve.png
│   │   ├── feature_correlations.png
│   │   ├── feature_importance.png
│   │   ├── figure_demographic_prevalence.png  # NEW: EDA enhancement
│   │   ├── figure_eda_distributions.png       # NEW: EDA enhancement
│   │   ├── hyperparameter_sensitivity.png
│   │   ├── model_comparison.png
│   │   └── roc_curve.png
│   │
│   └── tables/                    # Generated tables (5 files)
│
├── scripts/                        # Analysis and utility scripts
│   ├── README.md                  # Scripts documentation
│   ├── enhanced_eda.py            # Statistical validation & EDA figures
│   └── generate_statistics.py    # Cluster profiling & fairness analysis
│
├── src/                           # Core Python modules
│   ├── __init__.py
│   ├── classification.py          # Logistic regression & decision tree
│   ├── clustering.py              # K-Means clustering
│   ├── clustering_comparison.py   # K-Means vs DBSCAN comparison
│   ├── data_loader.py             # Data loading utilities
│   ├── hyperparameter_analysis.py # Hyperparameter sensitivity analysis
│   ├── model_comparison.py        # Model comparison utilities
│   └── preprocessing.py           # Data preprocessing
│
├── .gitignore                     # Git ignore rules
├── LICENSE                        # MIT License
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

## Directory Descriptions

### `data/`
Contains the CDC BRFSS 2015 diabetes dataset (253,680 records, 21 features).

### `notebooks/`
Jupyter notebooks used for exploratory analysis and model development. These document the iterative development process.

### `outputs/`
All generated outputs from the analysis:
- **figures/**: 13 PNG visualizations
- **tables/**: Generated statistical tables

### `scripts/`
Utility scripts for enhanced analysis:
- **enhanced_eda.py**: Generates statistical validation and EDA figures for Section 2.2
- **generate_statistics.py**: Generates cluster profiling and fairness analysis for Sections 3.4 and 4.8

### `src/`
Core Python modules implementing the machine learning pipeline:
- Data loading and preprocessing
- Clustering algorithms (K-Means, DBSCAN)
- Classification models (Logistic Regression, Decision Tree)
- Model comparison and evaluation
- Hyperparameter analysis

## Key Files

- **requirements.txt**: Python package dependencies
- **README.md**: Comprehensive project documentation

## Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run analysis scripts:**
   ```bash
   python scripts/enhanced_eda.py
   python scripts/generate_statistics.py
   ```

## Notes

- The project follows a clean separation: `src/` for core modules, `scripts/` for analysis utilities, `notebooks/` for development
- Dataset is loaded locally from `data/` directory
