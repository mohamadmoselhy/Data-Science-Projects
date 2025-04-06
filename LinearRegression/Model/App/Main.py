import streamlit as st
from src.utils import predict

st.image("D:\My drive\Course\Data Science\Models Testing\Data-Science-Projects\LinearRegression\Model\App\Icon.png", use_container_width=True)

# Title of the web app (English and Arabic)
st.title("Real Estate Price Prediction / التنبؤ بسعر العقار")

# Collect input data from user
st.subheader("Enter the property details: / أدخل تفاصيل العقار:")

# Create inputs for all required features (English and Arabic)
bedrooms = st.number_input("Number of Bedrooms: / عدد الغرف:", min_value=1, max_value=50)
bathrooms = st.number_input("Number of Bathrooms: / عدد الحمامات:", min_value=1, max_value=10)
sqft_living = st.slider("Square Footage of Living Area (sqft): / مساحة المنطقة السكنية (قدم مربع):", min_value=200, max_value=10000)
floors = st.number_input("Number of Floors: / عدد الطوابق:", min_value=1, max_value=5)
waterfront = st.selectbox("Waterfront (1 = Yes, 0 = No): / بالقرب من الماء (1 = نعم، 0 = لا):", [0, 1])
view = st.selectbox("View Quality (0 to 4): / جودة الإطلالة (من 0 إلى 4):", [0, 1, 2, 3, 4])
condition = st.selectbox("Condition (1 to 5): / الحالة (من 1 إلى 5):", [1, 2, 3, 4, 5])
grade = st.selectbox("Grade (1 to 13): / الدرجة (من 1 إلى 13):", [i for i in range(1, 14)])
yr_built = st.slider("Year Built: / سنة البناء:", min_value=1900, max_value=2025)
sqft_lot = st.slider("Lot Size (sqft): / حجم الأرض (قدم مربع):", min_value=500, max_value=100000)
sqft_above = st.slider("Square Footage of Area Above Ground (sqft): / مساحة المنطقة فوق الأرض (قدم مربع):", min_value=100, max_value=10000)
sqft_basement = st.slider("Square Footage of Basement (sqft): / مساحة الطابق السفلي (قدم مربع):", min_value=0, max_value=5000)

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
prediction = predict(user_input)  # Replace `predict()` with your actual prediction method

# Display the result (English and Arabic)
st.write(f"The estimated price of this property is: ${prediction[0]:,.2f} ")
st.write(f"السعر التقديري لهذا العقار هو: ${prediction[0]:,.2f}")
