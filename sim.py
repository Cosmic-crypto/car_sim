import random
import time
from statistics import mean
import matplotlib.pyplot as plt

# -------------------------
# --- Vehicle Class ------
# -------------------------
class Vehicle:
    def __init__(self, name: str, max_speed: int, speed: int):
        self.name = name
        self.max_speed = max_speed
        self.speed = speed

    def __str__(self):
        return f"{self.name} ({self.speed} km/h)"
    
    def __repr__(self):
        return f"name={self.name}, max_speed={self.max_speed}, speed={self.speed}"

    def accelerate(self, increase: int):
        self.speed = min(self.speed + increase, self.max_speed)
        
    def brake(self, decrease: int):
        self.speed = max(self.speed - decrease, 0)

# -------------------------
# --- Setup Simulation ----
# -------------------------
car = Vehicle("Car", 150, 0)

iterations = []
speeds = []

# --- User Input ---
rounds = int(input("Enter how many simulations to run:\n"))

if rounds > 1000:
    print(f"Limit is 1000 — the simulation will run 1000 times instead of {rounds}.")
    rounds = 1000

# --- Simulation Loop ---
try:
    for i in range(rounds):
        if random.choice(["accelerate", "brake"]) == "accelerate":
            car.accelerate(random.randint(5, 20))
        else:
            max_brake = max(1, int(car.speed))  # fix empty range error
            car.brake(random.randint(1, max_brake))

        iterations.append(i + 1)
        speeds.append(car.speed)

        print(f"{i+1}. Current speed of the {car.name}: {car.speed} km/h")

        if rounds < 100:
            time.sleep(rounds / 1000)

except KeyboardInterrupt:
    print("Simulation interrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# -------------------------
# --- Summary -------------
# -------------------------
avg_speed = mean(speeds)
max_speed_value = max(speeds)
min_speed_value = min(speeds)
max_speed_index = speeds.index(max_speed_value) + 1
min_speed_index = speeds.index(min_speed_value) + 1

print(f"\nAverage speed: {avg_speed:.2f} km/h")
print(f"Max speed: {max_speed_value} km/h at iteration {max_speed_index}")
print(f"Min speed: {min_speed_value} km/h at iteration {min_speed_index}")

if rounds <= 50:
    print("Entire journey log:", speeds)
else:
    print(f"Showing first 20 speeds: {speeds[:20]} ...")

# -------------------------
# --- Plot ----------------
# -------------------------
plt.style.use('dark_background')  # clean dark mode

# Smooth line for speeds
plt.plot(iterations, speeds, linestyle='-', label='Speed (km/h)')

# Highlight key points
plt.scatter(iterations[0], speeds[0], color='green', label='Start', zorder=5)
plt.scatter(iterations[-1], speeds[-1], color='white', label='End', zorder=5)
plt.scatter(max_speed_index, max_speed_value, color='blue', label='Max Speed', zorder=5)
plt.scatter(min_speed_index, min_speed_value, color='orange', label='Min Speed', zorder=5)

# Labels, title, legend, grid
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (km/h)")
plt.title(f"{car.name} Speed per second")
plt.legend()
plt.grid(True, alpha=0)

# Save and show plot
plt.savefig("car_speed_graph_clean.png", dpi=300)
plt.show()
