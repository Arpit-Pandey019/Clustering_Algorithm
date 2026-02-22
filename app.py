from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.cluster import KMeans
import numpy as np
import os

app = Flask(__name__)

# FORCE DELETE any existing model and train a NEW one
print("⚠️ Removing any old model file to ensure clean training...")
if os.path.exists("kmeans_model.pkl"):
    os.remove("kmeans_model.pkl")
    print("✅ Old model removed")

print("🔄 Training fresh model...")
# Sample data (your original dataset)
np.random.seed(42)
data = {
    'Annual income': np.random.randint(30000, 100000, 100),
    'SpendingScore': np.random.randint(1, 100, 100)
}
df = pd.DataFrame(data)
X = df.values

# Train KMeans
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# Save model
with open("kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)
print("✅ Fresh model trained and saved!")

@app.route("/", methods=["GET"])
def home():
    return "KMeans Clustering API is running! Use POST /predict with JSON data."

@app.route("/predict", methods=["POST"])
def predict_cluster():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
            
        user_df = pd.DataFrame(data)
        cluster = kmeans.predict(user_df)
        return jsonify({"cluster": int(cluster[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "model_loaded": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
