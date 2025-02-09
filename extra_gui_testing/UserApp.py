# IMPORTS AND LOAD THE MODEL FROM FILE
import tkinter
import pandas as pd
from joblib import load
model = load("polynom_model_1.joblib")

print("Working?")

# it works)

# PART 2: TEST THE MODEL FIRST WITHOUT PROCEEDING FURTHER (tester_row)