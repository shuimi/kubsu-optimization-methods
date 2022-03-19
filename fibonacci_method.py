class Fibonacci:

    def __init__(self, opt_func, a, b):
        self.opt_func = opt_func
        self.a = a
        self.b = b
        self.minimum = 0
        self.steps = []

    def __fib(self, n):
        if n in (1, 2):
            return 1
        return self.__fib(n - 1) + self.__fib(n - 2)

    def optimize(self, delta=0.2, epsilon=0.01):

        N = 1
        while self.__fib(N) <= abs(self.b - self.a) / delta:
            N += 1

        a_n = self.a
        b_n = self.b

        print(f'\nfibonacci: f(x) in [{self.a}, {self.b}]')
        print(f'N: {N}\n')

        y_n = a_n + (self.__fib(N - 2) / self.__fib(N)) * (b_n - a_n)
        z_n = a_n + (self.__fib(N - 1) / self.__fib(N)) * (b_n - a_n)

        k = 0
        while k != N - 3:
            print('iteration', k)
            print(f'    y == {y_n}, z == {z_n}')
            if self.opt_func(y_n) > self.opt_func(z_n):
                print(f'        ✅ {self.opt_func(y_n)} > {self.opt_func(z_n)}')
                a_n = y_n
                y_n = z_n
                z_n = a_n + (self.__fib(N - k - 2) / self.__fib(N - k - 1)) * (b_n - a_n)
            else:
                print(f'        ✅ {self.opt_func(y_n)} <= {self.opt_func(z_n)}')
                b_n = z_n
                z_n = y_n
                y_n = a_n + (self.__fib(N - k - 3) / self.__fib(N - k - 1)) * (b_n - a_n)
            print(f'    [a_{k}, b_{k}] == [{a_n}, {b_n}]; delta == {delta}')
            k += 1

        y_n = z_n
        z_n = y_n + epsilon

        if self.opt_func(y_n) <= self.opt_func(z_n):
            b_n = z_n
        else:
            a_n = y_n
        self.minimum = (a_n + b_n) / 2

        print("\niterations ==", k)
        print("x_minimum:", (a_n + b_n) / 2)
        print("f(x_minimum):", self.opt_func((a_n + b_n) / 2))

        fib = [self.__fib(i) for i in range(1, N + 1)]
        print('fibonacci numbers used: ', fib)

        return self.minimum
