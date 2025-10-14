import csv, sys, statistics
from pathlib import Path
import pandas as pd

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
            # You can process each row here if needed
        print("Rows:", row_count)
        if row_count == 0:
            return
    print("Columns:", list(row[0].keys()))