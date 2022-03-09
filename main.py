from dichotomy_method import Dichotomy
from fibonacci_method import Fibonacci
from golden_ratio import GoldenRatio


if __name__ == '__main__':

    def func(x):
        return x ** 2 + 2

    def report(method_name, result, steps):
        print(f'\n{method_name}: x = {result}, f(x) = {func(result)}')
        print(steps)

    dichotomy = Dichotomy(opt_func=func, a=-3, b=7)
    report(
        'dichotomy',
        dichotomy.optimize(delta=0.2, epsilon=0.5, max_iterations=1000),
        dichotomy.steps
    )

    golden_ratio = GoldenRatio(opt_func=func, a=-3, b=7)
    report(
        'golden_ratio',
        golden_ratio.optimize(epsilon=0.5, max_iterations=1000),
        golden_ratio.steps
    )

    fibonacci = Fibonacci(opt_func=func, a=-3, b=7)
    report(
        'fibonacci',
        fibonacci.optimize(delta=0.2, epsilon=0.5),
        fibonacci.steps
    )
