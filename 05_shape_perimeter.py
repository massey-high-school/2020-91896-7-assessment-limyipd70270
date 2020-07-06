# string checker from Mrs Gottschalk, edited so can have different error messages
def string_checker(question, error_msg, num_ok, to_check):
    error = error_msg

    valid = False
    while not valid:
        response = input(question).lower()

        if response in to_check:
            return response
        else:
            print(error)

# Number checking function (number must be a float that is more than 0)
def num_check(question):
    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# *** Main Routine starts here ***

shapes_list = ["circle", "square", "rectangle", "triangle", "trapezium", "parallelogram"]

pi= 3.14159265

# Initialise lists
# shapes_lengths is the list for the individual shape's lengths added
all_lengths = []
shapes_lengths = [1, 2, 3]

# ask user what shape they need to find the area and/or perimeter for
print("Please choose from the following: \ncircle, square, rectangle, triangle, trapezium, parallelogram")
print()

ask_shape = string_checker("What shape would you like to find the area and/or perimeter for? ",
                           "Please choose one of the shapes from the list!", "no", shapes_list)
if ask_shape == "circle":
    r = num_check("Radius: ")
    perimeter = 0
    perimeter = 2*pi*r

if ask_shape != "circle":
    perimeter = 0
    for item in shapes_lengths:
        perimeter += item

print("Perimeter: {:.2f}".format(perimeter))
