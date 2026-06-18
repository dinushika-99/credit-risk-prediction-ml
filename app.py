import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.block-container{
    padding-top:0rem;
    padding-left:2rem;
    padding-right:2rem;
}

#MainMenu, footer, header{
    visibility:hidden;
}

.banner{
    background-image:url('https://images.unsplash.com/photo-1560472355-536de3962603?w=1600&q=90');
    background-size:cover;
    background-position:center;
    height:260px;
    border-radius:12px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    margin-bottom:25px;
}

.banner h1{
    color:white;
    font-size:42px;
    margin-bottom:10px;
}

.banner p{
    color:white;
    font-size:18px;
}

.result-good{
    background:#d4edda;
    color:#155724;
    padding:15px;
    border-radius:10px;
    text-align:center;
    font-size:22px;
    font-weight:bold;
}

.result-bad{
    background:#f8d7da;
    color:#721c24;
    padding:15px;
    border-radius:10px;
    text-align:center;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.markdown("""
<div class="banner">
    <h1>💳 Credit Risk Prediction</h1>
    <p>Predict whether a customer is a Good or Bad Credit Risk</p>
</div>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("extra_trees_credit_model.pkl")

encoders = {
    col: joblib.load(f"{col}_encoder.pkl")
    for col in [
        "Sex",
        "Housing",
        "Saving accounts",
        "Checking account"
    ]
}

# ---------------- FORM ----------------
left, right = st.columns(2)

with left:
    st.subheader("👤 Personal Information")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=30
    )

    sex = st.selectbox(
        "Sex",
        ["male", "female"]
    )

    job = st.number_input(
        "Job (0-3)",
        min_value=0,
        max_value=3,
        value=1
    )

    housing = st.selectbox(
        "Housing",
        ["own", "rent", "free"]
    )

with right:
    st.subheader("🏦 Financial Information")

    saving_accounts = st.selectbox(
        "Saving Accounts",
        ["little", "moderate", "quite rich", "rich"]
    )

    checking_account = st.selectbox(
        "Checking Account",
        ["little", "moderate", "rich", "very rich"]
    )

    credit_amount = st.number_input(
        "Credit Amount",
        min_value=0,
        value=1000
    )

    duration = st.number_input(
        "Duration (Months)",
        min_value=1,
        value=12
    )

# ---------------- PREDICT BUTTON ----------------
st.write("")

predict = st.button(
    "🔍 Predict Risk",
    use_container_width=True
)

# ---------------- PREDICTION ----------------
if predict:

    input_df = pd.DataFrame({
        "Age": [age],
        "Sex": [encoders["Sex"].transform([sex])[0]],
        "Job": [job],
        "Housing": [encoders["Housing"].transform([housing])[0]],
        "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
        "Checking account": [encoders["Checking account"].transform([checking_account])[0]],
        "Credit amount": [credit_amount],
        "Duration": [duration]
    })

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.markdown(
            '<div class="result-good">✅ Predicted Credit Risk: GOOD</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-bad">⚠️ Predicted Credit Risk: BAD</div>',
            unsafe_allow_html=True
        )