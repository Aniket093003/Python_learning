import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number: ", value=0)
num2 = st.number_input("Enter second number: ", value=0)

calculate = st.selectbox("Select Operator", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if calculate == "Add":
        result = num1 + num2
    if calculate == "Subtract":
        result = num1 - num2
    if calculate == "Multiply":
        result = num1 * num2
    if calculate == "Divide":
        result = num1 / num2

st.success(f"Result: {result}")

