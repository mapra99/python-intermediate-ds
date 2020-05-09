# Import cars data
import pandas as pd
csv_path = "https://assets.datacamp.com/production/repositories/287/datasets/79b3c22c47a2f45a800c62cae39035ff2ea4e609/cars.csv"
cars = pd.read_csv(csv_path, index_col=0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row["cars_per_cap"]))
print(cars)
    
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
print(cars)
    
# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)