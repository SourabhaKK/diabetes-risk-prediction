"""Smoke tests: the modules import and the core helpers run on small inputs.

These do not validate model quality; they catch broken imports and regressions
in the data-loading and preprocessing helpers.
"""

import numpy as np
import pandas as pd

from src.data_loader import get_feature_info, load_diabetes_data
from src.preprocessing import (
    check_missing_values,
    get_class_distribution,
    prepare_features_target,
    scale_features,
)


def _tiny_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Diabetes_binary": [0, 0, 0, 1, 1, 0],
            "BMI": [22.0, 31.5, 27.1, 35.2, 29.9, 24.4],
            "Age": [3, 7, 5, 9, 8, 4],
        }
    )


def test_dataset_loads_with_binary_target():
    df = load_diabetes_data()
    assert len(df) > 0
    assert "Diabetes_binary" in df.columns
    assert set(df["Diabetes_binary"].unique()) <= {0, 1}


def test_feature_info_names_the_target():
    assert get_feature_info()["target"] == "Diabetes_binary"


def test_prepare_features_target_splits_columns():
    X, y = prepare_features_target(_tiny_frame())
    assert "Diabetes_binary" not in X.columns
    assert list(X.columns) == ["BMI", "Age"]
    assert len(X) == len(y) == 6


def test_scale_features_centres_training_data():
    X, _ = prepare_features_target(_tiny_frame())
    scaled, scaler = scale_features(X)
    assert np.allclose(scaled.mean(), 0.0, atol=1e-9)
    assert list(scaled.columns) == list(X.columns)


def test_scale_features_applies_training_scaler_to_test_data():
    X, _ = prepare_features_target(_tiny_frame())
    train, test, _ = scale_features(X.iloc[:4], X.iloc[4:])
    assert test.shape == (2, 2)
    assert list(test.columns) == list(train.columns)


def test_check_missing_values_counts_nulls():
    df = _tiny_frame()
    df.loc[0, "BMI"] = np.nan
    missing = check_missing_values(df)
    assert missing["BMI"] == 1
    assert missing["Age"] == 0


def test_class_distribution_reports_both_classes():
    _, y = prepare_features_target(_tiny_frame())
    dist = get_class_distribution(y)
    assert isinstance(dist, dict)
