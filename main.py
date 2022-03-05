from dichotomy_method import Dichotomy
from golden_ratio import GoldenRatio


if __name__ == '__main__':

    def func(x):
        return x ** 2 + 2

    # golden_ratio = Dichotomy(opt_func=func, a=-3, b=7)
    # result = golden_ratio.optimize(delta=0.2, epsilon=0.5, max_iterations=1000)

    # print(f'x = {result}, f(x) = {func(result)}')
    # print(golden_ratio.steps)

    golden_ratio = GoldenRatio(opt_func=func, a=-3, b=7)
    result = golden_ratio.optimize(epsilon=0.5, max_iterations=1000)

    print(f'x = {result}, f(x) = {func(result)}')
    print(golden_ratio.steps)

