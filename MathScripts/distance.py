import math

x1 = 3
x2 = 7
y1 = 4
y2 = 1

point_1 = (3,4)
point_2 = (7,1)

distance = math.sqrt((x2 -x1) ** 2 + (y2 - y1) ** 2)

print("The distance between points", str(point_1),"and",str(point_2), "is", float(distance))

import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

point1 = (3, 4)
point2 = (7, 1)

distance = calculate_distance(point1[0], point1[1], point2[0], point2[1])
print(f"The distance between points {point1} and {point2} is: {distance:.2f}")