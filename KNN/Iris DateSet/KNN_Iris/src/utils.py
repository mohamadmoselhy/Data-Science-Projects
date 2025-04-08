import numpy as np
import joblib
import streamlit as st


def predict(user_input,ModelPath,ScalerPath):
    LinearRegMod = joblib.load(ModelPath)  # Load the trained model
    MyScaler = joblib.load(ScalerPath)  # Load the saved scaler
    # Convert dict to 2D array if needed
    input_array = np.array([list(user_input.values())])
    input_array=MyScaler.transform(input_array)
    result = LinearRegMod.predict(input_array)
    return result


def get_user_input():
    """
    Collects input data from the user in both English and Arabic.
    Returns the user input as a dictionary.
    """
    # Create inputs for all required features (English and Arabic)
    bedrooms = st.number_input("Number of Bedrooms: / عدد الغرف:", min_value=1, max_value=50)
    bathrooms = st.number_input("Number of Bathrooms: / عدد الحمامات:", min_value=1, max_value=10)
    sqft_living = st.number_input("Square Footage of Living Area (sqft): / مساحة المنطقة السكنية (قدم مربع):", min_value=200, max_value=10000)
    floors = st.number_input("Number of Floors: / عدد الطوابق:", min_value=1, max_value=5)
    waterfront = st.selectbox("Waterfront (1 = Yes, 0 = No): / بالقرب من الماء (1 = نعم، 0 = لا):", [0, 1])
    view = st.selectbox("View Quality (0 to 4): / جودة الإطلالة (من 0 إلى 4):", [0, 1, 2, 3, 4])
    condition = st.selectbox("Condition (1 to 5): / الحالة (من 1 إلى 5):", [1, 2, 3, 4, 5])
    grade = st.selectbox("Grade (1 to 13): / الدرجة (من 1 إلى 13):", [i for i in range(1, 14)])
    yr_built = st.number_input("Year Built: / سنة البناء:", min_value=1900, max_value=2025)
    Renovated = st.selectbox("Renovated (1 = Yes, 0 = No): / تم تجديده (1 = نعم، 0 = لا):", [0, 1])
    sqft_lot = st.number_input("Lot Size (sqft): / حجم الأرض (قدم مربع):", min_value=500, max_value=100000)
    sqft_above = st.number_input("Square Footage of Area Above Ground (sqft): / مساحة المنطقة فوق الأرض (قدم مربع):", min_value=100, max_value=10000)
    sqft_basement = st.number_input("Square Footage of Basement (sqft): / مساحة الطابق السفلي (قدم مربع):", min_value=0, max_value=5000)

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
        'Renovated':Renovated,
        'sqft_lot': sqft_lot,
        'sqft_above': sqft_above,
        'sqft_basement': sqft_basement
    }

    return user_input