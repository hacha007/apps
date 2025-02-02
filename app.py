
import streamlit as st

# Title
st.title("My First Streamlit App 🚀")

# Header/Subheader
st.header("Welcome!")
st.subheader("Let's explore Streamlit components")

# Text input
name = st.text_input("Enter your name:", "John Doe")

# Slider
age = st.slider("Select your age:", 0, 100, 25)

# Button
if st.button("Click Me!"):
    st.balloons()  # Show celebration balloons
    st.write(f"Hello {name}! You're {age} years old.")

# Display dynamic output
st.write(f"### Your name: {name}")
st.write(f"### Your age: {age}")

# Checkbox
if st.checkbox("Show/Hide Secret Message"):
    st.success("You discovered the secret! 🎉")

# Selectbox
favorite_color = st.selectbox(
    "Choose your favorite color:",
    ["Red", "Green", "Blue", "Yellow"]
)
st.write(f"Your favorite color: {favorite_color}")