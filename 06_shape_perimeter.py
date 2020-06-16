# string checker from Mrs Gottschalk, edited so can have different error messages
def string_checker(question, error_msg, to_check, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question).lower()

        if response in to_check:
            return response
        else:
            print(error)

# *** Main Routine starts here ***

shapes_list = ["circle", "square", "rectangle", "triangle", "trapezium"]

pi= 3.14159265

# Initialise lists
# shapes_lengths is the list for the individual shape's lengths added
shapes_lengths = []

# ask user what shape they need to find the area and/or perimeter for
print("Please choose from the following: \ncircle, square, rectangle, triangle, trapezium")
print()

ask_shape = string_checker("What shape would you like to find the area and/or perimeter for? ",
                           "Please choose one of the shapes from the list!", shapes_list, "no")

if ask_shape == "circle":
    length_subtotal = 0
    for item in shapes_lengths:
        length_subtotal = 2*pi*item

if ask_shape != "circle":
    length_subtotal = 0
    for item in shapes_lengths:
        length_subtotal += item

print("Perimeter: {:.2f}".format(length_subtotal))




