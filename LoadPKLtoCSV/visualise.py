import pickle
import matplotlib.pyplot as plt
import matplotlib.animation as animation


path_load = "/home/shusrith/projects/blind-eyes/PredefinedNoisePDE/u,x,t/"
file_to_read = open(path_load + "/3_1.pkl", "rb")
loaded_dictionary = pickle.load(file_to_read)
u = loaded_dictionary["u"]
x = loaded_dictionary["x"]
t = loaded_dictionary["t"]

fig, ax = plt.subplots()
(line,) = ax.plot(x, u[0])


def update(frame):
    line.set_ydata(u[frame])
    ax.set_title(f"Time step {frame}")
    return (line,)


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=u.shape[0], blit=True
)

# Save as GIF
gif_path = "u_noisy_normalized_over_time.gif"
ani.save(gif_path, writer="imagemagick", fps=10)

print(f"GIF saved as {gif_path}")
