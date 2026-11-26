# 🩺 HealthAI – Diabetes Prediction System

### AI-Powered Diabetes Prediction Using Machine Learning

An interactive Machine Learning web application that predicts the possibility of diabetes based on patient health parameters. Built using Python, Scikit-learn and Streamlit, this project provides an easy-to-use interface for generating real-time predictions.

<p align="center">
  <a href="https://diabetes-prediction-app-007.streamlit.app/">
    <strong>🚀 LIVE DEMO – Try HealthAI</strong>
  </a>
</p>

---

## 📌 Project Overview

HealthAI is a Machine Learning-based diabetes prediction application that analyzes patient health information and classifies the possibility of diabetes.

The application uses a **Decision Tree Classifier** trained on medical diagnostic features. Users can enter patient information through an interactive web interface and receive an instant prediction.

The project demonstrates the complete Machine Learning workflow, from data preprocessing and exploratory data analysis to model training, evaluation and deployment.

## ✨ Features

- 🩺 **Diabetes Prediction:** Predicts diabetes using a trained Decision Tree model.
- 👤 **Patient Information:** Accepts eight different health parameters.
- ⚡ **Real-Time Results:** Generates predictions instantly.
- 📊 **Prediction Confidence:** Displays the model's estimated probability for its predicted class.
- 🎨 **Modern Interface:** Clean and responsive healthcare-themed Streamlit design.
- ☁️ **Cloud Deployment:** Accessible online through Streamlit Community Cloud.

## 🧠 Machine Learning Workflow

The project follows these steps:

1. **Data Collection:** Load the diabetes dataset using Pandas.
2. **Data Exploration:** Examine dataset structure, statistical information and feature distributions.
3. **Data Preprocessing:**
   - Identify invalid zero values in selected medical columns.
   - Replace invalid zeros with missing values.
   - Handle missing values using mean or median based on feature skewness.
4. **Data Visualization:** Generate histograms to understand numerical feature distributions.
5. **Train-Test Split:** Split the dataset into 80% training and 20% testing data using stratification.
6. **Model Training:** Train a Decision Tree Classifier with maximum depth of 4 and balanced class weights.
7. **Model Evaluation:** Evaluate the model using accuracy, confusion matrix and classification report.
8. **Deployment:** Save the trained model using Pickle and deploy it through Streamlit.

## 🔬 Input Features

The model uses the following eight features:

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Glucose concentration |
| BloodPressure | Blood pressure measurement |
| SkinThickness | Skin thickness measurement |
| Insulin | Insulin level |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Patient's age |

**Target Variable:**
- `0` – No Diabetes Predicted
- `1` – Diabetes Predicted

## 🤖 Machine Learning Model

**Algorithm:** Decision Tree Classifier

Model configuration:

- Maximum Depth: 4
- Class Weight: Balanced
- Random State: 42
- Train-Test Ratio: 80:20
- Stratified Sampling: Enabled

The model is evaluated using:
- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1-Score

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine Learning |
| Pickle | Model serialization |
| Streamlit | Web application development |
| Google Colab | Model development |
| GitHub | Version control and project hosting |
| Streamlit Community Cloud | Application deployment |

## 📂 Project Structure

```text
diabetes-prediction-app/
│
├── app.py                  # Streamlit web application
├── diabetes_model.pkl      # Trained Decision Tree model
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## ⚙️ Installation and Setup

Follow these steps to run the application locally.

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd diabetes-prediction-app
```

**3. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application**

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🌐 Live Application

Try the deployed application here:

🔗 https://diabetes-prediction-app-007.streamlit.app/

The application allows users to enter patient health information and obtain an instant Machine Learning prediction.

## 🚀 Future Improvements

- Add patient prediction history.
- Generate downloadable PDF prediction reports.
- Implement interactive health analytics and visualizations.
- Improve model performance through hyperparameter tuning.
- Compare Decision Tree with Random Forest and Logistic Regression.
- Add more advanced model explainability features.

## ⚠️ Disclaimer

This project is developed for educational and demonstration purposes only. Its predictions are generated by a Machine Learning model and must not be considered medical diagnoses or professional medical advice. Always consult a qualified healthcare professional for medical decisions.

## 👨‍💻 Author

**Sarveswaran S.**

B.E. Artificial Intelligence and Machine Learning Student

Interested in Machine Learning, Python Development and Full-Stack Development.

---

⭐ If you find this project interesting, consider giving this repository a star!
