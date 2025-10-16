import csv, sys, statistics
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog

#------- Functions -----
def analyze(path, status_label):
    try:
        openfile = pd.read_csv(path)
        print("\n--- Console Analysis ---")
        print(f"File '{path}' loaded successfully.")
        print(f"Rows: {len(openfile)}")
        return openfile
    except Exception as e:
        print(f"Error loading file '{path}': {e}")
        status_label.config(text=f"Error loading file: {e}")
        return None

def selectFile(status_label, target_frame):
    file_path= filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        dataframe = analyze(file_path)
        display_on_gui(data_frame, target_frame)
    else:
        print("No file selected.")

def display_on_gui(df, frame):
    # Clear any existing widgets in the frame (like an old table)
    for widget in frame.winfo_children():
        widget.destroy()

    if df is None:
        return
    
    df.columns = [str(col) for col in df.columns]  # Ensure all column names are strings
    # --- Create the Treeview with Scrollbars ---
    tree = ttk.Treeview(frame, show="headings")
    
    # Vertical scrollbar
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    
    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)

    # Place the widgets on the screen
    vsb.grid(row=0, column=1, sticky='nsew')
    hsb.grid(row=1, column=0, sticky='ns')
    tree.grid(row=0, column=0, sticky='ew')

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # --- Populate the Treeview ---
    # 1. Define columns from the DataFrame's columns
    tree["columns"] = list(df)

    # 2. Create column headings
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='w') # 'w' anchors text to the left

    # 3. Insert the data rows
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

# ------

# -----Main Function------
if __name__=="__main__":
    root = tk.Tk() #initialize
    root.title("CSVenger - CSV Analyzer")
    root.geometry("400x200")

        # --- Top Frame for Controls ---
    control_frame = tk.Frame(root)
    control_frame.pack(pady=10, fill='x')
    
    data_frame = tk.Frame(root)
    data_frame.pack(fill='both', expand=True, padx=10, pady=10)

    welcome_label = tk.Label(root, text="Welcome to CSVengeqr!", font=("Helvetica", 16))
    welcome_label.pack()
    
    # --- Data Frame for the Table ---
    # This frame will hold the Treeview widget
    data_frame = tk.Frame(root)
    data_frame.pack(fill='both', expand=True, padx=10, pady=10)

    open_button = tk.Button(root, text="Open CSV File", command=lambda: selectFile(status_label, data_frame),
                            font=("Helvetica", 14),
                            height=2, width=15)
    
    open_button.pack(side='left', expand=True, padx=20, pady=20)
    
    exit_button = tk.Button(root, text="Exit", command=root.quit,
                            font=("Helvetica", 14))
    
    status_label = tk.Label(root, text="Eish", fg="red")
    status_label.pack(side='bottom', fill='x')

    welcome_label.pack(pady=20)
    open_button.pack(pady=10)
    exit_button.pack(pady=10)

    root.mainloop()