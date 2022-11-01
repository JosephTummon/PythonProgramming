import math

while True:
        try:
            length = float(input("Please enter length: "))
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            break
height = length
radius = length 

#Area of square
area_square = length ** 2
print("Area of square with sides of length", length, "is", area_square)

#Volume of cube
volume_cube = length ** 3
print("Volume of cube with sides of length", length, "is", volume_cube)

#Area of circle 
area_circle = math.pi * (radius ** 2)
print("Area of circle with radius of length", length, "is", area_circle)

#Volume of sphere
volume_sphere = (4 / 3) * math.pi * (radius ** 3)
print("Volume of sphere with radius of length", length, "is", volume_sphere)

#Volume of cylinder 
volume_cylinder = math.pi * (radius ** 2) * height
print("Volumme of cylinder with radius and height of length", length, "is", volume_cylinder)

