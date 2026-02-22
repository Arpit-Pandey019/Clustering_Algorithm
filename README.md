# Customer Clustering API 🚀

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://clustering-algorithm.onrender.com)
[![GitHub](https://img.shields.io/badge/GitHub-arpit--pandey019-181717?style=for-the-badge&logo=github)](https://github.com/arpit-pandey019)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Arpit_Pandey-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/arpit-pandey-a28627302)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)

## 🌐 **Try It Live!**
**Visit the live application:** [**clustering-algorithm.onrender.com**](https://clustering-algorithm.onrender.com)

> **No setup required!** Just open the link in your browser, enter customer data, and get instant predictions.

---

## 📖 **About The Project**
This is a **production-ready Machine Learning API** that segments customers using K-means clustering. It features an interactive web interface for real-time predictions and is deployed on the Render cloud platform.

**Key Features:**
- ✅ **Instant Predictions** - Enter income & spending score, get cluster results immediately.
- ✅ **Interactive UI** - Clean, user-friendly web form.
- ✅ **Auto-Training** - The model trains itself automatically on deployment.
- ✅ **Production-Ready** - Uses Gunicorn for handling concurrent requests.

---

## 🛠️ **How to Use the API**

### **Option 1: Use the Web Interface (Easiest)**
Simply visit [**clustering-algorithm.onrender.com**](https://clustering-algorithm.onrender.com) and use the form.

### **Option 2: Make Direct API Calls**
You can integrate this API into your own applications. Here's how:

**Python Example:**
```python
import requests

# Your customer data
customer_data = {
    "Annual income": [55000],  # Income in dollars
    "SpendingScore": [75]      # Score from 1-100
}

# Call the API
response = requests.post(
    "https://clustering-algorithm.onrender.com/predict",
    json=customer_data
)

# Get the result
result = response.json()
print(f"Customer belongs to Cluster: {result['cluster']}")
```

**cURL Example:**
```bash
curl -X POST https://clustering-algorithm.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"Annual income":[48000], "SpendingScore":[42]}'
```

**JavaScript Example:**
```javascript
fetch('https://clustering-algorithm.onrender.com/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({'Annual income': [60000], 'SpendingScore': [80]})
})
.then(res => res.json())
.then(data => console.log('Cluster:', data.cluster));
```

---

## 📊 **Understanding the Results**

The model assigns customers to one of three clusters based on their income and spending habits:

| Cluster | Customer Type | Business Strategy |
|---------|---------------|-------------------|
| **0** | Budget Shopper | Send promotions, discounts, and value deals |
| **1** | Average Shopper | Regular marketing and loyalty reminders |
| **2** | Premium Shopper | VIP treatment, early access, premium offers |

---

## 💼 **Real-World Business Use Case**
An e-commerce company could use this API to:
1. Automatically segment new customers upon signup.
2. Send **targeted email campaigns** based on the cluster.
3. Personalize the shopping experience (e.g., show different products).
4. Analyze customer distribution over time.

---

## 🏗️ **Project Architecture**
```
[User Browser] → [Flask App on Render] → [KMeans Model] → [JSON Response]
       ↑                    ↑                      ↑                ↓
   Input Form        Gunicorn Server          Scikit-learn     Display Result
```

---

## 🚀 **Local Development Setup**
Want to run this locally? Follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/arpit-pandey019/REPO_NAME.git
   cd REPO_NAME
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## 📸 **Screenshots**
*(Add screenshots of your live site here to make the README visually appealing)*

| Home Page | Prediction Result |
|-----------|-------------------|
| ![Home](screenshots/home.png) | ![Result](screenshots/result.png) |

---

## 🧠 **What I Learned**
- Debugging production deployment issues (port binding, corrupted model files).
- Implementing **auto-retraining logic** to handle file corruption.
- Building user-friendly interfaces for machine learning models.
- Deploying and managing applications on the Render cloud platform.

---

## 📬 **Connect With Me**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arpit-pandey-a28627302)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/arpit-pandey019)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://clustering-algorithm.onrender.com)

- **Live Project:** [clustering-algorithm.onrender.com](https://clustering-algorithm.onrender.com)
- **GitHub:** [github.com/arpit-pandey019](https://github.com/arpit-pandey019)
- **LinkedIn:** [linkedin.com/in/arpit-pandey-a28627302](https://www.linkedin.com/in/arpit-pandey-a28627302)

---

## 👨‍💻 **About Me**
I'm Arpit Pandey, a passionate developer focused on building and deploying machine learning applications. This project demonstrates my ability to:
- Build production-ready ML APIs
- Deploy applications to cloud platforms
- Create user-friendly interfaces
- Solve real-world problems with AI

---

## ⭐ **Show Your Support**
If you found this project helpful, please consider:
- ⭐ Starring the repository on [GitHub](https://github.com/arpit-pandey019)
- 🔗 Sharing it on [LinkedIn](https://www.linkedin.com/in/arpit-pandey-a28627302)
- 💬 Reaching out for collaborations or questions

---

## 📄 **License**
Distributed under the MIT License. See `LICENSE` for more information.
