import pickle

path_load = "/home/pes1ug22am100/Documents/Research and Experimentation/AOML- KINN/NewDataset/PDE-Datasets/u,x,t"
file_to_read = open(path_load+"/2_12.pkl", "rb")
loaded_dictionary = pickle.load(file_to_read)
u = loaded_dictionary["u"]
x = loaded_dictionary["x"]
t = loaded_dictionary["t"]
print(u) # list of lists
print(f'\n\n\n{x}') # 1d lsit
print(f'\n\n\n{t}') # 1d list

# print(f'\n\n\nThe range of x: {min(x), max(x)}') # x: (-8.0, 7.9375)
# print(f'\n\n\nThe range of t: {min(t), max(t)}') # t: (0.0, 10.0)
# print(f'\n\n\nThe range of u: {min(u), max(u)}') # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

