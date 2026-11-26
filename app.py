
import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Diabetes Prediction | HealthCare AI",
    page_icon="🩺",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background: #f3f6fb;
    color: #172b4d;
}

header {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1150px;
}

.hero {
    background: linear-gradient(120deg, #102a56, #1769aa);
    padding: 38px;
    border-radius: 20px;
    color: white;
    margin-bottom: 28px;
}

.hero h1 {
    color: white;
    font-size: 36px;
    margin-bottom: 8px;
}

.hero p {
    color: #dcecff;
    font-size: 16px;
}

.section-card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #e3eaf3;
    margin-bottom: 20px;
}

.section-title {
    color: #12345a;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 20px;
}

div.stButton > button {
    background: linear-gradient(90deg, #1769aa, #2185d0);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 13px;
    font-weight: 700;
    width: 100%;
    transition: 0.3s;
}

div.stButton > button:hover {
    background: #104d83;
    color: white;
    border: none;
}

.result-card {
    padding: 25px;
    border-radius: 16px;
    background: white;
    border: 1px solid #dce5f0;
    text-align: center;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #8291a5;
    font-size: 13px;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>🩺 Diabetes Prediction System</h1>
    <p>AI-powered health analysis using Machine Learning</p>
    <p>Enter patient information to generate a diabetes prediction.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------

st.markdown("""
<div class="section-card">
    <div class="section-title">👤 Patient Information</div>
    <div class="section-subtitle">
        Provide accurate patient details for prediction.
    </div>
</div>
""", unsafe_allow_html=True)

with st.form("diabetes_form"):

    st.subheader("Personal Details")

    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input(
            "Number of Pregnancies",
            min_value=0,
            max_value=20,
            value=1
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=25
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=70.0,
            value=25.7
        )

        glucose = st.number_input(
            "Glucose Level (mg/dL)",
            min_value=0,
            max_value=300,
            value=100
        )

    with col2:
        blood_pressure = st.number_input(
            "Blood Pressure (mm Hg)",
            min_value=0,
            max_value=200,
            value=70
        )

        skin_thickness = st.number_input(
            "Skin Thickness (mm)",
            min_value=0,
            max_value=100,
            value=20
        )

        insulin = st.number_input(
            "Insulin Level (mu U/ml)",
            min_value=0,
            max_value=900,
            value=80
        )

        diabetes_pedigree = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0,
            max_value=3.0,
            value=0.5
        )

    st.markdown("---")

    submitted = st.form_submit_button(
        "🔍 Predict Diabetes",
        use_container_width=True
    )

# ---------------- PREDICTION ----------------

if submitted:

    if glucose == 0 or blood_pressure == 0 or bmi == 0:
        st.warning(
            "Please enter valid non-zero values for glucose, "
            "blood pressure and BMI."
        )

    else:

        patient = pd.DataFrame({
            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin],
            "BMI": [bmi],
            "DiabetesPedigreeFunction": [diabetes_pedigree],
            "Age": [age]
        })

        prediction = model.predict(patient)[0]

        st.markdown("## 📊 Prediction Results")

        if prediction == 0:

            st.markdown("""
            <div class="result-card">
                <h2 style="color:#16865c;">
                    ✅ No Diabetes Predicted
                </h2>
                <p style="color:#64748b;">
                    The model classified this patient as
                    belonging to the non-diabetic category.
                </p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-card">
                <h2 style="color:#d94848;">
                    ⚠️ Diabetes Predicted
                </h2>
                <p style="color:#64748b;">
                    The model classified this patient as
                    belonging to the diabetic category.
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Model probability
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(patient)[0]
            confidence = probabilities[list(model.classes_).index(prediction)] * 100

            st.metric(
                "Model Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.caption(
                "This is the model's estimated probability for its "
                "predicted class, not a clinical risk score."
            )

        st.warning(
            "This application is for educational purposes only. "
            "It cannot diagnose diabetes or replace medical advice. "
            "Please consult a qualified healthcare professional."
        )

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    <hr>
    <p>HealthCare AI | Diabetes Prediction System</p>
    <p>Powered by Python, Scikit-learn and Streamlit</p>
</div>
""", unsafe_allow_html=True)
