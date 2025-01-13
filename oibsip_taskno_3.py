import tkinter as tk
from tkinter import messagebox

#  calculate BMI
def calculate_bmi():
    try:
       
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())  # Height in cm

        height_m = height_cm / 100

    
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Input Error", "Please enter positive values for weight and height.")
            return

        # BMI formula
        bmi = weight / (height_m ** 2)

        #  the BMI result
        result_bmi.config(text=f"BMI: {bmi:.2f}")

        # Categorize BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        #  BMI category
        result_category.config(text=f"Category: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

#  the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")  # Window size
root.configure(bg="#F0F8FF")  # Light blue background

# title label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 24, "bold"), fg="#4CAF50", bg="#F0F8FF")
title_label.pack(pady=20)

# weight input section
weight_label = tk.Label(root, text="Enter your weight (kg):", font=("Arial", 12), bg="#F0F8FF")
weight_label.pack(pady=5)
entry_weight = tk.Entry(root, font=("Arial", 12), width=20, bd=2, relief="solid")
entry_weight.pack(pady=5)

# height input section (in centimeters)
height_label = tk.Label(root, text="Enter your height (cm):", font=("Arial", 12), bg="#F0F8FF")
height_label.pack(pady=5)
entry_height = tk.Entry(root, font=("Arial", 12), width=20, bd=2, relief="solid")
entry_height.pack(pady=5)

# calculate button
calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 14), bg="#4CAF50", fg="white", command=calculate_bmi)
calculate_button.pack(pady=20)

#  result labels
result_bmi = tk.Label(root, text="BMI: N/A", font=("Arial", 14), fg="#4CAF50", bg="#F0F8FF")
result_bmi.pack(pady=10)

result_category = tk.Label(root, text="Category: N/A", font=("Arial", 14), fg="#4CAF50", bg="#F0F8FF")
result_category.pack(pady=10)

root.mainloop()
