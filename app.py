from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.cluster import KMeans
import numpy as np
import os

app = Flask(__name__)

# CHECK IF MODEL EXISTS, IF NOT CREATE IT
if not os.path.exists("kmeans_model.pkl"):
    print("🔄 Model not found. Training new model...")
    # Sample data (your original dataset)
    np.random.seed(42)
    data = {
        'Annual income': np.random.randint(30000,100000,100),
        'SpendingScore': np.random.randint(1,100,100)
    }
    df = pd.DataFrame(data)
    X = df.values
    
    # Train KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)
    
    # Save model
    with open("kmeans_model.pkl", "wb") as f:
        pickle.dump(kmeans, f)
    print("✅ Model trained and saved!")
else:
    print("✅ Model found, loading existing model...")
    with open("kmeans_model.pkl", "rb") as f:
        kmeans = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "KMeans Clustering API is running!"

@app.route("/predict", methods=["POST"])
def predict_cluster():
    data = request.json
    user_df = pd.DataFrame(data)
    cluster = kmeans.predict(user_df)
    return jsonify({"cluster": int(cluster[0])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
