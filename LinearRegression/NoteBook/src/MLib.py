from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from datetime import datetime

def calculate_regression_metrics(y_test, y_predict):
    """
    This function calculates the Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² Score
    for the model's predictions.
    mse, mae, r2
    """
    mse = mean_squared_error(y_test, y_predict)
    mae = mean_absolute_error(y_test, y_predict)
    r2 = r2_score(y_test, y_predict)
    
    return mse, mae, r2


def prepare_and_train_linear_regression_model(x, y, test_size=0.3, shuffle=True, random_state=0):
    """
    This function splits the dataset into training and testing sets, scales the features using 
    StandardScaler, and trains a Linear Regression model on the scaled training data.
    """
    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, shuffle=shuffle, random_state=random_state)
    
    # Initialize the StandardScaler
    MyScaler = StandardScaler()
    
    # Fit and transform the training data, then transform the test data
    x_Scaled_train = MyScaler.fit_transform(x_train)
    x_Scaled_test = MyScaler.transform(x_test)
    
    # Initialize and fit the Linear Regression model
    LinearRegMod = LinearRegression()
    LinearRegMod.fit(x_Scaled_train, y_train)
    
    # Return scaler, model, and data splits
    return MyScaler, LinearRegMod, x_train, x_test, y_train, y_test


def save_model_and_scaler(model, scaler, model_filename='model', scaler_filename='scaler', save_dir='Model'):
    """
    Save the model and scaler to disk with a timestamp in the filename.
    """
    # Generate timestamp with the format "YYYY-MM-DD_HH-MM-SS"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create the full paths with timestamp
    model_path = f'{save_dir}/{model_filename}_{timestamp}.pkl'
    scaler_path = f'{save_dir}/{scaler_filename}_{timestamp}.pkl'
    
    # Save the model and scaler with timestamped filenames
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    
    print(f"Model saved as {model_path}")
    print(f"Scaler saved as {scaler_path}")