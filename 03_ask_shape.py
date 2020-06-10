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

# string checker from Mrs Gottschalk
def string_checker(question, to_check):
    valid = False
    while not valid:
        response = input(question).lower()

        if response in to_check:
            return response
        else:
            print("Please choose one of the shapes from the list!")

# *** Main Routine starts here ***

shapes_list = ["circle", "square", "rectangle", "triangle", "trapezium"]

# ask user what shape they need to find the area and/or perimeter for
print("Please choose from the following: \ncircle, square, rectangle, triangle, trapezium")
print()

ask_shape = string_checker("What shape would you like to find the area and/or perimeter for? ", shapes_list)
