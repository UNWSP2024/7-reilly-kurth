#Reilly Kurth
#3/7/2025

import math

def points(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance

def main():
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        point1 = (x1, y1, z1)

        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))
        point2 = (x2, y2, z2)

        distance = points(point1, point2)

        print(f"The distance between {point1} and {point2} is: {distance}")
    except ValueError:
        print("Error: Invalid number entered for coordinate")

main()