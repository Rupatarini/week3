import numpy as np
def manhattan(x1, x2, y1, y2):
    return np.abs(x2 - x1) + np.abs(y2 - y1)
x1, y1 = map(int, input("Enter coordinates (x, y) for the first point, separated by space: ").split())
x2, y2 = map(int, input("Enter coordinates (x, y) for the second point, separated by space: ").split())
point1 = np.array([x1, y1])
point2 = np.array([x2, y2])
print("Points entered by the user:")
print("Point 1:", point1)
print("Point 2:", point2)
distance = manhattan(x1, x2, y1, y2)
print(f"Manhattan distance between the two points is {distance}")
