import matplotlib.pyplot as plt
import cmath
import numpy as np

def solve_quadratic(a, b, c):
    try:
        # Check if the equation is quadratic (a cannot be 0)
        if a == 0:
            return  {"error": "This is not a quadratic equation as 'A' cannot be 0."}
        
        # Calculate the discriminant to determine the nature of the roots
        discriminant = (b ** 2) - (4 * a * c)
        
        # Calculate the two roots using the quadratic formula
        root_1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root_2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        
        # Determine the nature of the roots based on the discriminant
        if discriminant > 0:
            nature = "Real and distinct roots"
        elif discriminant == 0:
            nature = "Real and equal roots"
        else: 
            nature = "Complex roots"

        # Return the roots and their nature along with the discriminant
        return {
            "root_1": root_1,
            "root_2": root_2,
            "nature": nature,
            "discriminant": discriminant
        }
    except Exception as e:
        # Catch any other errors and return them
        return {"error": f"An error occurred: {e}"}


def graph_quad(a, b, c):
    # Calculate the x-coordinate of the vertex of the parabola
    vertex_x = -b / (2 * a)

    # Wider x range for better visualization (zoom out)
    x_padding = 10  # You can adjust this value to control the zoom-out level
    x_values = np.linspace(vertex_x - x_padding, vertex_x + x_padding, 600)
    
    # Calculate the corresponding y-values for the quadratic function
    y_values = a * x_values**2 + b * x_values + c

    # Compute dynamic y padding for zooming out vertically
    y_min, y_max = min(y_values), max(y_values)
    y_range = y_max - y_min if y_max != y_min else 10
    y_padding = y_range * 0.4  # More padding = more zoom-out vertically

    # Create the plot
    plt.figure(figsize=(10, 5))
    
    # Plot the quadratic curve with a label
    plt.plot(x_values, y_values, label=f'{a}x² + {b}x + {c}', color='blue')
    
    # Add horizontal and vertical lines for the axes
    plt.axhline(0, color='red', linewidth=0.5)
    plt.axvline(0, color='red', linewidth=0.5)
    
    # Set the title and labels
    plt.title('Graph of the Quadratic Function')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Enable grid for better readability
    plt.grid(True)
    
    # Add a legend with the equation
    plt.legend()

    # Apply zoomed-out y limits for a better view of the parabola
    plt.ylim(y_min - y_padding, y_max + y_padding)

    # Show the plot
    plt.show()
