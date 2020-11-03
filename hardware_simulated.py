import random


class SimulatedHardware:
    def __init__(self):
        self.sensitivity = 5
        self.curr_state = 6.5  # arbitrary starting state
        self.time_factor = 1

    def update_state(self, hardware_input):
        new_state = (
            self.curr_state
            - (hardware_input * self.sensitivity)
            + (1.0 / self.time_factor)
        )
        self.time_factor += 1
        self.curr_state = new_state

    def get_state(self):
        return self.curr_state
