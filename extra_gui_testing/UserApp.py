# IMPORTS AND LOAD THE MODEL FROM FILE
import tkinter
import pandas as pd
from joblib import load
model = load("polynom_model_1.joblib")

print("Working?")

# it works)

# PART 2: TEST THE MODEL FIRST WITHOUT PROCEEDING FURTHER (tester_row)

# this variable could be connected
# to a user interface (textbox etc.)
housing_median_age = 50,
total_rooms = 500,
total_bedrooms = 70,
population = 300,
households = 50,	
median_income = 8.4567, 
ocean_proximity_more_then_one_H_OCEAN =  1,
ocean_proximity_INLAND =  0,
ocean_proximity_NEAR_BAY = 0,
ocean_proximity_NEAR_OCEAN = 0

# map all the variables from the user
# into a Python dictionary
# the variable names have to match with the original dataset
tester_row = {
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,	
    "median_income": median_income, 
    "ocean_proximity_<1H OCEAN": ocean_proximity_more_then_one_H_OCEAN,
    "ocean_proximity_INLAND": ocean_proximity_INLAND,
    "ocean_proximity_NEAR BAY": ocean_proximity_NEAR_BAY,
    "ocean_proximity_NEAR OCEAN": ocean_proximity_NEAR_OCEAN
}

# convert to pandas-format
tester_row = pd.DataFrame([tester_row])

# get the output/result/answer from the model
# based on the user's new data (from above code cell)
result = model.predict(tester_row)[0]

print()
print(f"Predicted house price with given parameters")
print(f"{round(float(result), 2)} $")
print("----------------")

# PART 3: CREATE THE GUI

