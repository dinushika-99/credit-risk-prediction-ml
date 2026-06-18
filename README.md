# 📊 Credit Risk Prediction using Machine Learning

🚀 End-to-End Machine Learning project to predict whether a loan applicant is a GOOD or BAD credit risk using Python and Streamlit.

🌐 Live App: https://loan-risk-predictor-app.streamlit.app

---

## 📌 Project Overview

This project builds a **loan credit risk prediction system** using the German Credit Dataset.  
It analyses customer financial behaviour and predicts whether giving a loan is safe or risky.

📊 Dataset: https://www.kaggle.com/datasets/kabure/german-credit-data-with-risk

✅ Includes:
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Machine Learning Models  
- Model Tuning & Evaluation  
- Streamlit Web Application  

---

## 🧠 Problem Statement

Financial institutions need to decide:

👉 Should a loan be approved for a customer?

This project predicts:

- ✅ GOOD risk → Safe to approve loan  
- ❌ BAD risk → High risk of default  

---

## 📂 Dataset

**German Credit Dataset**

### Features:
- Age  
- Sex  
- Job  
- Housing  
- Saving accounts  
- Checking account  
- Credit amount  
- Duration  
- Purpose  

🎯 Target:
- Risk (GOOD / BAD)

---

## ⚙️ Technologies Used

- 🐍 Python  
- 🐼 Pandas  
- 🔢 NumPy  
- 📊 Matplotlib  
- 🎨 Seaborn  
- 🤖 Scikit-learn  
- 🚀 XGBoost  
- 💾 Joblib  
- 🌐 Streamlit  

---

## 🔄 Project Workflow
---
## 🧹 Data Preprocessing

- Checked missing values  
- Dropped rows with missing values  
- Removed unnecessary column (`Unnamed: 0`)  
- Checked duplicates  

📌 Dataset reduced from **1000 → 522 rows**

---

## 📊 Exploratory Data Analysis (EDA)

Visualisations used:

- 📈 Histograms (distribution of features)  
- 📦 Boxplots (outliers detection)  
- 📊 Countplots (categorical distribution)  
- 🔥 Heatmap (correlation analysis)  
- 🎯 Scatter plots (relationships between variables)  
- 🎻 Violin plots (distribution comparison)  

---

## 🔍 Key Insights

- Most customers are aged between **20–40**  
- Credit amount and duration have a **strong positive correlation**  
- High credit amount + long duration → higher risk  
- Higher job level → higher borrowing capacity  
- Low savings → unpredictable loan behaviour
