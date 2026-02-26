import math

x1 = int(input("Enter coordinate value x1:"))
x2 = int(input("Enter coordinate value x2:"))
y1 = int(input("Enter coordinate value y1:"))
y2 = int(input("Enter coordinate value y2:"))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(distance)