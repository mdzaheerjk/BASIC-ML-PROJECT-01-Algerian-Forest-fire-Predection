import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
st.title("Algerian Forest Fire Predection")

linear_model=pickle.load(open('models/linear.pkl','rb'))
scaler_model=pickle.load(open('models/scaler.pkl','rb'))


temperature=st.number_input("Temperature")
RH=st.number_input('RH')
Ws=st.number_input('Ws')
Rain=st.number_input('Rain')
FFMC=st.number_input('FFMC')
DMC=st.number_input('DMC')
ISI=st.number_input('ISI')
claas=st.number_input('Claas')
Region=st.number_input('Region')


new_data_scaled=scaler_model.transform([[temperature,RH,Ws,Rain,FFMC,DMC,ISI,claas,Region]])
result=linear_model.predict(new_data_scaled)


st.subheader(f"Predection is :{result}")