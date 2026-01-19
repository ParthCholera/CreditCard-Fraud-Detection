# 💳 Credit Card Fraud Detection using Machine Learning

An end-to-end Data Science project that detects fraudulent credit card transactions using a Random Forest classifier and deploys the model with a Streamlit web application.

This project handles highly imbalanced data and focuses on maximizing **fraud recall** — so fewer fraud cases are missed.

---

## 🚀 Features
- Handles imbalanced dataset using SMOTE
- Trained with Random Forest Classifier
- High Fraud Detection Recall (~99%)
- Deployed using Streamlit
- Interactive Web App for Predictions

---

## 🧠 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- imbalanced-learn (SMOTE)  
- Streamlit  
- Joblib  

---

## 📊 Model Performance
- Accuracy: ~99–100%  
- Fraud Recall: ~99%  
- Confusion Matrix used for evaluation

---

## 📁 Project Structure

CreditCard-Fraud-Detection/
│
├── app.py # Streamlit Web App
├── fraud_model.pkl # Trained ML Model
├── requirements.txt # Dependencies
├── README.md # Project Documentation


---

## ▶️ How to Run Locally

1️⃣ Clone the repository:
```bash
git clone https://github.com/ParthCholera/CreditCard-Fraud-Detection.git
cd CreditCard-Fraud-Detection

pip install -r requirements.txt

streamlit run app.py

http://localhost:8501
