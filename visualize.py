import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Define constraint lines
x = np.linspace(0, 1000, 1000)

# Constraint 1: x + y <= 800 => y <= 800 - x
y1 = 800 - x

# Constraint 2: x <= 400 (vertical line)
x2 = 400

# Constraint 3: y <= 700 (horizontal line)
y3 = 700

# Plot constraint lines
ax.plot(x, y1, 'r-', label='x + y = 800', linewidth=2)
ax.axvline(x=400, color='g', linestyle='-', label='x = 400', linewidth=2)
ax.axhline(y=700, color='b', linestyle='-', label='y = 700', linewidth=2)

# Define the feasible region by finding corner points
corner_points = [
    (0, 0),      # Origin
    (400, 0),    # Intersection of x=400 and y=0
    (400, 400),  # Intersection of x=400 and x+y=800
    (100, 700),  # Intersection of y=700 and x+y=800
    (0, 700),    # Intersection of y=700 and x=0
]

# Extract x and y coordinates for polygon
poly_x = [p[0] for p in corner_points]
poly_y = [p[1] for p in corner_points]

# Fill the feasible region
ax.fill(poly_x, poly_y, alpha=0.3, color='yellow', label='Feasible Region')

# Plot corner points
for point in corner_points:
    ax.plot(point[0], point[1], 'ko', markersize=8)
    ax.annotate(f'{point}', xy=point, xytext=(5, 5), textcoords='offset points', fontsize=9)

# Calculate objective function value at each corner point
print("Objective function values at corner points:")
print("=" * 50)
for point in corner_points:
    obj_value = 3*point[0] + 4*point[1]
    print(f"Point {point}: 3*{point[0]} + 4*{point[1]} = {obj_value}")

# Find optimal solution (maximum)
optimal_point = max(corner_points, key=lambda p: 3*p[0] + 4*p[1])
optimal_value = 3*optimal_point[0] + 4*optimal_point[1]

# Plot optimal solution
ax.plot(optimal_point[0], optimal_point[1], 'r*', markersize=20, label=f'Optimal: {optimal_point} (Z={optimal_value})')

# Plot objective function direction
# Objective: 3x + 4y = k, for different values of k
for k in [1000, 2000, 3000, optimal_value]:
    y_obj = (k - 3*x) / 4
    if k == optimal_value:
        ax.plot(x, y_obj, 'r--', linewidth=2, alpha=0.8, label=f'Objective: 3x+4y={k}')
    else:
        ax.plot(x, y_obj, 'gray', linestyle='--', alpha=0.3)

# Set axis limits and labels
ax.set_xlim(-50, 900)
ax.set_ylim(-50, 900)
ax.set_xlabel('x', fontsize=12, fontweight='bold')
ax.set_ylabel('y', fontsize=12, fontweight='bold')
ax.set_title('Linear Programming: Belt Problem - Feasible Region & Optimal Solution', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.savefig('feasible_solution.png', dpi=150, bbox_inches='tight')
print("\n" + "=" * 50)
print(f"✓ Optimal Solution: x = {optimal_point[0]}, y = {optimal_point[1]}")
print(f"✓ Maximum Objective Value: {optimal_value}")
print("=" * 50)
print("\nVisualization saved as 'feasible_solution.png'")
plt.show()
