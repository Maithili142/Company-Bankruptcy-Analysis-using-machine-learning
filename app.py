# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:20:58 2024

@author: DELL
"""

import streamlit as st
import pandas as pd
import pickle

#load trained model
#@st.cache
st.cache_data
def load_model():
   with open("C:/Users/HP/OneDrive\Desktop/Bankruptcy project/rf_model.pkl", "rb") as model_file:
     loaded_model=pickle.load(model_file)
     return loaded_model
loaded_model=load_model()
#with open("D:\Bank deployment/rf_model.pkl", "rb") as model_file:
 #   model = pickle.load(model_file)   
#streamlit app
st.title("Bankruptcy Prediction")
feature1=st.number_input("ROA(C) before interest and depreciation before interest", value=0.0)
feature2=st.number_input( "ROA(A) before interest and % after tax",value=0.0)
feature3=st.number_input("ROA(B) before interest and depreciation after tax",value=0.0)
feature4=st.number_input(" Net Value Per Share (B)",value=0.0)
feature5=st.number_input("Net Value Per Share (A)",value=0.0)
feature6=st.number_input("Persistent EPS in the Last Four Seasons",value=0.0)
feature7=st.number_input(" Per Share Net profit before tax (Yuan ¥)",value=0.0)
feature8=st.number_input( " Debt ratio %",value=0.0)
feature9=st.number_input ("Net worth/Assets",value=0.0)
feature10=st.number_input( " Borrowing dependency",value=0.0)
feature11=st.number_input( " Net profit before tax/Paid-in capital",value=0.0)
feature12=st.number_input( "Working Capital to Total Assets",value=0.0)
feature13=st.number_input("Current Liability to Assets",value=0.0)
feature14=st.number_input("Current Liabilities/Equity",value=0.0) 
feature15=st.number_input("Retained Earnings to Total Assets",value=0.0)
feature16=st.number_input("Current Liability to Equity",value=0.0)
feature17=st.number_input("Current Liability to Current Assets",value=0.0)
feature18=st.number_input(" Net Income to Total Assets", value=0.0)
feature19=st.number_input("Net Income to Stockholder's Equity",value=0.0)
feature20=st.number_input(" Liability to Equity",value=0.0)

#create button predict
if st.button('Predict'):
    input_data=[[feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,
                 feature9,feature10,feature11,feature12,feature13,feature14,feature15,
                 feature16,feature17,feature18,feature19,feature20]]

    prediction=loaded_model.predict(input_data)
    
    if prediction[0]==0:
           st.write("The company is predicted to be non bankrupt")
    else:
        st.write("The company is predicted to be bankrupt")