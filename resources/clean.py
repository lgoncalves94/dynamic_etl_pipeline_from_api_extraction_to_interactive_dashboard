import pandas as pd
import re

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_colwidth', None)  # No limit on column width
pd.set_option('display.width', None)  # Allow unlimited width


def clean_column(column):
    column = column.replace('Basel', '').replace('Total', '')  # Remove specified strings
    column = re.sub(r'\[.*?\]', '', column)  # Remove brackets and contents
    return column

with open('basel_10y_weather.csv','r') as file :
    data = pd.read_csv(file)

# Rename columns using the clean_column function
data.rename(columns={column: clean_column(column).strip().lower().replace(' ','_') for column in data.columns}, inplace=True)
data.drop(columns=['wind_direction'],inplace=True)

data.to_csv('clean.csv', index=False)


print(data.head())

# data.rename(columns={})