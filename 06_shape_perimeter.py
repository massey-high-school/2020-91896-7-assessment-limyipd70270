pi= 3.14159265

# Initialise lists
# shapes_lengths is the list for the individual shape's lengths added
shapes_lengths = [2, 3]
shapes_list = ["circle", "square", "rectangle", "triangle", "trapezium"]
ask_shape = input("What shape would you like to find the area and/or perimeter for? ")

if ask_shape == "circle":
    length_subtotal = 0
    for item in shapes_lengths:
        length_subtotal = 2*pi*item[0]

if ask_shape != "circle":
    length_subtotal = 0
    for item in shapes_lengths:
        length_subtotal += item[0]

print("Perimeter: {:.2f}".format(length_subtotal))




