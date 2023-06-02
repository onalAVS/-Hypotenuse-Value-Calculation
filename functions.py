import math

def calculate_circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area

# Example usage
radius = float(input("Enter the radius of the circle: "))
circle_perimeter, circle_area = calculate_circle(radius)

print("Perimeter of the circle:", circle_perimeter)
print("Area of the circle:", circle_area)
