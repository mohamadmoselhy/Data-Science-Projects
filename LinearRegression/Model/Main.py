import streamlit as st
from src.utils import *



# Assuming your model and prediction function are already available
# For example: from your_model_file import model, predict_function

# Title of the web app
st.title("Real Estate Price Prediction")

# Collect input data from user
st.subheader("Enter the property details:")

# Create inputs for all required features
bedrooms = st.number_input("Number of Bedrooms:", min_value=1, max_value=50)
bathrooms = st.number_input("Number of Bathrooms:", min_value=1, max_value=10)
sqft_living = st.number_input("Square Footage of Living Area (sqft):", min_value=200, max_value=10000)
floors = st.number_input("Number of Floors:", min_value=1, max_value=5)
waterfront = st.selectbox("Waterfront (1 = Yes, 0 = No):", [0, 1])
view = st.selectbox("View Quality (0 to 4):", [0, 1, 2, 3, 4])
condition = st.selectbox("Condition (1 to 5):", [1, 2, 3, 4, 5])
grade = st.selectbox("Grade (1 to 13):", [i for i in range(1, 14)])
yr_built = st.number_input("Year Built:", min_value=1900, max_value=2025)
sqft_lot = st.number_input("Lot Size (sqft):", min_value=500, max_value=100000)
sqft_above = st.number_input("Square Footage of Area Above Ground (sqft):", min_value=100, max_value=10000)
sqft_basement = st.number_input("Square Footage of Basement (sqft):", min_value=0, max_value=5000)


# Create the feature array for prediction
user_input = {
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'sqft_living': sqft_living,
    'floors': floors,
    'waterfront': waterfront,
    'view': view,
    'condition': condition,
    'grade': grade,
    'yr_built': yr_built,
    'sqft_lot': sqft_lot,
    'sqft_above': sqft_above,
    'sqft_basement': sqft_basement
}

# Make a prediction based on user input
# Assuming you have a prediction function (e.g., model.predict())
prediction = predict(user_input)  # Replace `predict()` with your actual prediction method

# Display the prediction result
st.subheader("Prediction Result:")
st.write(f"The estimated price for a property with the following details:")
st.write(f"- {bedrooms} bedrooms")
st.write(f"- {bathrooms} bathrooms")
st.write(f"- {sqft_living} sqft of living area")
st.write(f"- {floors} floors")
st.write(f"- Waterfront: {'Yes' if waterfront == 1 else 'No'}")
st.write(f"- View Quality: {view}")
st.write(f"- Condition: {condition}")
st.write(f"- Grade: {grade}")
st.write(f"- Built in {yr_built}")
st.write(f"- Lot Size: {sqft_lot} sqft")
st.write(f"- {sqft_above} sqft of area above ground")
st.write(f"- {sqft_basement} sqft of basement")

st.write(f"The estimated price of this property is: ${prediction[0]:,.2f}")
