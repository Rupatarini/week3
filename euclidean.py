import math
def euclidean_distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
points_count = int(input("Enter the number of points: "))
points = []
for i in range(points_count):
    x = int(input("Enter the x value for point : "))
    y = int(input("Enter the y value for point : "))
    points.append((x, y))
if len(points) < 2:
    print("At least two points are required to calculate the distance.")
else:
    x1, y1 = points[0]
    x2, y2 = points[1]
    distance = euclidean_distance(x1, x2, y1, y2)
    print("The Euclidean distance between the first two points is:", distance)
