import streamlit as st
import joblib

model = joblib.load("linear_regression_model.pkl")
st.title("enter model")
st.write("enter prediction mdoel")
feature_value = st.number_input("enter value",min_value=0,max_value=100)
if st.button("[redit"):
	prediction = model.predict([[feature_value]])
	st.write(f"The prediction is {prediction[0]:.2f}")
