# Diabetes Risk Prediction and Population Health Profiling

> **Evidence-based machine learning for diabetes risk stratification using CDC BRFSS 2015 data**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Methodology](#-methodology)
- [Results & Findings](#-results--findings)
- [Visualizations](#-visualizations)
- [Project Structure](#-project-structure)
- [Installation & Usage](#-installation--usage)
- [Key Insights](#-key-insights--learnings)
- [Limitations & Future Work](#-limitations--future-work)
- [References](#-references)
- [Author](#-author)

---

## 🎯 Overview

This project demonstrates **systematic, evidence-based application of machine learning** to diabetes risk prediction using the CDC BRFSS 2015 dataset (253,680 survey responses). The work combines unsupervised and supervised learning to identify population health segments and predict individual diabetes risk, with emphasis on **interpretability, fairness, and responsible deployment practices**.

### Purpose

Address the public health challenge of diabetes screening and risk stratification by:
- Identifying distinct population segments for targeted interventions
- Predicting individual diabetes risk using interpretable models
- Evaluating model fairness across demographic subgroups
- Demonstrating responsible healthcare ML deployment practices

### Approach

**Dual Methodology:**
1. **Unsupervised Learning**: K-Means clustering (k=3) for population health profiling
2. **Supervised Learning**: Logistic Regression for transparent risk prediction

### Highlights

The project demonstrates:
- Literature-grounded algorithm selection
- Statistical validation of exploratory analysis
- Actionable cluster interpretation for public health
- Comprehensive fairness analysis across demographics
- Honest acknowledgment of limitations

---

## ✨ Key Features

- 📊 **Dual Methodology**: Combines unsupervised (K-Means) and supervised (Logistic Regression) learning
- 📈 **Statistical Rigor**: Mann-Whitney U tests, Chi-square analysis (χ²=18537.57), cross-validation
- 🎯 **Actionable Insights**: Three risk-stratified population segments (9.3%, 13.3%, 34.2% prevalence)
- ⚖️ **Fairness Analysis**: Comprehensive evaluation across income, education, and gender demographics
- 🔍 **Interpretability First**: Prioritizes explainable models for clinical governance
- 📚 **Literature-Grounded**: Benchmarked against published results (Küsmüş 2025: ROC-AUC 0.83)
- 🏥 **Healthcare-Focused**: Evaluation criteria aligned with deployment requirements

---

## 🔬 Methodology

### Data Source

**Dataset**: [CDC BRFSS 2015 Diabetes Health Indicators](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators)  
**Source**: UCI Machine Learning Repository (ID 891)

**Characteristics:**
- **Records**: 253,680 survey responses
- **Features**: 21 health indicators (BMI, age, general health, high BP, high cholesterol, etc.)
- **Target**: Binary classification (diabetes/no diabetes)
- **Class Imbalance**: 5.35:1 (more non-diabetic cases)
- **Data Type**: Self-reported survey data (BRFSS 2015)

### Evaluation Framework

**CRISP-DM Methodology** with five healthcare-specific criteria:

1. **Interpretability**: Can stakeholders understand model decisions?
2. **Stability**: Does performance generalize across data partitions?
3. **Scalability**: Can the approach handle population-level data?
4. **Clinical Communicability**: Can results inform public health actions?
5. **Governance Readiness**: Is the model suitable for regulatory scrutiny?

### Unsupervised Learning: K-Means Clustering

**Objective**: Identify population segments with distinct diabetes risk profiles

**Algorithm**: K-Means (k=3)

**Justification:**
- **Interpretable**: Clear centroids for health professionals
- **Scalable**: Efficient with 253K records
- **Empirically validated**: Compared against DBSCAN (unstable: 4K-10K noise points)

**Cluster Selection:**
- Elbow method suggested k=3-4
- k=3 aligns with low/moderate/high risk stratification
- Silhouette score: 0.3 (moderate separation, typical for health data)

### Supervised Learning: Logistic Regression

**Objective**: Predict individual diabetes risk with interpretable coefficients

**Algorithm**: Logistic Regression with balanced class weights

**Justification:**
- **Competitive Performance**: ROC-AUC 0.818 vs published ensemble methods (0.83)
- **Interpretability**: Coefficient-based explanations for clinical governance
- **Probabilistic**: Provides risk scores, not just binary predictions
- **Literature-Aligned**: Feature importance matches published findings (HighBP, BMI, GenHlth, Age)

**Key Parameters:**
- `class_weight='balanced'`: Addresses 5.35:1 class imbalance
- Default regularization: Avoids overfitting
- 80-20 stratified train-test split

**Evaluation Metrics:**
- **ROC-AUC**: Overall discriminative ability
- **Recall**: Proportion of diabetics correctly identified (critical for screening)
- **Precision**: Proportion of positive predictions that are correct
- **Cross-Validation**: 5-fold CV confirms stability (0.818 ± 0.012)

---

## 📊 Results & Findings

### Clustering Results: Three Population Segments

| Cluster | Population % | Diabetes Prevalence | Median BMI | Median Age | High BP | High Chol | Risk Level |
|---------|--------------|---------------------|------------|------------|---------|-----------|------------|
| **Low Risk** | 70% | **9.3%** | 26.0 | 7 (younger) | 28% | 35% | ⬇️ Low |
| **Moderate Risk** | 5% | **13.3%** | 29.5 | 9 (middle) | 52% | 48% | ➡️ Moderate |
| **High Risk** | 25% | **34.2%** | 32.0 | 11 (older) | 76% | 68% | ⬆️ High |

**Key Insight**: **3.7x risk ratio** between low and high-risk clusters demonstrates meaningful population stratification without using outcome labels.

**Public Health Implications:**
- **Low Risk (70%)**: Mass education and lifestyle interventions sufficient
- **Moderate Risk (5%)**: Targeted screening programs warranted
- **High Risk (25%)**: Intensive screening, clinical follow-up, aggressive risk factor management required

### Classification Performance

| Metric | Value | Literature Benchmark | Interpretation |
|--------|-------|----------------------|----------------|
| **ROC-AUC** | **0.818** | 0.83 (Küsmüş 2025) | Competitive with ensemble methods |
| **Recall** | 0.761 | - | 76% of diabetics identified |
| **Precision** | 0.341 | - | 34% of positive predictions correct |
| **Cross-Val Std** | ±0.012 | - | Highly stable performance |

> **Performance Context**: Our logistic regression achieves ROC-AUC of 0.818, competitive with published Gradient Boosting/XGBoost (0.83) while maintaining coefficient-based interpretability essential for clinical governance. The 1-2% performance difference does not justify the loss of explainability.

### Statistical Validation

**Exploratory Data Analysis (Mann-Whitney U, Chi-square tests):**

| Comparison | No Diabetes | Diabetes | Test Statistic | p-value | Interpretation |
|------------|-------------|----------|----------------|---------|----------------|
| **Median BMI** | 27.0 | 31.0 | Mann-Whitney U | p < 0.001 | Highly significant |
| **Median Age Category** | 8.0 | 10.0 | Mann-Whitney U | p < 0.001 | Highly significant |
| **High BP Prevalence** | 37.1% | 73.8% | χ² = 18537.57 | p < 0.001 | Strong association |

**Validation**: Observed patterns align with established clinical risk factors, confirming dataset contains clinically plausible signal.

### Fairness Analysis: Demographic Subgroup Performance

| Subgroup | ROC-AUC | Recall | Precision | Performance Gap |
|----------|---------|--------|-----------|-----------------|
| **Low Income (1-3)** | 0.76 | 0.89 | 0.39 | **-6%** vs High Income |
| **High Income (6-8)** | 0.82 | 0.66 | 0.31 | Reference |
| **Low Education (1-3)** | 0.76 | 0.91 | 0.41 | **-7%** vs High Education |
| **High Education (5-6)** | 0.83 | 0.71 | 0.33 | Reference |
| **Female** | 0.83 | 0.76 | 0.35 | +3% vs Male |
| **Male** | 0.80 | 0.76 | 0.33 | Reference |

> ⚠️ **Critical Finding**: Performance degradation for low-income and low-education groups (6-7% lower ROC-AUC) reflects **data quality disparities** from reduced healthcare access, not algorithmic bias alone. Deployment would require monitoring for bias amplification and potentially stratified models for vulnerable subgroups.

### Feature Importance

**Top Predictors** (aligned with literature):
1. **General Health Status** (GenHlth)
2. **Body Mass Index** (BMI)
3. **Age**
4. **High Blood Pressure** (HighBP)
5. **High Cholesterol** (HighChol)

**Validation**: Feature importance aligns with published findings (Küsmüş 2025; Sadaria & Parekh 2024), providing independent validation that the model captures clinically meaningful risk patterns.

---

## 📈 Visualizations

### Key Figures

**Enhanced Exploratory Data Analysis:**
- **Figure 1**: Distribution of key health indicators by diabetes status (6-panel violin plots)
- **Figure 2**: Diabetes prevalence across demographic groups (income, education, age)

**Clustering Analysis:**
- **Figure 3**: Elbow curve for cluster selection
- **Figure 4**: Cluster profiles (mean feature values)
- **Figure 5**: Diabetes prevalence by cluster
- **Figure 6**: K-Means vs DBSCAN comparison

**Classification Performance:**
- **Figure 7**: Model comparison (Logistic Regression vs Decision Tree)
- **Figure 8**: Confusion matrix
- **Figure 9**: ROC curve (AUC = 0.818)
- **Figure 10**: Feature importance (logistic regression coefficients)
- **Figure 11**: Hyperparameter sensitivity analysis

All visualizations available in `outputs/figures/`

---

## 📁 Project Structure

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
├── PROJECT_STRUCTURE.md           # Detailed project structure documentation
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

---

## 🚀 Installation & Usage

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/diabetes-risk-prediction.git
cd diabetes-risk-prediction
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Analysis

#### Option 1: Jupyter Notebooks (Recommended for Exploration)

```bash
jupyter notebook
```

Run notebooks in order:
1. `notebooks/data_exploration.ipynb`
2. `notebooks/clustering_analysis.ipynb`
3. `notebooks/classification_model.ipynb`

#### Option 2: Python Scripts (For Generating Enhanced Statistics)

```bash
# Generate enhanced EDA figures and statistical validation
python scripts/enhanced_eda.py

# Generate cluster profiling and fairness analysis
python scripts/generate_statistics.py
```

#### Option 3: Python API (For Integration)

```python
from src.data_loader import load_diabetes_data
from src.preprocessing import preprocess_data
from src.clustering import perform_clustering
from src.classification import train_logistic_regression, evaluate_model

# Load and prepare data
df = load_diabetes_data()
X_train, X_test, y_train, y_test = preprocess_data(df)

# Perform clustering
kmeans, labels, silhouette = perform_clustering(X_train, n_clusters=3)

# Train classifier
model = train_logistic_regression(X_train, y_train)

# Evaluate
metrics, y_pred, y_proba = evaluate_model(model, X_test, y_test)
print(f"ROC-AUC: {metrics['roc_auc']:.3f}")
```

### Dependencies

```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
ucimlrepo>=0.0.3
jupyter>=1.0.0
```

See `requirements.txt` for complete list.

---

## 💡 Key Insights & Learnings

### Technical Learnings

**1. Interpretability-Performance Trade-offs**
- Logistic Regression (ROC-AUC 0.818) vs Ensemble Methods (0.83)
- **Decision**: 1-2% performance difference does not justify loss of coefficient-based explanations
- **Lesson**: In healthcare ML, interpretability is a deployment requirement, not a nice-to-have

**2. Statistical Validation Matters**
- Mann-Whitney U tests validate observed BMI/Age differences (p < 0.001)
- Chi-square test confirms High BP association (χ² = 18537.57)
- **Lesson**: Statistical testing distinguishes genuine patterns from sampling artifacts

**3. Fairness as a First-Class Concern**
- 6-7% ROC-AUC degradation for low-income/education groups
- Root cause: data quality disparities from healthcare access inequalities
- **Lesson**: Algorithmic fairness cannot compensate for systemic data inequalities

### Methodological Decisions

**Why K-Means over DBSCAN?**
- DBSCAN produced 4,000-10,000 noise points with unstable cluster counts (0-21)
- K-Means provided stable 3 clusters with interpretable centroids
- **Justification**: Stability and interpretability outweigh DBSCAN's theoretical advantages

**Why Logistic Regression over Random Forests?**
- Marginal performance gain (1.8% ROC-AUC difference with Decision Tree)
- Coefficient-based explanations essential for clinical governance
- **Justification**: Governance readiness prioritized over raw performance

**Why Balanced Weighting over SMOTE?**
- Avoids creating synthetic data patterns
- Maintains original data distribution
- **Justification**: Simplicity and authenticity over complex resampling

### Healthcare Context

**Population Segmentation for Resource Allocation:**
- Low-risk cluster (70%): Mass education sufficient
- Moderate-risk cluster (5%): Targeted screening
- High-risk cluster (25%): Intensive intervention

**False Negative Implications:**
- Even 76% recall means 24% of diabetics missed
- In screening contexts, false negatives delay necessary care
- **Deployment requirement**: Clear communication that model is preliminary screening, not diagnosis

**Data Quality as Root Cause:**
- Performance disparities reflect healthcare access inequalities
- Technical solutions alone cannot solve systemic problems
- **Deployment requirement**: Address upstream data collection disparities

---

## ⚠️ Limitations & Future Work

### Current Limitations

**Data Limitations:**
- **Self-reported data**: Introduces recall bias and measurement error
- **2015 temporal constraints**: Health patterns may have shifted (COVID-19, policy changes)
- **Survey bias**: Respondents may not represent full population (underrepresentation of vulnerable groups)
- **Binary target**: Diabetes risk exists on continuum, but data is binary

**Model Limitations:**
- **Linear assumptions**: Logistic regression cannot capture complex non-linear interactions
- **Feature interactions**: May underestimate risk for unusual combinations of risk factors
- **Generalization**: Trained on 2015 US survey data—may not generalize to other populations/time periods

**Deployment Limitations:**
- **Educational demonstration**: Not validated for clinical deployment
- **No regulatory approval**: Would require prospective validation, clinical oversight
- **No clinical workflow integration**: Deployment requires integration with existing systems

### Future Improvements

**Phase 1: Enhanced Validation (3-6 months)**
- Bootstrap validation of cluster stability (1000 iterations)
- Threshold optimization with cost-benefit analysis
- Calibration analysis for predicted probabilities (Platt scaling, isotonic regression)

**Phase 2: Advanced Modeling (6-12 months)**
- Integration of clustering features into classification (cluster membership as feature)
- Stratified models for demographic subgroups (address fairness disparities)
- Ensemble methods with interpretability tools (SHAP, partial dependence plots)

**Phase 3: Deployment Preparation (12-18 months)**
- Prospective validation on new survey waves (2017, 2019, 2021 BRFSS)
- Integration with electronic health records for validation against clinical diagnoses
- Continuous monitoring and recalibration as population health patterns evolve
- Regulatory compliance assessment (FDA, MHRA)

---

## 📚 References

### Key Publications

1. **Küsmüş, A. (2025)**. Diabetes Prediction Based on Health Indicators Using Machine Learning: Feature Selection and Algorithm Comparison. *International Journal of Advanced Engineering and Management Research*, 10(02), 281-292. [https://doi.org/10.51505/ijaemr.2025.1115](https://doi.org/10.51505/ijaemr.2025.1115)

2. **SaiTeja, L., Regulwar, G. B., Sai Anish Reddy, G., Satwick, T., Kulkarni, V., Singh, S., & Shalini, K. (2025)**. Diabetes Prediction by Using Various Machine-Learning Algorithms. In *Intelligent Data Engineering and Analytics* (pp. 233-243). Springer.

3. **Sadaria, P., & Parekh, R. (2024)**. An Analysis of Machine Learning Approaches for Diabetic Prediction. In *Deep Learning and Visual Artificial Intelligence* (pp. 49-57). Springer.

### Dataset

**Teboul, A. (2021)**. CDC Diabetes Health Indicators Dataset. UCI Machine Learning Repository. [https://archive.ics.uci.edu/dataset/891](https://archive.ics.uci.edu/dataset/891)

### Data Source

**Centers for Disease Control and Prevention (2024)**. Behavioral Risk Factor Surveillance System (BRFSS). [https://www.cdc.gov/brfss/](https://www.cdc.gov/brfss/)

### Technical References

**Pedregosa, F., et al. (2011)**. Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.

---

## 👤 Author

**Sourabha K Kallapur**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

## 🙏 Acknowledgments

- **CDC** for maintaining the BRFSS dataset
- **UCI Machine Learning Repository** for dataset hosting
- **Scikit-learn Community** for excellent ML library and documentation
- **Published Researchers** (Küsmüş, SaiTeja, Sadaria & Parekh) for benchmarking context

---

<div align="center">

*Demonstrating responsible, interpretable, and fair machine learning for healthcare applications*

</div>
