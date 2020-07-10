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

# *** Main Routine starts here ***

shapes_list = ["circle", "square", "rectangle", "triangle", "trapezium", "parallelogram"]

# ask user what shape they need to find the area and/or perimeter for
print("Please choose from the following: \ncircle, square, rectangle, triangle, trapezium, parallelogram")
print()

ask_shape_a = string_checker("What shape would you like to find the area for? ", "Please choose one of the shapes from the list!", "no", shapes_list)
print(ask_shape_a)
ask_shape_p = string_checker("What shape would you like to find the perimeter for? ", "Please choose one of the shapes from the list!", "no", shapes_list)
print(ask_shape_p)