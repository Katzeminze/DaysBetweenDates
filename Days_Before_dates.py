# Days_Before_dates.py

from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

entry_date1 = None
entry_date2 = None

def calculate_days_between_dates(date1_str, date2_str):
    # Convert string dates to datetime objects
    date1 = datetime.strptime(date1_str, '%d-%m-%Y')
    date2 = datetime.strptime(date2_str, '%d-%m-%Y')
    
    # Calculate the difference in days
    delta = abs((date2 - date1).days)
    return delta

def on_calculate():
    date1 = entry_date1.get_date()
    date2 = entry_date2.get_date()
    try:
        days = calculate_days_between_dates(date1, date2)
        messagebox.showinfo("Result", f'Days between {date1} and {date2}: {days}')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid dates in DD-MM-YYYY format.")

def userInterface():
    global entry_date1, entry_date2
    root = tk.Tk()
    root.title("Days Between Dates Calculator")

    # Create and place the calendars
    entry_date1 = Calendar(root, selectmode='day', date_pattern='dd-mm-yyyy')
    entry_date1.pack(pady=10)

    entry_date2 = Calendar(root, selectmode='day', date_pattern='dd-mm-yyyy')
    entry_date2.pack(pady=10)

    # Create and place the calculate button
    button_calculate = tk.Button(root, text="Calculate Days", command=on_calculate)
    button_calculate.pack(pady=20)

    # Run the application
    root.mainloop()
    # global entry_date1, entry_date2
    # # Create the main window
    # root = tk.Tk()
    # root.title("Days Between Dates Calculator")

    # # Create and place the labels and entry fields
    # label_date1 = tk.Label(root, text="Enter first date (DD-MM-YYYY):")
    # label_date1.pack()

    # entry_date1 = tk.Entry(root)
    # entry_date1.pack()

    # label_date2 = tk.Label(root, text="Enter second date (DD-MM-YYYY):")
    # label_date2.pack()

    # entry_date2 = tk.Entry(root)
    # entry_date2.pack()

    # # Create and place the calculate button
    # button_calculate = tk.Button(root, text="Calculate Days", command=on_calculate)
    # button_calculate.pack()

    # # Run the application
    # root.mainloop()

# start your program 
userInterface()
