from fastapi import FastAPI
from pydantic import BaseModel
from src.pipelines.prediction_pipeline import PredictionPipeline

app = FastAPI(
    title="Store Sales Forecasting API",
    description="Predict store sales using LightGBM",
    version="1.0"
)

# Input model
class PredictionRequest(BaseModel):
    store_nbr: int
    family: str
    onpromotion: int
    dcoilwtico: float
    city: str
    state: str
    store_type: str
    cluster: int
    is_holiday: int
    date: str


@app.get("/")
def home():
    return {
        "message": "Store Sales Forecasting API is Running!"
    }


@app.post("/predict")
def predict(request: PredictionRequest):

    pipeline = PredictionPipeline()

    prediction = pipeline.predict(
        store_nbr=request.store_nbr,
        family=request.family,
        onpromotion=request.onpromotion,
        dcoilwtico=request.dcoilwtico,
        city=request.city,
        state=request.state,
        store_type=request.store_type,
        cluster=request.cluster,
        is_holiday=request.is_holiday,
        date=request.date
    )

    return {
        "Predicted Sales": prediction
    }