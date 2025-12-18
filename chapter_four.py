import streamlit as st 
import pandas as pd

st.title("Chai sales dashboard")
file = st.file_uploader("Uplod you csv file",type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Sales Summary")
    st.write(df.describe())
    
if file:
    embarked = df["Embarked"].unique()
    selected_embarked = st.selectbox("Select Embarked", embarked)
    df_filtered = df[df["Embarked"] == selected_embarked]
    st.subheader(f"Data for Embarked: {selected_embarked}") 
    st.dataframe(df_filtered)
    

    