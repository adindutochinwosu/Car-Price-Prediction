import pandas as pd
import streamlit as st
import numpy as np
import time
import xgboost as xgb

# from sklearn.preprocessing import StandardScaler

st.title("Car Price Prediction Web App")
st.text("Deploy Machine Learning Model using Streamlit and Docker")

st.header("Please enter the required vehicle information: ")


# STEP 1: =================================== ACCEPT USER INPUT ====================================#

# following lines create boxes in which user can enter data required to make prediction
# Year = st.number_input("Car Registration Year")
Year = st.selectbox("Car Registration Year", ("1970", "1996", "1997", "1998", "1999", "2000",
                                              "2001", "2002", "2003", "2004", "2005", "2006",
                                              "2007", "2008", "2009", "2010", "2011", "2012",
                                              "2013", "2014", "2015", "2016", "2017", "2018",
                                              "2019", "2020"))

# =========== Transmission ============#
Transmission = st.selectbox(
    'Transmission Type', ("Manual", "Automatic", "Semi-Auto", "Other"))

if Transmission == 'Manual':
    Transmission = 0
elif Transmission == "Semi-Auto":
    Transmission = 1
elif Transmission == 'Automatic':
    Transmission = 2
elif Transmission == 'Other':
    Transmission = 3
else:
    pass

# =========== Mileage ============#
Mileage = st.number_input("Odometer Reading (miles)")

# =========== Fuel Type ============#
FuelType = st.selectbox(
    "Fuel Type", ("Diesel", "Petrol", "Hybrid", "Electric", "Other"))

if FuelType == 'Petrol':
    FuelType = 0
elif FuelType == 'Diesel':
    FuelType = 1
elif FuelType == 'Hybrid':
    FuelType = 2
elif FuelType == 'Other':
    FuelType = 3
elif FuelType == 'Electric':
    FuelType = 4
else:
    pass

# =========== Tax ============#
Tax = st.number_input("Annual Tax (£)")

# =========== Miles per Gallon ============#
MPG = st.number_input("Miles per gallon (MPG)")

# =========== Engine Size ============#
EngineSize = st.number_input("Engine size (Litres)")

# =========== Make ============#
Make = st.selectbox("Manufacturer",
                    ("Ford", "Volkswagen", "Vauxhall", "Mercedes", "BMW", "Audi", "Toyota", "Skoda", "Hyundai"))
if Make == 'Ford':
    Make = 0
elif Make == 'Volkswagen':
    Make = 1
elif Make == 'Vauxhall':
    Make = 2
elif Make == 'Mercedes':
    Make = 3
elif Make == 'BMW':
    Make = 4
elif Make == 'Audi':
    Make = 5
elif Make == 'Toyota':
    Make = 6
elif Make == 'Skoda':
    Make = 7
elif Make == 'Hyundai':
    Make = 8
else:
    pass


# STEP 2: =================================== PERFORM PREDICTION ====================================#

# defining the function which will make the prediction using the data which the user inputs
def predictCarPrice(predictors):
    features = np.array(predictors).reshape(1, 8)

    # Convert the features to DMatrix data type
    df_features = xgb.DMatrix(features)

    # Loading the trained model
    trained_model = xgb.Booster({'nthread': 4})
    trained_model.load_model("xgb_dmatrix.model")

    predicted_result = trained_model.predict(df_features)

    return predicted_result


if st.button("Predict the Car Price"):
    with st.spinner("Predicting the car price..."):
        time.sleep(1)

    features_list = [int(Year), int(Transmission), int(Mileage), int(FuelType), int(Tax), float(MPG), float(EngineSize),
                     int(Make)]

    result = predictCarPrice(features_list)

    # Rounding up the predicted price
    # predicted_car_price = round(result[0])
    predicted_car_price = int(result)

# STEP 3: =================================== PRESENT USER WITH PREDICTED CAR PRICE ====================================#
    st.success("The predicted car price is {0}{1}".format("£", predicted_car_price))
    print("\n")
