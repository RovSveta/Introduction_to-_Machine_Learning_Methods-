# IMPORTS AND LOAD THE MODEL FROM FILE
import tkinter
import pandas as pd
from joblib import load
model = load("polynom_model.joblib")

print("Working?")
