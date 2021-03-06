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
# num_lengths is number next to these shapes, amount of times to ask for length
shapes_list = {"circle": 1,
               "c": 1,
               "square": 4,
               "s": 4,
               "rectangle": 4,
               "r": 4,
               "triangle": 3,
               "t": 3,
               "trapezium": 4,
               "z": 4,
               "parallelogram": 4,
               "p": 4}
pi= 3.14159265

# Initialise lists
# all_lengths includes every shapes' dimensions
all_history = []

# ask user what shape they need to find the perimeter for
print("Please choose from the following: \ncircle (c), square (s), rectangle (r), triangle (t), trapezium (z), parallelogram (p)\n")

loop = True
while loop:
    # shapes_lengths is the list for the individual shape's lengths added
    shape_history = []
    ask_shape_p = input_checker("What shape would you like to find the perimeter for? ", checklist=shapes_list,
                               error_msg="Please choose one of the shapes from the list!", num_ok=False)

    # append shape name to the history
    shape_history.append(ask_shape_p)

    if ask_shape_p == "circle" or ask_shape_p == "c":
        r = input_checker("Radius: ")
        perimeter = 2*pi*r
        shape_history.append(perimeter)

    elif ask_shape_p != "circle" or ask_shape_p != "c":
        print()
        print("Please enter the lengths (don't need to include the unit of measurement) for your shape, pressing 'enter' after each one.")

        num_lengths = shapes_list[ask_shape_p]
        # e.g. for i in [0,1,2,3] ..... range is a function that gives an array of numbers starting from 0

        # initialise counter outside the for loop
        perimeter = 0
        for i in range(num_lengths):
            # length is for each side of the shape
            length = input_checker("Length {}: ".format(i+1))
            perimeter += length
        shape_history.append(perimeter)

    print("Perimeter: {:.2f}".format(perimeter))
    all_history.append(shape_history)

    print()
    rerun = input_checker("Would you like to calculate the perimeter for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N", num_ok=False)
    print()
    if rerun == "n":
        loop = False

for item in all_history:
    print("{}: {:.2f}".format(item[0], item[1]))
