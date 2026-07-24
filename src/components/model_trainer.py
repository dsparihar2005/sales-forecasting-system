from src.utils.exception import CustomException
from src.utils.logger import logging
from dataclasses import dataclass

import pandas as pd
import lightgbm as lgb
import joblib
import os
import math


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from category_encoders import OrdinalEncoder

@dataclass
class ModelTrainerConfig:
    train_data = os.path.join("artifacts", "train_data.csv")
    trained_model = os.path.join("artifacts", "trained_model.joblib")
    encoder = os.path.join("artifacts", "encoder.joblib")

class ModelTrainer:

    def __init__(self):
        self.config = ModelTrainerConfig()
        logging.info(">>> MODEL TRAINER STARTED <<<")

    def train_model(self):
        try:
            print("Loading training data...")

            df = pd.read_csv(self.config.train_data)

            print("Creating date features...")

            df["date"] = pd.to_datetime(df["date"])

            df["year"] = df["date"].dt.year
            df["month"] = df["date"].dt.month
            df["day"] = df["date"].dt.day
            df["dayofweek"] = df["date"].dt.dayofweek

            df.drop(columns=["date", "id"], inplace=True)

            print("Encoding categorical columns...")

            categorical_cols = [
                "family",
                "city",
                "state",
                "store_type"
            ]

            encoder = OrdinalEncoder(cols=categorical_cols)

            df[categorical_cols] = encoder.fit_transform(df[categorical_cols])

            X = df.drop(columns=["sales"])
            y = df["sales"]

            print("Splitting dataset...")

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )

            print("Training LightGBM model...")

            model = lgb.LGBMRegressor(
                n_estimators=300,
                learning_rate=0.05,
                max_depth=10,
                random_state=42
            )

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            mae = mean_absolute_error(y_test, predictions)
            
            rmse = math.sqrt(mean_squared_error(y_test, predictions))

            print(f"MAE  : {mae:.2f}")
            print(f"RMSE : {rmse:.2f}")

            print("Saving model...")

            joblib.dump(model, self.config.trained_model)
            joblib.dump(encoder, self.config.encoder)

            print("✅ Model saved successfully!")

        except Exception as e:
            raise CustomException(e)    