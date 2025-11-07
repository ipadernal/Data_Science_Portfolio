import pandas as pd
import numpy as np

#display options of columns
pd.set_option('display.max_columns', None)

file_path = 'p1_loan_data.csv'
df = pd.read_csv(file_path, low_memory=False)