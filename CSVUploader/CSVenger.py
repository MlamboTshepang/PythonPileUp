import csv, sys, statistics
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import filedialog


def selectFile():
    file_path= filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        analyze(file_path)
    else:
        print("No file selected.")

def analyze(path):
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row_count = 0
        nums = None
        for row in reader:
            if row_count == 0:
                nums = {k: [] for k in row.keys()}
                print("Columns:", list(row.keys()))
            row_count += 1
            print(dataframe := pd.DataFrame([row]))
        print("Rows:", row_count)
        if row_count == 0:
            return
    print("Columns:", list(row[0].keys()))

if __name__=="__main__":
    root = tk.Tk() #initialize
    root.title("CSVenger - CSV Analyzer")
    root.geometry("400x200")

    welcome_label = tk.Label(root, text="Welcome to CSVenger!", font=("Helvetica", 16))

    open_button = tk.Button(root, text="Open CSV File", command=lambda: selectFile(root),
                            font=("Helvetica", 14),
                            height=2, width=15)
    
    exit_button = tk.Button(root, text="Exit", command=root.destroy,
                            font=("Helvetica", 14))
    
    welcome_label.pack(pady=20)
    open_button.pack(pady=10)
    exit_button.pack(pady=10)