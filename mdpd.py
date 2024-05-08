# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:27:36 2024

@author: mahen
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Health Prediction App",
                   layout="wide",
                   page_icon="❤‍🩹")

#loading the saved models 
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))
#brestcancer_model =pickle.load(open('/Users/lakshyabhardwaj/Downloads/multiple-disease-prediction-streamlit-app-main/dataset/breastcancer.csv','rb'))

 


# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "serif"


# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("https://www.example.com/image.jpg");
#     }
#    </style>
#     """,
#     unsafe_allow_html=True
# )
# sidebar for navigation 
with st.sidebar:
    selected = option_menu('Health Prediction App',
                           ['Diabetes(मधुमेह) Prediction',
                            'Heart Disease(हृदय रोग) Prediction',
                            'Parkinsons(पार्किंसंस रोग) Prediction',
                            # 'BreastCancer Prediction'
                            ],
                             menu_icon='person-check-fill',
                            icons=['bi bi-thermometer-half', 'heart-pulse', 'bi bi-eye',
                                #    'yin-yang'
                                   ],
                            default_index=0)
with st.popover("Add Name(नाम)"):
    st.markdown("Hello 👋")
    name = st.text_input("What's your name? आपका नाम क्या है?")

st.write("Hello नमस्ते",name)

# Diabetes Prediction Page
if selected == 'Diabetes(मधुमेह) Prediction':
    # page title
    st.title('Diabetes(मधुमेह) Prediction')
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies ( गर्भावस्था की संख्या)', min_value=0, step=1)
        Glucose = st.number_input('Glucose Level(रक्त शर्करा)', min_value=0, step=1)
        BloodPressure = st.number_input('Blood Pressure(रक्तचाप)', min_value=0, step=1)
        SkinThickness = st.number_input('Skin Thickness(त्वचा की मोटाई)', min_value=0, step=1)
    with col2:
        Insulin = st.number_input('Insulin Level(इंसुलिन स्तर)', min_value=0, step=1)
        BMI = st.number_input('BMI(बीएमआई)', min_value=0.0, step=0.1)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, step=0.1)
        Age = st.number_input('Age(आयु)', min_value=0, step=1)

    # code for Prediction
    diab_diagnosis = ''
    bpnow = ''
    insuli =''
    glnow=''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        if ( BloodPressure >= 160 ): 
            bpnow = 'Your Blood pressure is high\n'
        else:
            bpnow='Your Blood pressure is Normal\n' 
        if ( Insulin >= 270 ): 
           insuli = 'Your Insulin is high\n'
        else:
            insuli='Your Insulin is Normal\n'
        if ( Glucose >= 160 ): 
            glnow = 'Your Glucose is high\n'
        else:
           glnow='Your Glucose is Normal\n' 
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
    st.success(diab_diagnosis)
    st.success(bpnow)
    st.success(insuli)
    st.success(glnow)

# Heart Disease Prediction Page
if selected == 'Heart Disease(हृदय रोग) Prediction':
    # page title
    st.title('Heart Disease(हृदय रोग) Prediction')
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input('Age(आयु)', min_value=0, step=1)
        sex = st.number_input('Sex(लिंग) (0 = female(महिला), 1 = male(पुरुष))', min_value=0, max_value=1, step=1)
        cp = st.number_input('Chest Pain Type(सीने का दर्द)', min_value=0, step=1)
        trestbps = st.number_input('Resting Blood Pressure(रक्तचाप)', min_value=0, step=1)
        chol = st.number_input('Serum Cholestoral (कोलेस्ट्रॉल)in mg/dl', min_value=0, step=1)
        fbs = st.number_input('Fasting Blood Sugar(रक्त शर्करा) > 120 mg/dl', min_value=0, max_value=1, step=1)
    with col2:
        restecg = st.number_input('Resting Electrocardiographic Results(इलेक्ट्रोकार्डियोग्राफ़िक परिणाम)', min_value=0, step=1)
        thalach = st.number_input('Maximum Heart Rate Achieved(अधिकतम हृदय गति)', min_value=0, step=1)
        exang = st.number_input('Exercise Induced Angina(एनजाइना)', min_value=0, max_value=1, step=1)
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, step=0.1)
        slope = st.number_input('Slope of the Peak Exercise ST Segment(ST रेखा की प्रवणता)', min_value=0, step=1)
        ca = st.number_input('Major Vessels Colored by Flourosopy (प्रतिदीप्तिदर्शन में रंगी नस)', min_value=0, step=1)
        thal = st.number_input('Thal (थैलेसीमिया)(0 = normal; 1 = fixed defect; 2 = reversable defect)', min_value=0, max_value=2, step=1)

    # code for Prediction
    heart_diagnosis = ''
    bpnow = ''

    if st.button('Heart Disease Test Result'):
        
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        heart_prediction = heart_disease_model.predict([user_input])
        if ( restecg >= 160 ): 
            bpnow = 'Your Blood pressure is high\n'
        else:
            bpnow='Your Blood pressure is Normal\n'  
        if (heart_prediction[0] == 1 ):
            heart_diagnosis = 'The person is having heart disease\n '
        else :
            heart_diagnosis='The person does not have any heart disease\n'
            
        
    st.success(heart_diagnosis)
    st.success(bpnow)

# Parkinson's Prediction Page
if selected == "Parkinsons(पार्किंसंस रोग) Prediction":
    # page title
    st.title("Parkinson's Disease(पार्किंसंस रोग) Prediction")
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    with col1:
        fo = st.number_input('MDVP:  Fo(Hz)', step=0.1)
        fhi = st.number_input('MDVP:  Fhi(Hz)', step=0.1)
        flo = st.number_input('MDVP:  Flo(Hz)', step=0.1)
        Jitter_percent = st.number_input('MDVP:  Jitter(%)', step=0.1)
        Jitter_Abs = st.number_input('MDVP:  Jitter(Abs)', step=0.1)
        RAP = st.number_input('MDVP:  RAP', step=0.1)
        PPQ = st.number_input('MDVP:  PPQ', step=0.1)
        NHR = st.number_input('NHR', step=0.1)
        HNR = st.number_input('HNR', step=0.1)
        RPDE = st.number_input('RPDE', step=0.1)
        D2 = st.number_input('D2', step=0.1)
    with col2:
        DDP = st.number_input('Jitter:  DDP', step=0.1)
        Shimmer = st.number_input('MDVP:  Shimmer', step=0.1)
        Shimmer_dB = st.number_input('MDVP:  Shimmer(dB)', step=0.1)
        APQ3 = st.number_input('Shimmer:  APQ3', step=0.1)
        APQ5 = st.number_input('Shimmer:  APQ5', step=0.1)
        APQ = st.number_input('MDVP:  APQ', step=0.1)
        DDA = st.number_input('Shimmer:  DDA', step=0.1)
       
        DFA = st.number_input('DFA', step=0.1)
        spread1 = st.number_input('spread1', step=0.1)
        spread2 = st.number_input('spread2', step=0.1)
        PPE = st.number_input('PPE', step=0.1)

    # code for Prediction
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                      APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2,D2, PPE]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)