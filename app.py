import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle
st.title("Algerian Forest Fire Predection")


temperature=st.text_input("Temperature")
RH=st.text_input('RH')
Ws=st.text_input('Ws')
Rain=st.text_input('Rain')
FFMC=st.text_input('FFMC')
DMC=st.text_input('DMC')
ISI=st.text_input('ISI')

st.subheader("Predection is :")