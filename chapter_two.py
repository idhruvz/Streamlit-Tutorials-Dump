import streamlit as st 
st.title("Chai maker app")

if st.button("Brew Chai"):
    st.success("Your chai is being brewed! ☕️")
    
add_sugar = st.checkbox("Add sugar", value=True)

if add_sugar:
    st.write("Sugar will be added to your chai.")
    
tea_type = st.radio("Select tea type", ["Black Tea", "Green Tea", "Herbal Tea"])
st.write(f"You selected {tea_type}.")
flavour = st.selectbox("Choose a flavour", ["Masala", "Ginger", "Cardamom", "Tulsi", "Lemon"]) 
st.write(f"You chose {flavour} flavour.")

milk_amount = st.slider("Select milk amount (ml)", 0, 200, 100)
st.write(f"Milk amount set to {milk_amount} ml.")

brew_time = st.number_input("Set brewing time (minutes)", min_value=1, max_value=10, value=5)
st.write(f"Brewing time set to {brew_time} minutes.")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}, your chai will be ready soon!")
    

