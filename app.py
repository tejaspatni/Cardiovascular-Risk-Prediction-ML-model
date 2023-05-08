#Importing Libraries

import os
import streamlit as st
import numpy as np
import pickle
from pickle import load
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Cardiovascular Disease Predictor",
                   layout="wide")

#import model
st.title("Cardiovascular Disease Predictor")
pipe=pickle.load(open("dt_classifier.pkl","rb"))
dataset=pickle.load(open("dataset.pkl","rb"))


age = st.slider(":blue[Select Your Age]",21, 80, 30 )

sex = st.radio(":blue[Select Your Gender]", ["Male", "Female"])
if sex == "Male":
    sex = 0
else:
    sex = 1


cigsPerDay = st.slider(":blue[Select no of cigs per day]",0, 50)

BPMeds = st.radio(":blue[Taking BP Medicines]", ["Yes", "No"])
if BPMeds == "Yes":
    BPMeds = 1
else:
    BPMeds = 0

prevalentStroke = st.radio(":blue[Stroke History]", ["Yes", "No"])
if prevalentStroke == "Yes":
    prevalentStroke = 1
else:
    prevalentStroke = 0

prevalentHyp = st.radio(":blue[Hypertention History]", ["Yes", "No"])
if prevalentHyp == "Yes":
    prevalentHyp = 1
else:
    prevalentHyp = 0

diabetes = st.radio(":blue[Diabetes History]", ["Yes", "No"])
if diabetes == "Yes":
    diabetes = 1
else:
    diabetes = 0



totChol = st.slider(":blue[Select Your Cholestrol Level]", 100, 540, 300)

BMI = st.slider(":blue[Select Your BMI Level]", 0, 50, 5)



heartRate = st.radio(":blue[Select Your Heart Rate]", list(range(0, 201, 25)))

glucose = st.slider(":blue[Select Your glucose Level]", 0, 300, 5)

mean_art_bp = st.slider(":blue[Select Your BP Level]", 0, 300, 5)

if st.button('Predict'):
    query_point = np.array([age, sex,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes, totChol, BMI,heartRate,glucose,mean_art_bp])
    query_point = query_point.reshape(1, -1)
    prediction = pipe.predict(query_point)
    if prediction == 0:
        st.success("You don't have a Cardiovascular Disease 😊!")

    else:
        st.error("You have a Cardiovascular Disease 😥!")

        