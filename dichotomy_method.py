class Dichotomy:

    def __init__(self, opt_func, a, b):
        self.opt_func = opt_func
        self.a = a
        self.b = b
        self.minimum = 0
        self.steps = []

    def optimize(self, epsilon, delta, max_iterations):

        iteration = 0

        current_left = self.a
        current_right = self.b

        while True:

            new_left = (current_left + current_right - delta) * 0.5
            new_right = (current_left + current_right + delta) * 0.5

            if self.opt_func(new_left) < self.opt_func(new_right):
                current_right = new_right
            else:
                current_left = new_left

            iteration += 1
            self.steps += [[current_left, current_right]]

            if abs(current_right - current_left) < 2 * epsilon or iteration > max_iterations:
                self.minimum = (current_left + current_right) * 0.5
                break

        return self.minimum
