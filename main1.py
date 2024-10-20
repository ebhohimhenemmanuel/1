# Simple and Compound Interest Calculator


import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * (1 + rate / 100) ** time - principal

        result = f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        messagebox.showinfo("Interest Calculation", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

app = tk.Tk()
app.title("Interest Calculator")

tk.Label(app, text="Principal Amount:").grid(row=0, column=0)
principal_entry = tk.Entry(app)
principal_entry.grid(row=0, column=1)

tk.Label(app, text="Time Period (in years):").grid(row=1, column=0)
time_entry = tk.Entry(app)
time_entry.grid(row=1, column=1)

tk.Label(app, text="Rate of Interest (%):").grid(row=2, column=0)
rate_entry = tk.Entry(app)
rate_entry.grid(row=2, column=1)

calculate_button = tk.Button(app, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, columnspan=2)

app.mainloop()
