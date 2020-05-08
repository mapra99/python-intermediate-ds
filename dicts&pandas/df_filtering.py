import pandas as pd
import numpy as np

csv_path = "https://assets.datacamp.com/production/repositories/287/datasets/79b3c22c47a2f45a800c62cae39035ff2ea4e609/cars.csv"
cars = pd.read_csv(csv_path, index_col=0)

# Use dr to subset cars: sel
sel = cars[cars['drives_right']]
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars['cars_per_cap'] > 500]
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
print(medium)