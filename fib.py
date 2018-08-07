def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def f(n):
    for k in range(n):
        for i in range(2000):
            fib(20)

if __name__ == '__main__':
    f(10)

