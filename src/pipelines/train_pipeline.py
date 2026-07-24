from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    print("Step 1: Data Ingestion")
    dataingestion = DataIngestion()
    dataingestion.load_dataset()

    print("Step 2: Data Integration")
    datatransformation = DataTransformation()
    datatransformation.integrate_data()

    print("Step 3: Data Splitting")
    datatransformation.split_data(number_of_test_days=15)

    print("Step 4: Data Transformation")
    datatransformation.transform_data()

    print("Step 5: Model Training")
    modeltrainer = ModelTrainer()
    modeltrainer.train_model()

    print("\n✅ Training completed successfully.")