import pickle
import csv
import os

path_load = "/home/pes1ug22am100/Documents/Research and Experimentation/AOML- KINN/NewDataset/PDE-Datasets/u,x,t"
output_load = "/home/pes1ug22am100/Documents/Research and Experimentation/AOML- KINN/NewDataset/"
csv_path = os.path.join(output_load, "combined_output.csv")

with open(csv_path, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["file_name", "t_index", "x_index", "u_value"])

    for file_name in os.listdir(path_load):
        if file_name.endswith(".pkl"):
            # Load each pickle file
            with open(os.path.join(path_load, file_name), "rb") as file_to_read:
                loaded_dictionary = pickle.load(file_to_read)
            
            u = loaded_dictionary["u"]
            x = loaded_dictionary["x"]
            t = loaded_dictionary["t"]

            for t_idx, t_value in enumerate(t):
                for x_idx, x_value in enumerate(x):
                    writer.writerow([file_name, t_value, x_value, u[t_idx][x_idx]])

print(f"Data successfully written to combined CSV at: {csv_path}")
