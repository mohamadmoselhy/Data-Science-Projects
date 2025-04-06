import numpy as np
import joblib

def predict(user_input):
    LinearRegMod = joblib.load('LinearRegression/Model/App/model.pkl')  # Load the trained model
    MyScaler = joblib.load('LinearRegression/Model/App/scaler.pkl')  # Load the saved scaler
    # Convert dict to 2D array if needed
    input_array = np.array([list(user_input.values())])
    input_array=MyScaler.transform(input_array)
    result = LinearRegMod.predict(input_array)
    return result