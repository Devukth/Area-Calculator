# Area Calculator
pi = 3.14

print("Area Calculator")
print("What is the shape of your area?\n1 - Square\n2 - Circle\n3 - Triangle\n4 - Rectangle"
)
shape = int(input("> "))
def get_area_from_shape(shapeI):
    if (shapeI == 1):
        print("What is the length of the side?\n")
        side = float(input("> "))

        return (side * side)
    elif (shapeI == 2):
        print("What is the radius of the circle?\n")
        r = float(input("> "))

        return (pi * (r * r))
    elif (shapeI == 3):
        print("What is the width of the base of the triangle?\n")
        b = float(input("> "))
        print("What is the height of the triangle?\n")
        h = float(input("> "))

        return (0.5 * b * h)
    elif (shapeI == 4):
        print("What is the length of the rectangle?\n")
        l = float(input("> "))
        print("What is the breadth/width of the rectangle?\n")
        b = float(input("> "))

        return (l * b)
print(get_area_from_shape(shape))