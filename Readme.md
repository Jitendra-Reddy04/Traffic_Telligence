# 🚦 Traffic_Telligence  
### Traffic Volume Estimation Using Machine Learning

Traffic_Telligence is a machine learning–based project that predicts **traffic volume** using historical data, weather conditions, and time-based features. The project also includes a **Flask web application** for user interaction and prediction display.

---

## 📌 Overview
Traffic congestion is a major challenge in urban areas. This project aims to estimate traffic volume accurately using machine learning models trained on real-world traffic and weather data. The system helps in understanding traffic patterns and supports better traffic planning and management.

---

## 🧠 Machine Learning Details
- **Problem Type:** Regression  
- **Model Used:** Random Forest Regressor  
- **Preprocessing:**  
  - Label Encoding  
  - Standard Scaling  
- **Evaluation Metrics:**  
  - Mean Squared Error (MSE)  
  - R² Score  

---

## 🌐 Flask Web Application
The Flask app allows users to:
- Enter traffic-related inputs
- Predict traffic volume
- View results through a simple HTML interface

---
#Folder structure
Traffic_Telligence/
├── Flask/
│ ├── app.py
│ └── templates/
│ ├── index.html
│ └── output.html
├── traffic_volume.ipynb
├── .gitignore
└── README.md


> **Note:** Model files (`.pkl`) and dataset files (`.csv`) are excluded using `.gitignore` due to GitHub size limits.

---

## ⚙️ How to Run
```bash
git clone https://github.com/Jitendra-Reddy04/Traffic_Telligence.git
cd Traffic_Telligence
pip install numpy pandas scikit-learn flask matplotlib
python Flask/app.py
