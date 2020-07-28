# Functions go here


# Number checker

# Unit checker

# Shape checker

# quad area
def quad_area(length, width):
    area = length * width
    return area

def quad_perim(length, width):
    perim = 2 * (length + width)
    return perim

# square perimeter






main_list = []

shape = ""
while shape != "xxx":

    shape_info = []

    shape = input("Shape: ")
    if shape.lower() == "xxx":
        break

    if shape == "square":
        width = int(input("Width: "))
        dimensions = "{} x {}".format(width, width)
        area = quad_area(width, width)
        perimeter = quad_perim(width, width)

    if shape == "triangle":
        apb = input("area / perimeter / both")
        if apb == "area":
            perimeter = "n/a"
        elif apb == "perimeter":
            area = "n/a"

    shape_info.append(shape)
    shape_info.append(dimensions)
    shape_info.append(area)
    shape_info.append(perimeter)

    main_list.append(shape_info)

    width = float(input("Width: "))
    dimensions = "width: {}".format(width)

    area = width * width
    perimeter = width * 4

    shape_info.append(shape)
    shape_info.append(dimensions)
    shape_info.append(area)
    shape_info.append(perimeter)

    main_list.append(shape_info)


# print it!
print("Shape Info")
print(shape_info)

print()
print("History")
for item in main_list:
    print("Shape: {}".format(item[0]))
    print("Dimensions: {}".format(item[1]))