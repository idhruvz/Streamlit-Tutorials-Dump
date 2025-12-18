import streamlit as st 

st.title("Hello Chai App")
st.subheader("Brewed with stramlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")

chai = st.selectbox("Select your chai",["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai", "Lemon Chai"])
st.write(f"You choose {chai}. Excellent choice ")

st.success("Enjoy your cup of chai!")

