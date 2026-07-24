import os
import joblib
import pandas as pd
from dataclasses import dataclass


@dataclass
class PredictionPipelineConfig:
    model_path = os.path.join("artifacts", "trained_model.joblib")
    encoder_path = os.path.join("artifacts", "encoder.joblib")


class PredictionPipeline:

    def __init__(self):
        self.model = joblib.load(PredictionPipelineConfig.model_path)
        self.encoder = joblib.load(PredictionPipelineConfig.encoder_path)

    def predict(
        self,
        store_nbr,
        family,
        onpromotion,
        dcoilwtico,
        city,
        state,
        store_type,
        cluster,
        is_holiday,
        date,
    ):

        date = pd.to_datetime(date)

        sample = pd.DataFrame({
            "store_nbr": [store_nbr],
            "family": [family],
            "onpromotion": [onpromotion],
            "dcoilwtico": [dcoilwtico],
            "city": [city],
            "state": [state],
            "store_type": [store_type],
            "cluster": [cluster],
            "is_holiday": [is_holiday],
            "year": [date.year],
            "month": [date.month],
            "day": [date.day],
            "dayofweek": [date.dayofweek]
        })

        categorical = ["family", "city", "state", "store_type"]

        sample[categorical] = self.encoder.transform(sample[categorical])

        prediction = self.model.predict(sample)

        return round(float(prediction[0]), 2)