from math import sqrt


class GoldenRatio:

    def __init__(self, opt_func, a, b):
        self.opt_func = opt_func
        self.__a = a
        self.__b = b
        self.minimum = 0
        self.steps = []

    def optimize(self, epsilon, max_iterations):

        print(f'\ngolden ratio: f(x) in [{self.__a}, {self.__b}]')
        print(f'epsilon: {epsilon}; iterations_limit: {max_iterations}\n')

        iteration = 0

        print(f'iteration {iteration}')

        current_left = self.__a + ((3 - sqrt(5)) / 2) * (self.__b - self.__a)
        current_right = self.__a + self.__b - current_left
        self.steps += [[current_left, current_right]]

        print(f'    [a_{iteration}, b_{iteration}] == [{self.__a}, {self.__b}]')
        print(f'    [x_{iteration}, y_{iteration}] == [{current_left}, {current_right}]\n')

        while True:
            if self.opt_func(current_left) < self.opt_func(current_right):
                print(f'    f({current_left}) < f({current_right})')
                self.__b = current_right
                current_right = current_left
                current_left = self.__a + self.__b - current_right
            else:
                print(f'    f({current_left}) > f({current_right})')
                self.__a = current_left
                current_left = current_right
                current_right = self.__a + self.__b - current_left

            iteration += 1

            print(f'        [a_{iteration}, b_{iteration}] == [{self.__a}, {self.__b}]')
            print(f'        [x_{iteration}, y_{iteration}] == [{current_left}, {current_right}]')

            sign = ''
            if abs(current_right - current_left) < 2 * epsilon:
                sign = '<'
            else:
                sign = '>'

            print(f'    abs(a_{iteration} - b_{iteration}) == {abs(current_right - current_left)} {sign} {2 * epsilon}')

            self.steps += [[current_left, current_right]]

            if abs(self.__b - self.__a) < 2 * epsilon or iteration > max_iterations:
                self.minimum = (self.__a + self.__b) * 0.5
                print(f'\nx_minimum == {self.minimum}')
                print(f'f(x_minimum) == {self.opt_func(self.minimum)}')
                break

            print(f'\niteration {iteration}')

        return self.minimum
