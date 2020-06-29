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

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
        else:
            return response

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
# all_lengths includes every shapes' dimensions
all_lengths = []
# shapes_lengths is the list for the individual shape's lengths added
shapes_lengths = [1, 2, 3]

# ask user what shape they need to find the area and/or perimeter for
print("Please choose from the following: \ncircle, square, rectangle, triangle, trapezium, parallelogram")
print()

ask_shape = string_checker("What shape would you like to find the area and/or perimeter for? ",
                           "Please choose one of the shapes from the list!", "no", shapes_list)
# !!!!!!!!! what if they have a square which have the same measurements on all sides, would they put the 4 lengths repeated or just once?
if ask_shape == "circle":
    r = num_check("Radius: ")
    perimeter = 0
    perimeter = 2*pi*r

if ask_shape != "circle":
    print("Please enter the lengths (don't need to include the unit of measurement) for your shape, pressing 'enter' after each one. Print 'xxx' once you have entered all of them")

    length = ""
    while length != "xxx":
        # length is for each side of the shape
        length = not_blank("Length: ", "Please enter a number that is more than zero", "yes")

        # If user enters exit code, break out of loop
        if length == "xxx":
            break

        shapes_lengths.append(length)
        all_lengths.append(shapes_lengths)

        perimeter = 0
        for item in shapes_lengths:
            perimeter += item


print("Perimeter: {:.2f}".format(perimeter))
# !!!!!!!!! does it matter that there's no limit to lengths entered even if shape doesn't have that many lengths, e.g. 3 entered for square or 2 entered for circle

