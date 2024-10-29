import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load data
path_load = "/home/shusrith/projects/blind-eyes/PredefinedNoisePDE/u,x,t/"
file_to_read = open(path_load + "/2_0.pkl", "rb")
loaded_dictionary = pickle.load(file_to_read)
u = loaded_dictionary["u"]
x = loaded_dictionary["x"]
t = loaded_dictionary["t"]

# Parameters for Gaussian noise
mean = 1.0  # Non-zero mean
std_dev = 0.1  # Standard deviation

# Generate Gaussian noise
noise = np.random.normal(mean, std_dev, u.shape)

# Add noise to u
u_noisy = u + noise

# Normalize u_noisy to be between 0 and 1
u_min = np.min(u_noisy)
u_max = np.max(u_noisy)
u_noisy_normalized = (u_noisy - u_min) / (u_max - u_min)

# Create figure and axis
fig, ax = plt.subplots()
(line,) = ax.plot(x, u_noisy_normalized[0])


def update(frame):
    line.set_ydata(u_noisy_normalized[frame])
    ax.set_title(f"Time step {frame}")
    return (line,)


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=u_noisy_normalized.shape[0], blit=True
)

# Save as GIF
gif_path = "u_noisy_normalized_over_time.gif"
ani.save(gif_path, writer="imagemagick", fps=10)

print(f"GIF saved as {gif_path}")
loaded_dictionary["u_noisy"] = u_noisy

# Save the modified dictionary back to a pickle file (optional)
path_save = "/home/shusrith/projects/blind-eyes/PredefinedNoisePDE/u,x,t/"
file_to_write = open(path_save + "/2_0.pkl", "wb")
pickle.dump(loaded_dictionary, file_to_write)
file_to_write.close()
