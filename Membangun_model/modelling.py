import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import json

# Set tracking URI ke localhost
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
mlflow.set_experiment("Latihan Credit Scoring")

# Load data bersih
df = pd.read_csv('../namadataset_preprocessing/data_bersih.csv')
X = df.drop('loan_status', axis=1)
y = df['loan_status']

# Training dengan manual logging
with mlflow.start_run():
    params = {"n_estimators": 100, "max_depth": 5}
    model = RandomForestClassifier(**params)
    model.fit(X, y)
    
    # Logging parameter
    mlflow.log_params(params)
    
    # Logging metrik
    predictions = model.predict(X)
    acc = accuracy_score(y, predictions)
    mlflow.log_metric("accuracy", acc)
    
    # Logging artefak (model)
    mlflow.sklearn.log_model(model, "model")
    
    print(f"Model trained with accuracy: {acc}")