import pickle
import csv
import json
import os

path_load = "/home/pes1ug22am100/Documents/Research and Experimentation/AOML- KINN/NewDataset/PDE-Datasets/u,x,t"
file_name = "2_12.pkl"
output_load = "/home/pes1ug22am100/Documents/Research and Experimentation/AOML- KINN/NewDataset/"
output_name = f"output_{file_name.split('.')[0]}"
file_to_read = open(os.path.join(path_load, file_name), "rb")
loaded_dictionary = pickle.load(file_to_read)
u = loaded_dictionary["u"]
x = loaded_dictionary["x"]
t = loaded_dictionary["t"]

csv_path = os.path.join(output_load, f"{output_name}.csv")
with open(csv_path, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["t_index", "x_index", "u_value"])
    for t_idx, t_value in enumerate(t):
        for x_idx, x_value in enumerate(x):
            writer.writerow([t_value, x_value, u[t_idx][x_idx]])

print(f"Data successfully written to CSV at: {csv_path}")