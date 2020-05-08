import pandas as pd

csv_path = "https://assets.datacamp.com/production/repositories/287/datasets/79b3c22c47a2f45a800c62cae39035ff2ea4e609/cars.csv"
cars = pd.read_csv(csv_path, index_col=0)

# Square Brackets to select columns
print(cars['country'])
print(cars[['country']])
print(cars[['country', 'drives_right']])

# Square Brackets to select rows
print(cars[0:3])
print(cars[3:6])

# loc and iloc
print(cars.loc['JPN'])
print(cars.iloc[2])
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])
print(cars.loc['MOR', 'drives_right'])
print(cars.loc[['RU','MOR'], ['country','drives_right']])