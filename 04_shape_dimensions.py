import sys
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
                if response == "xxx":
                    sys.exit()
                else:
                    # If answer is not xxx, that means it is a number, or other characters
                    # If it's a number need to convert string number to float number
                    # If it's another character, trying to convert to float will fail and error out
                    response = float(response)
                # if number is a negative or zero, it prints error msg otherwise it will use your answer as the response
                if response <= 0:
                    print(error)
                else:
                    return response

            except ValueError:
                # Typing a non-number answers goes here, not including 'xxx'
                print("Please print 'xxx' to exit or a number above zero!")
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

# ask user what shape they need to find the area and/or perimeter for
print("Please choose from the following: \ncircle, square, rectangle, triangle, trapezium, parallelogram")
print()

ask_shape_a = input_checker("What shape would you like to find the area for? ",
                            error_msg="Please choose one of the shapes from the list!", num_ok=False,
                            checklist=shapes_list)

ask_shape_p = input_checker("What shape would you like to find the perimeter for? ",
                            error_msg="Please choose one of the shapes from the list!", num_ok=False,
                            checklist=shapes_list)

# dimensions to calculate the perimeter
print("Please enter the measurements (make sure they're in the same unit but don't include them) for your shape.")

loop = True
while loop:
    if ask_shape_a or ask_shape_p == "circle":
        # radius used for both area/perimeter
        r = input_checker("Radius: ")
        # print differently, not blank as int and num check as float, make all answers nicely as one of these types
        shapes_lengths.append(r)
        print(shapes_lengths)

    if ask_shape_p != "circle":
        length = ""
        while length != "xxx":
            length = input_checker("Length: ")
            # !!!!!!! all_lengths is for the history list, do i need to add different variable for when i add the lengths of area dimensions??????????
            # bc all_lengths would have ALL the lengths which some are repeated
            shapes_lengths.append(length)

    if ask_shape_a != "circle":
        base = input_checker("Base: ")
        height = input_checker("Height: ")
        top_length = input_checker("Top length: ")

        # put in the lists for printing for history
        shapes_lengths.append(base)
        shapes_lengths.append(height)
        shapes_lengths.append(top_length)

    print(shapes_lengths)
    # swap ask_PA and shape dimensions, and renumber to add the 3 as a component


