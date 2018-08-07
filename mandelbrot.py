import math

def mandelbrot(z , c , n=40):
    if abs(z) > 1000:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

def main():
    for x in [a * 0.02 for a in range(-8000, 3000)]:
       for y in [a * 0.05 for a in range(-2000, 2000)]:
          mandelbrot(0, x + 1j * y)

if __name__ == '__main__':
    main()
