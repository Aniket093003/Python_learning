import streamlit as st

st.title("Hello GeeksForGeeks !!!")

st.header("This is a header") 
st.subheader("This is a subheader")

st.text("Hello GeeksForGeeks!!!")





chai = st.selectbox("your choice", ["", "chai", "cofee"])

st.text(f"your choice is : {chai}")