import matplotlib.pyplot as plt
import cmath
import numpy as np

def cubic_solver(a, b, c, d):
    # Check if the equation is a valid cubic equation (a cannot be 0)
    if a == 0:
        return {"error": "this is an Invalid Cubic Equation"}
    
    # Define the coefficients for the cubic equation
    co_efficients = (a, b, c, d)
    
    # Use numpy's roots function to find the roots of the cubic equation
    roots = np.roots(co_efficients)
    
    # Separate real and complex roots
    real_roots = [r.real for r in roots if np.isreal(r)]  # Only real parts of real roots
    complex_roots = [r for r in roots if not np.isreal(r)]  # Complex roots

    # Return a dictionary with the real roots, complex roots, and all roots
    return {
        "real_roots": real_roots,
        "complex_roots": complex_roots,
        "all_roots": roots
    }
    
def cubic_grapher(a, b, c, d):
    # Dynamically scale the x-range based on the coefficients to avoid excessively large graphs
    x_range = max(10, abs(a)*5 + abs(b)*2 + abs(c))  # Ensure a reasonable range
    
    # Generate 400 points between -x_range and x_range for plotting the cubic curve
    # Calculate y-values based on the cubic equation
    x = np.linspace(-x_range, x_range, 400)
    y = (a * x ** 3) + (b * x ** 2) + (c * x) + d

    # Create a figure with custom size
    plt.figure(figsize=(10, 6))
    
    # Plot the cubic function curve
    plt.plot(x, y, label=f'{a}x³ + {b}x² + {c}x + {d}')
    
    # Add horizontal and vertical lines for the axes
    plt.axhline(0, color='red', linewidth=0.5)  # x-axis
    plt.axvline(0, color='red', linewidth=0.5)  # y-axis
    
    # Set the title and labels for the graph
    plt.title("Graph of Cubic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    
    # Enable grid for better visualization
    plt.grid(True)
    
    # Display the legend with the equation label
    plt.legend()
    
    # Show the plot
    plt.show()
