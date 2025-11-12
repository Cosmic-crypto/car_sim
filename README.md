# Vehicle Speed Simulation

A Python script that simulates vehicle movement, tracks speed changes over time, and visualizes the results using matplotlib.

## Features

- **Vehicle Class**: Simulates basic vehicle behavior with acceleration and braking
- **Speed Simulation**: Models realistic vehicle movement over time
- **Data Visualization**: Generates a speed vs. time graph
- **Performance Metrics**: Calculates average speed and total distance traveled

## Requirements

- Python 3.6+
- matplotlib
- statistics (included in Python standard library)

## Installation

1. Clone the repository
2. Install the required packages:
   ```bash
   pip install matplotlib
   ```

## Usage

Run the script:
```bash
python main2.py
```

The script will:
1. Simulate a car's movement with random acceleration and braking
2. Track the car's speed over time
3. Generate a speed vs. time graph
4. Display performance metrics including:
   - Total simulation time
   - Average speed
   - Total distance traveled

## Output

The script creates a visualization showing:
- Speed (km/h) on the Y-axis
- Time (seconds) on the X-axis
- A line graph of speed changes over time

## Customization

You can modify the following parameters in the script:
- `SIMULATION_DURATION`: Total simulation time in seconds
- `TIME_STEP`: Time between each simulation step
- `MAX_ACCELERATION`: Maximum acceleration/deceleration per time step

## Example Output

```
=== Simulation Complete ===
Total time: 60.0 seconds
Average speed: 75.0 km/h
Total distance traveled: 1.25 km
```

## Dependencies

- matplotlib: For generating the speed vs. time graph
- random: For generating random speed changes
- time: For tracking simulation time
- statistics: For calculating average speed
