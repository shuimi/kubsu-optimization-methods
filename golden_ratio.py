from math import sqrt


class GoldenRatio:

    def __init__(self, opt_func, a, b):
        self.opt_func = opt_func
        self.__a = a
        self.__b = b
        self.minimum = 0
        self.steps = []

    def optimize(self, epsilon, max_iterations):

        iteration = 0

        current_left = self.__a + ((3 - sqrt(5)) / 2) * (self.__b - self.__a)
        current_right = self.__a + self.__b - current_left
        self.steps += [[current_left, current_right]]

        while True:

            if self.opt_func(current_left) < self.opt_func(current_right):
                self.__b = current_right
                current_right = current_left
                current_left = self.__a + self.__b - current_right
            else:
                self.__a = current_left
                current_left = current_right
                current_right = self.__a + self.__b - current_left

            iteration += 1
            self.steps += [[current_left, current_right]]

            if abs(self.__b - self.__a) < 2 * epsilon or iteration > max_iterations:
                self.minimum = (self.__a + self.__b) * 0.5
                break

        return self.minimum
