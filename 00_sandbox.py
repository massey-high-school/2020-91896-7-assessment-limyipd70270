main_list = []

shape = ""
while shape != "xxx":

    shape_info = []

    shape = input("Shape: ")
    if shape.lower() == "xxx":
        break

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