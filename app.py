from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained KMeans model
with open("kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict_cluster():
    data = request.json  # Expect JSON input like {"Annual income":[...], "SpendingScore":[...]}
    user_df = pd.DataFrame(data)
    cluster = kmeans.predict(user_df)
    return jsonify({"cluster": int(cluster[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)