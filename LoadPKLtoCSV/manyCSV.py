import pickle
import csv
import os

path_load = "/home/pes1ug22am100/Documents/Research and Experimentation/AOML- KINN/NewDataset/PDE-Datasets/u,x,t"
output_load = "/home/pes1ug22am100/Documents/Research and Experimentation/AOML- KINN/NewDataset/"

for file_name in os.listdir(path_load):
    if file_name.endswith(".pkl"):
        with open(os.path.join(path_load, file_name), "rb") as file_to_read:
            loaded_dictionary = pickle.load(file_to_read)
        
        u = loaded_dictionary["u"]
        x = loaded_dictionary["x"]
        t = loaded_dictionary["t"]

        output_name = f"output_{file_name.split('.')[0]}.csv"
        csv_path = os.path.join(output_load, output_name)
        
        with open(csv_path, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["t_index", "x_index", "u_value"])
            
            for t_idx, t_value in enumerate(t):
                for x_idx, x_value in enumerate(x):
                    writer.writerow([t_value, x_value, u[t_idx][x_idx]])

        print(f"Data successfully written to CSV at: {csv_path}")
