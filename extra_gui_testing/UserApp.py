# PART 1: IMPORTS AND LOAD THE MODEL FROM FILE
import tkinter as tk
import pandas as pd
from joblib import load

# Load the trained model
model = load("linear_model_2.joblib")

print("Working?")
# it works)

# PART 2: CREATE THE GUI

# Create the main window
window = tk.Tk()
window.title("House Price Prediction GUI Application")
window.geometry("600x500")
window.option_add("*font", "lucida 14")

# Define the variable names that your model expects
variables = [
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
    "distance_to_coast"
]

# Dictionary to hold the Entry widgets for each variable
entries = {}

# Create a frame:
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create labels and entry fields for each variable
for idx, var in enumerate(variables):
    lbl = tk.Label(input_frame, text=var + ":", anchor="w", width=20)
    lbl.grid(row=idx, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(input_frame, width=15)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries[var] = entry

# insert default values for convenience
default_values = {
    "housing_median_age": "50",
    "total_rooms": "500",
    "total_bedrooms": "70",
    "population": "300",
    "households": "50",
    "median_income": "8.4567",
    "distance_to_coast": "1"
}

# Insert default values
for var, default in default_values.items():
    entries[var].insert(0, default)

# Create a StringVar for displaying the prediction result
result_var = tk.StringVar()
result_var.set("Enter values and click the button!")

# Result label
result_label = tk.Label(window, textvariable=result_var, fg="blue")
result_label.pack(pady=10)

# Function to retrieve inputs, make prediction, and display the result
def set_text_by_button():
    try:
        # Get values from entry fields and convert them to float
        input_data = {var: float(entries[var].get()) for var in variables}
    except ValueError:
        result_var.set("Error: Please enter valid numbers!")
        return

    # Convert dictionary to DataFrame for prediction
    tester_df = pd.DataFrame([input_data])

    # Make the prediction
    result = model.predict(tester_df)[0]
    
    # Display the prediction result
    result_var.set(f"Predicted Price: {round(float(result), 2)} $")

# Prediction button
predict_button = tk.Button(window, text="Get House Price!", command=set_text_by_button)
predict_button.pack(pady=10)

# Bind Enter key to trigger the prediction
window.bind('<Return>', lambda event: set_text_by_button())

# Run the Tkinter event loop
window.mainloop()

# I used help of ChatGPT here, when I was trying to implement UI without it based on lesson notes,
# I couldn't create a  multiply entries and it worked only if I would have only one support variable.