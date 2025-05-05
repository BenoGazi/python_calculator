import matplotlib.pyplot as plt
import cmath
import numpy as np


def solve_quadratic(a, b, c):
    try:
        if a == 0:
            return  {"error": "This is not a quardratic equation as 'A' cannot be 0."}
        discriminant = (b ** 2) - (4 * a * c)
        root_1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root_2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        if discriminant > 0:
            nature = "Real and distinct roots"
        elif discriminant == 0:
            nature = "Real and equal roots"
        else: 
            nature = "Complex roots"

        return {
            "root_1": root_1,
            "root_2": root_2,
            "nature": nature,
            "discriminant": discriminant
        }
    except Exception as e:
        return {"error": f"An error occurred: {e}"}


def graph_quad(a, b, c):
    vertex_x = -b / (2 * a)

    # Wider x range for zoom-out
    x_padding = 10  # You can increase this to 15 or 20 if needed
    x_values = np.linspace(vertex_x - x_padding, vertex_x + x_padding, 600)
    y_values = a * x_values**2 + b * x_values + c

    # Compute dynamic y padding
    y_min, y_max = min(y_values), max(y_values)
    y_range = y_max - y_min if y_max != y_min else 10
    y_padding = y_range * 0.4  # More padding = more zoom-out vertically

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, label=f'{a}x² + {b}x + {c}', color='blue')
    plt.axhline(0, color='red', linewidth=0.5)
    plt.axvline(0, color='red', linewidth=0.5)
    plt.title('Graph of the Quadratic Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

    # Apply zoomed-out y limits
    plt.ylim(y_min - y_padding, y_max + y_padding)

    plt.show()