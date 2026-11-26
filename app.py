
import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

# Application title
st.title("🩺 Diabetes Prediction System")
st.write("Enter patient details to predict the possibility of diabetes.")

st.divider()

# Patient information
st.subheader("Patient Information")

pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose Level", 0, 300, 100)
blood_pressure = st.number_input("Blood Pressure", 0, 200, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin Level", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.7)
diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function", 0.0, 3.0, 0.5
)
age = st.number_input("Age", 1, 120, 25)

st.divider()

# Prediction button
if st.button("Predict Diabetes", use_container_width=True):

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

    st.subheader("Prediction Result")

    if prediction == 0:
        st.success("Prediction: No Diabetes detected")
    else:
        st.error("Prediction: Diabetes detected")

    st.warning(
        "This is an educational machine learning prediction, "
        "not a medical diagnosis. Consult a qualified healthcare professional."
    )
  
