import pickle
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters for Gaussian noise
mean = 1.0  # Non-zero mean
std_dev = 0.1  # Standard deviation
sigma = 1  # Standard deviation for Gaussian kernel

# Iterate over the file names from 3_0.pkl to 3_29.pkl
for k in range(1, 5):
    for l in range(30):
        file_name = f"{k}_{l}.pkl"
        path_load = f"/kaggle/working/PredefinedNoisePDE/u,x,t/{file_name}"

        # Load data
        with open(path_load, "rb") as file_to_read:
            loaded_dictionary = pickle.load(file_to_read)

        u = loaded_dictionary["u"]
        x = loaded_dictionary["x"]
        t = loaded_dictionary["t"]

        # Generate Gaussian noise
        noise = np.zeros(shape=(u.shape[0], u.shape[1]))
        for i in range(u.shape[0]):
            for j in range(u.shape[1]):
                noise[i, j] = np.random.normal(
                    np.random.normal(abs(u[i][j]), abs(u[i][j]) + 0.1), abs(u[i][j])
                )

        # Add noise to u
        u_noisy = u + noise

        # Apply Gaussian filter to smooth the noisy data
        u_noisy_smoothed = gaussian_filter(u_noisy, sigma=sigma)

        # Normalize u_noisy_smoothed to be between 0 and 1
        u_min = np.min(u_noisy_smoothed)
        u_max = np.max(u_noisy_smoothed)
        u_noisy_normalized = (u_noisy_smoothed - u_min) / (u_max - u_min)

        loaded_dictionary["u_noisy"] = u_noisy_normalized
        with open(path_load, "wb") as file_to_write:
            pickle.dump(loaded_dictionary, file_to_write)

        print(f"Processed and saved {file_name}")
