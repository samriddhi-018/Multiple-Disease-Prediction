import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️",
                   )

# loading the saved models
diabetes_model = pickle.load(open('C:/Users/Sankrishna Goyal/PycharmProjects/Multiple Diseases Prediction/saved_models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/Sankrishna Goyal/PycharmProjects/Multiple Diseases Prediction/saved_models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/Sankrishna Goyal/PycharmProjects/Multiple Diseases Prediction/saved_models/parkinsons_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    components.html(""" <script src="https://cdn.botpress.cloud/webchat/v1/inject.js"></script>
        <script src="https://mediafiles.botpress.cloud/c0f6cf31-4d6f-4461-85e7-b8d944d722ee/webchat/config.js" defer></script>""",
                    height=350, )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0)

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0)

    with col3:
        BMI = st.number_input('BMI value', min_value=0)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0)

    with col2:
        Age = st.number_input('Age of the Person', min_value=0)

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)



# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=0)

    with col2:
        sex = st.number_input('Sex(if male enter 1 otherwise 0)', min_value=0, max_value=1, step=1)

    with col3:
        cp = st.number_input('Chest Pain types(normal-1, excess-2, abnormal-3)', min_value=0, max_value=3, step=1)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure(b/w 80 & 160)', min_value=0)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl(b/w 150-450)', min_value=0)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1, step=1)

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (Normal-0, Abnormal-1)', min_value=0, max_value=2, step=1)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved(b/w 130-250)', min_value=0)

    with col3:
        exang = st.number_input('Exercise Induced Angina(Exist-1, Not-0)', min_value=0, max_value=1, step=1)

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise(b/w 0-5)')

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1)

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=4, step=1)

    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, step=1)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz-Fo)")

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz-Fhi)')

    with col3:
        flo = st.number_input('MDVP:Flo(Hz-Flo)')

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(Jitter-%)')

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Jitter-Abs)')

    with col1:
        RAP = st.number_input('MDVP(RAP)')

    with col2:
        PPQ = st.number_input('MDVP(PPQ)')

    with col3:
        DDP = st.number_input('Jitter(DDP)')

    with col4:
        Shimmer = st.number_input('MDVP(Shimmer)')

    with col5:
        Shimmer_dB = st.number_input('MDVP Shimmer(dB)')

    with col1:
        APQ3 = st.number_input('Shimmer(APQ3)')

    with col2:
        APQ5 = st.number_input('Shimmer(APQ5)')

    with col3:
        APQ = st.number_input('MDVP(APQ)')

    with col4:
        DDA = st.number_input('Shimmer(DDA)')

    with col5:
        NHR = st.number_input('NHR')

    with col1:
        HNR = st.number_input('HNR')

    with col2:
        RPDE = st.number_input('RPDE')

    with col3:
        DFA = st.number_input('DFA')

    with col4:
        spread1 = st.number_input('spread1')

    with col5:
        spread2 = st.number_input('spread2')

    with col1:
        D2 = st.number_input('D2')

    with col2:
        PPE = st.number_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
