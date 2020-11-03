class PIDController:
    def __init__(self, Kp, Ki, Kd, start_error, start_time):
        self.curr_error = start_error
        self.curr_time = start_time

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.sensitivity = 5

    def get_controller_output(self, new_time, new_error):
        time_diff = new_time - self.curr_time

        error_integral_estimate = (new_error + self.curr_error) * time_diff / 2.0
        error_derivative_estimate = (new_error - self.curr_error) / time_diff

        self.curr_error = new_error
        self.curr_time = new_time

        # CORE FORUMLA:
        return (
            self.Kp * self.curr_error
            + self.Ki * error_integral_estimate
            + self.Kd * error_derivative_estimate
        )
