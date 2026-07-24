# 📈 Sales Forecasting System

An end-to-end machine learning application that predicts future retail sales using historical sales data. The project uses **LightGBM** for regression modeling and **FastAPI** to provide real-time sales predictions through REST APIs.

---

## 🚀 Features

- Predict future sales using historical retail data
- End-to-end machine learning pipeline
- Automated data preprocessing and feature engineering
- FastAPI-based REST API for predictions
- Categorical feature encoding
- Date-based feature extraction
- Modular project structure for scalability
- Easy integration with frontend applications

---

## 🛠️ Tech Stack

### Programming Language
- Python 3.11+

### Machine Learning
- LightGBM
- Scikit-learn
- Pandas
- NumPy

### Backend
- FastAPI
- Uvicorn

### Model Serialization
- Joblib

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
sales-forecasting-system/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipelines/
│   │   ├── train_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── utils.py
│   ├── logger.py
│   └── exception.py
│
├── artifacts/
│
└── data/
```

---

## ⚙️ Workflow

1. Load historical sales dataset
2. Clean and preprocess data
3. Perform feature engineering
4. Encode categorical variables
5. Train LightGBM regression model
6. Save trained model
7. Serve predictions using FastAPI

---

## 📊 Machine Learning Pipeline

### Data Preprocessing

- Handle missing values
- Convert date column into:
  - Year
  - Month
  - Day
  - Day of Week
- Encode categorical features
- Prepare training dataset

### Model Training

Algorithm used:

- LightGBM Regressor

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## 🌐 API Endpoint

### POST `/predict`

Predict future sales.

### Sample Request

```json
{
  "store_nbr": 1,
  "family": "BEVERAGES",
  "onpromotion": 5,
  "dcoilwtico": 49.58,
  "city": "Quito",
  "state": "Pichincha",
  "store_type": "D",
  "cluster": 13,
  "is_holiday": 0,
  "date": "2017-08-15"
}
```

### Sample Response

```json
{
  "Predicted Sales": 1969.9
}
```

---

## 🖥️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/sales-forecasting-system.git
```

```bash
cd sales-forecasting-system
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the API

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

to access the Swagger UI.

---

## 📈 Future Improvements

- Hyperparameter tuning
- Model monitoring
- Docker containerization
- CI/CD pipeline
- Cloud deployment
- Interactive dashboard
- Time-series model comparison
- Automated retraining pipeline

---

## 🎯 Applications

- Retail Sales Forecasting
- Inventory Planning
- Demand Forecasting
- Business Analytics
- Revenue Estimation
- Supply Chain Optimization

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Dushyant Singh**

GitHub: https://github.com/dsparihar2005
linkedin: https://www.linkedin.com/feed/
