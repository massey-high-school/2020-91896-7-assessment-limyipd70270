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

# *** Main Routine starts here ***
# Variables
shapes_list = ["circle", "c", "square", "s", "rectangle", "r", "triangle", "t", "trapezium", "z", "parallelogram", "p"]

all_history = []
pi= 3.14159265

# ask user what shape they need to find the area for
print("Please choose from the following: \ncircle (c), square (s), rectangle (r), triangle (t), trapezium (z), parallelogram (p)\n")

loop = True
while loop:
    # shapes_lengths is the list for the individual shape's lengths added
    shape_history = []
    ask_shape_a = input_checker("What shape would you like to find the area for? ", checklist=shapes_list,
                               error_msg="Please choose one of the shapes from the list!", num_ok=False)

    # append shape name to the history
    shape_history.append(ask_shape_a)

    if ask_shape_a == "circle" or ask_shape_a == "c":
        r = input_checker("Radius: ")
        area = pi*(r**2)
        shape_history.append(area)

    elif ask_shape_a == "rectangle" or ask_shape_a == "r" or ask_shape_a == "square" or ask_shape_a == "s" or ask_shape_a == "parallelogram" or ask_shape_a == "p":
        base = input_checker("Base: ")
        height = input_checker("Height: ")
        area = base * height
        shape_history.append(area)

    elif ask_shape_a == "triangle" or ask_shape_a == "t":
        base = input_checker("Base: ")
        height = input_checker("Height: ")
        area = (base * height)/2
        shape_history.append(area)

    elif ask_shape_a == "trapezium" or ask_shape_a == "z":
        base = input_checker("Base: ")
        height = input_checker("Height: ")
        top_length = input_checker("Top length: ")
        area = ((top_length + base) * height)/2
        shape_history.append(area)


    # don't need area=0 bc not adding onto previous numbers
    print("Area: {:.2f}".format(area))
    all_history.append(shape_history)
