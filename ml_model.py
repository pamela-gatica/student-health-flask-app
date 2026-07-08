import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

FEATURES = [
    "Age", "Gender", "Heart_Rate", "Blood_Pressure_Systolic",
    "Blood_Pressure_Diastolic", "Stress_Level_Biosensor",
    "Stress_Level_Self_Report", "Physical_Activity", "Sleep_Quality",
    "Mood", "Study_Hours", "Project_Hours",
]
CAT_COLS = ["Gender", "Physical_Activity", "Sleep_Quality", "Mood"]
NUM_COLS = [c for c in FEATURES if c not in CAT_COLS]

_model = None


def get_model(df: pd.DataFrame):
    global _model
    if _model is None:
        preprocessor = ColumnTransformer([
            ("num", StandardScaler(), NUM_COLS),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CAT_COLS),
        ])
        pipeline = Pipeline([
            ("prep", preprocessor),
            ("clf", RandomForestClassifier(
                n_estimators=200, random_state=42, class_weight="balanced"
            )),
        ])
        pipeline.fit(df[FEATURES], df["Health_Risk_Level"])
        _model = pipeline
    return _model


def predict(model, form_data: dict):
    X = pd.DataFrame([{f: form_data[f] for f in FEATURES}])
    prediction = model.predict(X)[0]
    probas = model.predict_proba(X)[0]
    proba_dict = {cls: round(p * 100, 1) for cls, p in zip(model.classes_, probas)}
    return prediction, proba_dict
