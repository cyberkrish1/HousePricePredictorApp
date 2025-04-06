# --- model1.py ---
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

def preprocess_data(data):
    data['air_conditioned'] = data['air_conditioned'].map({'yes': 1, 'no': 0})
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_locations = encoder.fit_transform(data[['location']])
    location_df = pd.DataFrame(encoded_locations, columns=encoder.get_feature_names_out(['location']))
    data_encoded = pd.concat([data.drop(columns=['location']), location_df], axis=1)
    return data_encoded, encoder

def train_models(data_encoded):
    X = data_encoded.drop(columns=['price'])
    y = data_encoded['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    lin_reg = LinearRegression().fit(X_train, y_train)
    rf = RandomForestRegressor(random_state=42).fit(X_train, y_train)
    return lin_reg, rf

def prepare_input(input_dict, location, encoder, reference_columns):
    input_df = pd.DataFrame([input_dict])
    location_encoded = encoder.transform(pd.DataFrame([[location]], columns=['location']))
    location_encoded_df = pd.DataFrame(location_encoded, columns=encoder.get_feature_names_out(['location']))
    final_input = pd.concat([input_df, location_encoded_df], axis=1)
    for col in reference_columns:
        if col not in final_input.columns:
            final_input[col] = 0
    final_input = final_input[reference_columns]
    return final_input
