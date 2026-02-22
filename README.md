# Customer Clustering API 🚀

## Live Demo
Base URL: `https://clustering-algorithm-5.onrender.com`

## Quick Start
```python
import requests

response = requests.post(
    'https://clustering-algorithm-5.onrender.com/predict',
    json={'Annual income': [50000], 'SpendingScore': [60]}
)
print(f"Customer segment: {response.json()['cluster']}")
