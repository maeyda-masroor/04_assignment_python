import streamlit as st
import pandas as pd

st.title("BMI calculator")
height = st.slider("Enter height in cm",100,250,175)
weight = st.slider("Enter weight",40,200,70)

bmi = float(weight / ((height/100)**2))
st.write('you bmi is'+str(bmi))
st.write("BMI category")
st.write("underweight BMI less than 18.5")
st.write("normal weight 18 and 25")
st.write("overwiegth 25 and 29.99")
st.write("obseity 30 and above")

