# Some parameters assigned by default if not assigned in the function (keyword arguments, e.g. num_ok=True means if you don't assign a value to num_ok, it will just be True automatically)

# Args:
# question (str)    question to ask user
# checklist (list)  list of valid answers
# error_msg (str)   statement to print for user when invalid answer
# num_ok (bool)     True: checks whether input is a positive number

# string checker from Mrs Gottschalk, edited so can have different error messages, got sister to help combine functions for efficiency
def input_checker(question, checklist=None, error_msg=None, num_ok=True):
# top sections is 'what it means'/ what it puts as the value, the bottom section is what it does
    if num_ok: # prints this error message if it goes to the while loop, if it's a negative number or blank
        error = "Please enter a number that is more than zero"
    else:
        error = error_msg # otherwise prints out the error msg in the function arguments

    while True: # for the whole thing, not the same as num_ok=True
        if num_ok: # since it's set to true, it will do this bc it allows numbers otherwise,
            # Check if number is valid measurement (positive)
            try:
                response = input(question).lower()
                # If it's a number need to convert string number to float number
                # If it's another character, trying to convert to float will fail and error out
                response = float(response)
                # if number is a negative or zero, it prints error msg otherwise it will use your answer as the response
                if response <= 0:
                    print(error)
                else:
                    return response

            except ValueError:
                # Typing a non-number answers goes here
                print(error)
                # After this line it just exits because of the "Error"

        else: # ** it goes to this since it can't have numbers and num_ok=false
            # Check if answer is in list
            response = input(question).lower()

            if response in checklist:
                return response
            else:
                print(error)
# Initialise lists
# shapes_lengths is the list for the individual shape's lengths added
shapes_lengths = []
shapes_list = ["circle", "square", "rectangle", "triangle", "trapezium", "parallelogram"]
# num_lengths is number next to these shapes, amount of times to ask for length
shapes_list = {"circle": 1,
               "square": 4,
               "rectangle": 4,
               "triangle": 3,
               "trapezium": 4,
               "parallelogram": 4}

# dimensions to calculate the perimeter
print("Enter the measurements (make sure they're in the same unit but don't include them) for your shape.")

# ask user what shape they need to find the area and/or perimeter for
print("Please choose from the following: \ncircle, square, rectangle, triangle, trapezium, parallelogram")
print()

ask_shape_a = input_checker("What shape would you like to find the area for? ",
                            error_msg="Please choose one of the shapes from the list!", num_ok=False,
                            checklist=shapes_list)

if ask_shape_a == "circle":
    r = input_checker("Radius: ")
    shapes_lengths.append(r)

elif ask_shape_a == "rectangle" or ask_shape_a == "square" or ask_shape_a == "triangle" or ask_shape_a == "parallelogram":
    base = input_checker("Base: ")
    height = input_checker("Height: ")
    shapes_lengths.append(base)
    shapes_lengths.append(height)

elif ask_shape_a == "trapezium":
    base = input_checker("Base: ")
    height = input_checker("Height: ")
    top_length = input_checker("Top length: ")
    shapes_lengths.append(base)
    shapes_lengths.append(height)
    shapes_lengths.append(top_length)

ask_shape_p = input_checker("What shape would you like to find the perimeter for? ",
                            error_msg="Please choose one of the shapes from the list!", num_ok=False,
                            checklist=shapes_list)

if ask_shape_p == "circle":
    r = input_checker("Radius: ")
    shapes_lengths.append(r)

elif ask_shape_p != "circle":
    num_lengths = shapes_list[ask_shape_p]
    # e.g. for i in [0,1,2,3] ..... range is a function that gives an array of numbers starting from 0

    # initialise counter outside the for loop
    perimeter = 0
    for i in range(num_lengths):
        # length is for each side of the shape
        length = input_checker("Length {}: ".format(i+1))
        shapes_lengths.append(length)

print(("Measurements: {}").format(shapes_lengths))
