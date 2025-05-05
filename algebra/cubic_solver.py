import matplotlib.pyplot as plt
import cmath
import numpy as np


def cubic_solver(a, b, c, d):
        if a == 0:
            return {"error": "this is an Invalid Cubic Equation"}
        co_efficients = (a, b, c, d)
        roots = np.roots(co_efficients)
        real_roots = [r. real for r in roots if np.isreal(r)]
        complex_roots = [r for r in roots if not np.isreal(r)]

        return {
            "real_roots": real_roots,
            "complex_roots": complex_roots,
            "all_roots": roots
        }
    
def cubic_grapher(a, b, c, d):
    x_range = max(10, abs(a)*5 + abs(b)*2 + abs(c))  # Dynamic scaling
    x = np.linspace(-x_range, x_range, 400)
    y = (a * x ** 3) + (b * x ** 2) + (c * x) + d

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'{a}x³ + {b}x² + {c}x + {d}')
    plt.axhline(0, color='black', linewidth=0.5)  # x-axis
    plt.axvline(0, color='black', linewidth=0.5)  # y-axis
    plt.title("Graph of Cubic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()
