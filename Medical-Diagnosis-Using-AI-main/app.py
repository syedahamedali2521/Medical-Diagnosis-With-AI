import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(135, 206, 235, 0.75);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# FIXED: Correct Model Paths (Works on Streamlit Cloud)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

models = {
    'diabetes': pickle.load(open(os.path.join(BASE_DIR, 'Models/diabetes_model.sav'), 'rb')),
    'heart_disease': pickle.load(open(os.path.join(BASE_DIR, 'Models/heart_disease_model.sav'), 'rb')),
    'parkinsons': pickle.load(open(os.path.join(BASE_DIR, 'Models/parkinsons_model.sav'), 'rb')),
    'lung_cancer': pickle.load(open(os.path.join(BASE_DIR, 'Models/lungs_disease_model.sav'), 'rb')),
    'thyroid': pickle.load(open(os.path.join(BASE_DIR, 'Models/Thyroid_model.sav'), 'rb'))
}

# Create a dropdown menu for disease prediction
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Hypo-Thyroid Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    if st.button('Diabetes Test Result'):
        result = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        st.success("The person is diabetic" if result[0] == 1 else "The person is not diabetic")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex', 'sex', 'number')
    cp = display_input('Chest Pain types (0–3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120mg/dl (1=yes)', 'Enter FBS', 'fbs', 'number')
    restecg = display_input('Resting ECG (0–2)', 'Enter ECG result', 'restecg', 'number')
    thalach = display_input('Max Heart Rate', 'Enter Max HR', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1=yes)', 'Enter EXANG', 'exang', 'number')
    oldpeak = display_input('Oldpeak', 'Enter oldpeak', 'oldpeak', 'number')
    slope = display_input('Slope (0–2)', 'Enter slope', 'slope', 'number')
    ca = display_input('Major Vessels (0–3)', 'Enter CA value', 'ca', 'number')
    thal = display_input('Thal (0–2)', 'Enter Thal value', 'thal', 'number')

    if st.button('Heart Disease Test Result'):
        result = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        st.success("The person has heart disease" if result[0] == 1 else "The person does not have heart disease")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details:")

    fo = display_input('MDVP:Fo(Hz)', '', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', '', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', '', 'flo', 'number')
    Jitter_percent = display_input('Jitter(%)', '', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('Jitter(Abs)', '', 'Jitter_Abs', 'number')
    RAP = display_input('RAP', '', 'RAP', 'number')
    PPQ = display_input('PPQ', '', 'PPQ', 'number')
    DDP = display_input('DDP', '', 'DDP', 'number')
    Shimmer = display_input('Shimmer', '', 'Shimmer', 'number')
    Shimmer_dB = display_input('Shimmer(dB)', '', 'Shimmer_dB', 'number')
    APQ3 = display_input('APQ3', '', 'APQ3', 'number')
    APQ5 = display_input('APQ5', '', 'APQ5', 'number')
    APQ = display_input('APQ', '', 'APQ', 'number')
    DDA = display_input('DDA', '', 'DDA', 'number')
    NHR = display_input('NHR', '', 'NHR', 'number')
    HNR = display_input('HNR', '', 'HNR', 'number')
    RPDE = display_input('RPDE', '', 'RPDE', 'number')
    DFA = display_input('DFA', '', 'DFA', 'number')
    spread1 = display_input('Spread1', '', 'spread1', 'number')
    spread2 = display_input('Spread2', '', 'spread2', 'number')
    D2 = display_input('D2', '', 'D2', 'number')
    PPE = display_input('PPE', '', 'PPE', 'number')

    if st.button("Parkinson's Test Result"):
        result = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        st.success("The person has Parkinson's disease" if result[0] == 1 else "The person does not have Parkinson's disease")

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details:")

    GENDER = display_input('Gender (1 Male, 0 Female)', '', 'GENDER', 'number')
    AGE = display_input('Age', '', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 Yes)', '', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 Yes)', '', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 Yes)', '', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 Yes)', '', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 Yes)', '', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 Yes)', '', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 Yes)', '', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 Yes)', '', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 Yes)', '', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 Yes)', '', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 Yes)', '', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 Yes)', '', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 Yes)', '', 'CHEST_PAIN', 'number')

    if st.button("Lung Cancer Test Result"):
        result = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        st.success("The person has lung cancer" if result[0] == 1 else "The person does not have lung cancer")

# Thyroid Prediction
if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid")
    st.write("Enter the following details:")

    age = display_input('Age', '', 'age', 'number')
    sex = display_input('Sex (1 Male)', '', 'sex', 'number')
    on_thyroxine = display_input('On Thyroxine (1 Yes)', '', 'on_thyroxine', 'number')
    tsh = display_input('TSH Level', '', 'tsh', 'number')
    t3_measured = display_input('T3 Measured (1 Yes)', '', 't3_measured', 'number')
    t3 = display_input('T3 Level', '', 't3', 'number')
    tt4 = display_input('TT4 Level', '', 'tt4', 'number')

    if st.button("Thyroid Test Result"):
        result = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        st.success("The person has Hypo-Thyroid" if result[0] == 1 else "The person does not have Hypo-Thyroid")
