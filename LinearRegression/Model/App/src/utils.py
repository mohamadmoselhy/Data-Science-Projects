import numpy as np
import joblib

def predict(user_input):
    LinearRegMod = joblib.load("D:\My drive\Course\Data Science\Models Testing\Data-Science-Projects\LinearRegression\Model\model.pkl")  # Load the trained model
    MyScaler = joblib.load("D:\My drive\Course\Data Science\Models Testing\Data-Science-Projects\LinearRegression\Model\scaler.pkl")  # Load the saved scaler
    # Convert dict to 2D array if needed
    input_array = np.array([list(user_input.values())])
    input_array=MyScaler.transform(input_array)
    result = LinearRegMod.predict(input_array)
    return result