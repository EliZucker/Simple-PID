from controller import *
from hardware_simulated import *
import numpy as np
from scipy.interpolate import spline
import matplotlib.pyplot as plt


def simulate():
    hardware = SimulatedHardware()

    timestamps = np.arange(0, 3, 0.1)
    positions = np.empty(timestamps.shape)

    # Get positions over time via controller+simulator:
    curr_state = hardware.get_state()
    controller = PIDController(0.2, 0.1, 0.05, curr_state, 0)
    for i, time in enumerate(timestamps):
        controller_output = controller.get_controller_output(i + 1, curr_state)
        hardware.update_state(controller_output)
        curr_state = hardware.get_state()
        positions[i] = curr_state
        print(curr_state)

    x_smooth = np.linspace(timestamps.min(), timestamps.max(), 2000)
    positions_smooth = spline(timestamps, positions, x_smooth)
    plt.plot(x_smooth, positions_smooth)
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.show()


if __name__ == "__main__":
    simulate()
