
import streamlit as st
import pandas as pd
import pickle

# ---------------- CONFIGURATION ----------------

st.set_page_config(
    page_title="HealthAI | Diabetes Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD MODEL ----------------

with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background: #f4f7fb;
    color: #172b4d;
}

[data-testid="stAppViewContainer"] {
    background: #f4f7fb;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hide default header */
header {
    background: transparent !important;
}

/* All text */
html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
}

h1, h2, h3, p, label {
    color: #183153;
}

/* Hero section */
.hero {
    background: linear-gradient(120deg, #102d50, #176b87);
    padding: 38px;
    border-radius: 22px;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(16,45,80,0.12);
}

.hero-tag {
    color: #75e0d0 !important;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero h1 {
    color: white !important;
    font-size: 36px;
    font-weight: 800;
    margin: 12px 0;
}

.hero p {
    color: #d9e9f5 !important;
    font-size: 16px;
}

/* Section headings */
.section-heading {
    font-size: 23px;
    font-weight: 750;
    color: #17365d;
    margin-bottom: 5px;
}

.section-description {
    color: #718096 !important;
    font-size: 14px;
    margin-bottom: 22px;
}

/* Form card */
[data-testid="stForm"] {
    background: #ffffff !important;
    border: 1px solid #e2eaf2 !important;
    border-radius: 18px !important;
    padding: 28px !important;
    box-shadow: 0 5px 20px rgba(20,50,80,0.05);
}

/* Input labels */
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label,
.stNumberInput label,
.stSelectbox label {
    color: #344b67 !important;
    font-weight: 650 !important;
    font-size: 14px !important;
}

/* Input fields */
[data-testid="stNumberInput"] input {
    background: #f8fafc !important;
    color: #172b4d !important;
    border: 1px solid #d8e2ed !important;
    border-radius: 9px !important;
    height: 44px !important;
    color-scheme: light !important;
}

[data-testid="stNumberInput"] button {
    background: #edf3f8 !important;
    color: #183153 !important;
    border: none !important;
}

[data-testid="stNumberInput"] input:focus {
    border: 1px solid #168b91 !important;
    box-shadow: 0 0 0 2px rgba(22,139,145,0.12) !important;
}

/* Prediction button */
[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(100deg, #117c83, #159e9a) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px !important;
    font-weight: 750 !important;
    font-size: 16px !important;
    width: 100% !important;
    transition: 0.3s ease;
}

[data-testid="stFormSubmitButton"] button:hover {
    background: #106b72 !important;
    transform: translateY(-2px);
}

/* Result cards */
.result {
    background: white;
    border-radius: 18px;
    padding: 28px;
    margin-top: 20px;
    text-align: center;
    border: 1px solid #e2eaf2;
    box-shadow: 0 5px 20px rgba(20,50,80,0.06);
}

.result h2 {
    font-size: 27px;
    margin-bottom: 10px;
}

.result p {
    color: #64748b !important;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px 10px;
    color: #8291a5;
    font-size: 13px;
}

hr {
    border-color: #e1e8f0 !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HERO SECTION ----------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">HEALTHCARE • ARTIFICIAL INTELLIGENCE</div>
    <h1>🩺 HealthAI</h1>
    <p style="font-size:21px; font-weight:600;">
        Diabetes Prediction System
    </p>
    <p>
        Intelligent health analysis powered by Machine Learning.
        Enter patient health parameters to generate a model prediction.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- PATIENT INFORMATION ----------------

st.markdown("""
<div class="section-heading">👤 Patient Information</div>
<div class="section-description">
Enter the patient's health details below.
</div>
""", unsafe_allow_html=True)


with st.form("patient_form"):

    st.markdown("### Personal & Medical Details")
    st.caption("All fields are required for prediction.")

    col1, col2 = st.columns(2, gap="large")

    with col1:

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=1
        )

        glucose = st.number_input(
            "Glucose Level (mg/dL)",
            min_value=0,
            max_value=300,
            value=100
        )

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

    with col2:

        insulin = st.number_input(
            "Insulin Level (mu U/ml)",
            min_value=0,
            max_value=900,
            value=80
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=70.0,
            value=25.7,
            step=0.1
        )

        diabetes_pedigree = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0,
            max_value=3.0,
            value=0.5,
            step=0.01
        )

        age = st.number_input(
            "Age (years)",
            min_value=1,
            max_value=120,
            value=25
        )

    st.markdown("---")

    submitted = st.form_submit_button(
        "🔍  ANALYZE PATIENT",
        use_container_width=True
    )


# ---------------- PREDICTION ----------------

if submitted:

    if glucose == 0 or blood_pressure == 0 or bmi == 0:
        st.warning(
            "Please enter non-zero values for glucose, "
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

        st.markdown("---")
        st.markdown("""
        <div class="section-heading">📊 Prediction Report</div>
        <div class="section-description">
        Machine learning classification result
        </div>
        """, unsafe_allow_html=True)

        if prediction == 0:

            st.markdown("""
            <div class="result">
                <h2 style="color:#15966b;">
                    ✓ No Diabetes Predicted
                </h2>
                <p>
                The model classified this patient
                into the non-diabetic category.
                </p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result">
                <h2 style="color:#dc5555;">
                    ⚠ Diabetes Predicted
                </h2>
                <p>
                The model classified this patient
                into the diabetic category.
                </p>
            </div>
            """, unsafe_allow_html=True)

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(patient)[0]

            confidence = probabilities[
                list(model.classes_).index(prediction)
            ] * 100

            st.metric(
                "Model Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.caption(
                "This is the model's estimated probability for "
                "its predicted class, not a clinical risk score."
            )

        st.warning(
            "Educational use only. This prediction is not a "
            "medical diagnosis. Please consult a qualified "
            "healthcare professional for medical advice."
        )


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    <hr>
    <b>HealthAI | Diabetes Prediction System</b>
    <br><br>
    Built with Python • Streamlit • Scikit-learn
    <br>
    Machine Learning Project
</div>
""", unsafe_allow_html=True)
