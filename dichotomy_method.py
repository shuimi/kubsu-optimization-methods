class Dichotomy:

    def __init__(self, opt_func, a, b):
        self.opt_func = opt_func
        self.a = a
        self.b = b
        self.minimum = 0
        self.steps = []

    def optimize(self, epsilon, delta, max_iterations):

        print(f'\ndichotomy: f(x) in [{self.a}, {self.b}]')
        print(f'epsilon: {epsilon}; delta: {delta}; iterations_limit: {max_iterations}\n')

        iteration = 0

        current_left = self.a
        current_right = self.b

        print(f'iteration {iteration}\n    [a_{iteration}, b_{iteration}] == [{current_left}, {current_right}]')

        while True:

            new_left = (current_left + current_right - delta) * 0.5
            new_right = (current_left + current_right + delta) * 0.5

            print(f'    [x_{iteration}, y_{iteration}] == [{current_left}, {current_right}]')

            if self.opt_func(new_left) < self.opt_func(new_right):
                current_right = new_right
            else:
                current_left = new_left

            iteration += 1

            print(f'iteration {iteration}\n    [a_{iteration}, b_{iteration}] == [{current_left}, {current_right}]')

            sign = ''
            if abs(current_right - current_left) < 2 * epsilon:
                sign = '<'
            else:
                sign = '>'

            print(f'    abs(a_{iteration} - b_{iteration}) == {abs(current_right - current_left)} {sign} {2 * epsilon}')

            self.steps += [[current_left, current_right]]

            if abs(current_right - current_left) < 2 * epsilon or iteration > max_iterations:
                self.minimum = (current_left + current_right) * 0.5
                print(f'\nx_minimum == {self.minimum}')
                print(f'f(x_minimum) == {self.opt_func(self.minimum)}')
                break

        return self.minimum
