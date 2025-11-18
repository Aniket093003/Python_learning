import streamlit as st
from PIL import Image

st.header("Ques1")

st.title("Hello python")

name = st.text_input("Enter your name", "Type here...")
st.text(f"Hello,{name}")

st.header("Ques2")
number = st.slider("Choose a number 1-100", min_value=1 , max_value=100)

st.text(f"Square of the number is: {number ** 2} ")

st.header("Ques3")


uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


image = Image.open(uploaded_file)
st.image(image, caption="Uploaded Image")

if st.button("ballons"):
    st.balloons()