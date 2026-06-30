import dagshub
import mlflow
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import json
import os

# 1. Inisialisasi DagsHub (Huruf disesuaikan persis dengan repo lu)
dagshub.init(repo_owner="just-naumi", repo_name="Eksperimen_SML_naumi", mlflow=True)
mlflow.set_tracking_uri("https://dagshub.com/just-naumi/Eksperimen_SML_naumi.mlflow")
mlflow.set_experiment("Latihan Credit Scoring")

# 2. Load Data Bersih
print("Memuat dataset...")
df = pd.read_csv('../namadataset_preprocessing/data_bersih.csv')
X = df.drop('loan_status', axis=1)
y = df['loan_status']

# 3. Training & Manual Logging
print("Mulai training model RandomForest...")
with mlflow.start_run():
    # Setup Hyperparameter
    params = {"n_estimators": 150, "max_depth": 10, "min_samples_split": 2}
    model = RandomForestClassifier(**params)
    
    # Fit Model
    model.fit(X, y)
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    print(f"Akurasi Model: {acc:.4f}")

    # Log Metrik & Parameter
    print("Logging metrik ke DagsHub...")
    mlflow.log_params(params)
    mlflow.log_metric("accuracy", acc)

    # Artefak Tambahan 1: Confusion Matrix
    print("Membuat dan menyimpan artefak Confusion Matrix...")
    cm = confusion_matrix(y, preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.savefig("training_confusion_matrix.png")
    mlflow.log_artifact("training_confusion_matrix.png")
    plt.close() # Tutup plot agar tidak numpuk

    # Artefak Tambahan 2: Info JSON
    print("Membuat dan menyimpan artefak JSON...")
    metric_info = {"dataset": "credit_risk", "model": "RandomForest", "accuracy": acc}
    with open("metric_info.json", "w") as f:
        json.dump(metric_info, f)
    mlflow.log_artifact("metric_info.json")

    # Log Model Sklearn Utama
    print("Logging model utama...")
    mlflow.sklearn.log_model(model, "model")

print("Selesai! Semua data sudah di-push ke DagsHub.")