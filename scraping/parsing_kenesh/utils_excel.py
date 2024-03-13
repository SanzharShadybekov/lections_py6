import pandas as pd
import os

DIR_PATH = os.getcwd() + '/files'


csv_file = pd.read_csv(DIR_PATH + '/deputy.csv')
csv_file.to_excel(DIR_PATH + '/deputy.xlsx', index=None, header=True)

