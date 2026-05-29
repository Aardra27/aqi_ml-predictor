
import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AQI Predictor",
    page_icon="🌍",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("best_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stNumberInput label {
    color: white !important;
    font-weight: 600;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 12px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg,#0072ff,#00c6ff);
}

.metric-card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    color: white;
    margin-top: 20px;
}

.small-text {
    color: #cbd5e1;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
# 🌍 Air Quality Index Predictor
### Predict AQI using Machine Learning models
""")

st.markdown(
    "<p class='small-text'>Built with Streamlit, Scikit-learn, and Machine Learning regression models.</p>",
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📘 About")

st.sidebar.info("""
This project predicts AQI using trained Machine Learning models.

Models used:
- Linear Regression
- Random Forest
- AdaBoost
- Gradient Boosting
- KNN
""")

st.sidebar.success("Developed by Aardra")

# =========================
# INPUT SECTION
# =========================
st.markdown("## 📥 Enter Pollutant Values")

cols = st.columns(2)

user_input = {}

for i, feature in enumerate(feature_cols):

    with cols[i % 2]:

        value = st.number_input(
            f"{feature}",
            min_value=0.0,
            value=5.0,
            step=0.1
        )

        user_input[feature] = value

# =========================
# PREDICT BUTTON
# =========================
input_df = pd.DataFrame([user_input])

if st.button("🚀 Predict AQI"):

    prediction = model.predict(input_df)[0]

    # AQI Classification
    if prediction <= 50:
        category = "🟢 Good"
        color = "#22c55e"

    elif prediction <= 100:
        category = "🟡 Moderate"
        color = "#eab308"

    elif prediction <= 150:
        category = "🟠 Unhealthy for Sensitive Groups"
        color = "#f97316"

    elif prediction <= 200:
        category = "🔴 Unhealthy"
        color = "#ef4444"

    elif prediction <= 300:
        category = "🟣 Very Unhealthy"
        color = "#a855f7"

    else:
        category = "⚫ Hazardous"
        color = "#111827"

    # AQI NUMBER CARD
    st.markdown(f"""
    <div class="metric-card">
        <h2>Predicted AQI</h2>
        <h1 style="font-size:60px;">{prediction:.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

    # AQI STATUS BOX
    st.markdown(f"""
    <div class="result-box" style="background-color:{color};">
        {category}
    </div>
    """, unsafe_allow_html=True)

    st.success("Prediction completed successfully.")

else:
    st.info("Enter pollutant values and click Predict AQI.")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<center>🌱 Machine Learning based AQI Prediction System</center>",
    unsafe_allow_html=True
)

