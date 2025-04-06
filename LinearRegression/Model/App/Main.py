import streamlit as st
from src.utils import predict,get_user_input

st.image('LinearRegression/Model/App/Images/Icon.png', use_container_width=True)

# Title of the web app (English and Arabic)
st.title("Real Estate Price Prediction / التنبؤ بسعر العقار")

# Collect input data from user
st.subheader("Enter the property details: / أدخل تفاصيل العقار:")

user_input = get_user_input()

# Make a prediction based on user input
prediction = predict(user_input)  # Replace `predict()` with your actual prediction method

# Display the result (English and Arabic)
st.write(f"The estimated price of this property is: ${prediction[0]:,.2f} ")
st.write(f"السعر التقديري لهذا العقار هو: ${prediction[0]:,.2f}")
