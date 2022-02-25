from dichotomy_method import Dichotomy


if __name__ == '__main__':

    def func(x):
        return x ** 2 + 2

    dichotomy = Dichotomy(opt_func=func, a=-3, b=7)
    result = dichotomy.optimize(delta=0.2, epsilon=0.5, max_iterations=1000)

    print(f'x = {result}, f(x) = {func(result)}')
    print(dichotomy.steps)
