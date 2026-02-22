from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import pickle
from sklearn.cluster import KMeans
import numpy as np
import os

app = Flask(__name__)

# Your existing model training code
if os.path.exists("kmeans_model.pkl"):
    os.remove("kmeans_model.pkl")
    print("✅ Old model removed")

print("🔄 Training fresh model...")
np.random.seed(42)
data = {
    'Annual income': np.random.randint(30000,100000,100),
    'SpendingScore': np.random.randint(1,100,100)
}
df = pd.DataFrame(data)
X = df.values

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

with open("kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)
print("✅ Fresh model trained and saved!")

# ADD THIS SIMPLE HTML FORM
HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Customer Clustering API</title>
    <style>
        body { font-family: Arial; max-width: 500px; margin: 50px auto; padding: 20px; }
        label { font-weight: bold; display: block; margin-top: 15px; margin-bottom: 5px; }
        input { width: 100%; padding: 10px; margin: 5px 0 15px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { background: blue; color: white; padding: 10px 20px; border: none; cursor: pointer; border-radius: 4px; }
        button:hover { background: darkblue; }
        .result { margin-top: 20px; padding: 20px; background: #f0f0f0; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>Customer Clustering API</h1>
    <p>Enter customer details to see which cluster they belong to:</p>
    
    <label>💰 Annual Income ($)</label>
    <input type="number" id="income" placeholder="e.g., 50000" value="50000">
    
    <label>📊 Spending Score (1-100)</label>
    <input type="number" id="score" placeholder="e.g., 60" value="60">
    
    <button onclick="predict()">Predict Cluster</button>
    
    <div class="result" id="result"></div>

    <script>
        async function predict() {
            const income = document.getElementById('income').value;
            const score = document.getElementById('score').value;
            
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    'Annual income': [parseInt(income)],
                    'SpendingScore': [parseInt(score)]
                })
            });
            
            const data = await response.json();
            document.getElementById('result').innerHTML = 
                '<h3>Result:</h3>' +
                '<p>Customer belongs to <strong>Cluster ' + data.cluster + '</strong></p>';
        }
    </script>
</body>
</html>
'''

@app.route("/", methods=["GET"])
def home():
    return HTML_FORM  # Now shows a nice form instead of just text

@app.route("/predict", methods=["POST"])
def predict_cluster():
    try:
        data = request.json
        user_df = pd.DataFrame(data)
        cluster = kmeans.predict(user_df)
        return jsonify({"cluster": int(cluster[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
