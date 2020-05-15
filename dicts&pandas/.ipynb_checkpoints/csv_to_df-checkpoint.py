import pandas as pd

csv_path = "https://assets.datacamp.com/production/repositories/287/datasets/79b3c22c47a2f45a800c62cae39035ff2ea4e609/cars.csv"
cars = pd.read_csv(csv_path, index_col=0)

print(cars)