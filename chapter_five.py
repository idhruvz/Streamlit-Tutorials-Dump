import streamlit as st 
import requests

st.title("Live currecy converter")
amount = st.number_input("Enter the amount in INR",min_value=1)
target_currency = st.selectbox("Convert to",["USD","EUR","GBP","JPY","AUD","CAD"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][target_currency]
    converted_amount = amount * rate
    st.success(f"{amount} INR is equal to {converted_amount:.2f} {target_currency}")
