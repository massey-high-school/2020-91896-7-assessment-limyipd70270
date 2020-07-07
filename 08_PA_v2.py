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
        error = "Please enter a number that is more than zero!"
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
# Initialise lists
# all_lengths includes every shapes' dimensions
all_p_history = []
all_a_history = []

# num_lengths is number next to these shapes, amount of times to ask for length
shapes_list = {"circle": 1, "c": 1, "square": 4, "s": 4, "rectangle": 4, "r": 4, "triangle": 3, "t": 3, "trapezium": 4, "z": 4, "parallelogram": 4, "p": 4}

units_list = ["mm", "millimeters", "millimetres", "cm", "centimeters", "centimetres", "m", "meters", "metres", "km", "kilometers", "kilometres"]
mm = ["mm", "millimeters", "millimetres"]
cm = ["cm", "centimeters", "centimetres"]
m = ["m", "meters", "metres"]
km = ["km", "kilometers", "kilometres"]
pi= 3.14159265

print ("========================= Welcome to the Perimeter/Area Calculator! =========================\n"
       "\nDon't leave anything blank and press 'enter' after each answer. Please make sure that the\n"
       "measurements you enter for each shape are numbers above zero and in the same units! All the \n"
       "perimeters/areas will be rounded to 2s.f.\n"
       "\n=============================================================================================\n")


print("Please choose from the following: \ncircle (c), square (s), rectangle (r), triangle (t), trapezium (z), parallelogram (p)\n")

ask_p = input_checker("Would you like to find the perimeter? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)

if ask_p == "y":
    loop = True
    while loop:
        # shapes_lengths is the list for the individual shape's lengths added
        shape_p_hist = []
        shape_p = input_checker("Shape: ", error_msg="Please choose one of the shapes from the list!", num_ok=False, checklist=shapes_list)

        if shape_p == "c":
            shape_p = "circle"
        elif shape_p == "s":
            shape_p = "square"
        elif shape_p == "r":
            shape_p = "rectangle"
        elif shape_p == "t":
            shape_p = "triangle"
        elif shape_p == "z":
            shape_p = "trapezium"
        elif shape_p == "p":
            shape_p = "parallelogram"
        shape_p_hist.append(shape_p)

        unit = input_checker("Unit: ", checklist=units_list, error_msg="Please enter a valid unit!", num_ok=False)
        if unit in mm:
            unit = "mm"
        elif unit in cm:
            unit = "cm"
        elif unit in m:
            unit = "m"
        elif unit in km:
            unit = "km"
        shape_p_hist.append(unit)

        if shape_p == "circle" or shape_p == "c":
            r = input_checker("Radius: ")
            perimeter = 2*pi*r
            shape_p_hist.append(perimeter)

        elif shape_p != "circle" or shape_p != "c":
            num_lengths = shapes_list[shape_p]
            # e.g. for i in [0,1,2,3] ..... range is a function that gives an array of numbers starting from 0
            # initialise counter outside the for loop
            perimeter = 0
            for i in range(num_lengths):
                # length is for each side of the shape
                length = input_checker("Length {}: ".format(i+1))
                perimeter += length
            shape_p_hist.append(perimeter)

        print("Perimeter: {:.2f}{}".format(perimeter, unit))
        all_p_history.append(shape_p_hist)
        print("==============================================")

        rerun = input_checker("Would you like to calculate the perimeter for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
        if rerun == "n":
            loop = False

else:
    loop = False

ask_a = input_checker("Would you like to find the area? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
bh_list = ["rectangle", "r", "square", "s", "parallelogram", "p"]

if ask_a == "y":
    loop = True
    while loop:
        # shapes_lengths is the list for the individual shape's lengths added
        shape_a_hist = []
        shape_a = input_checker("Shape: ", checklist=shapes_list, error_msg="Please choose one of the shapes from the list!", num_ok=False)

        if shape_a == "c":
            shape_a = "circle"
        elif shape_a == "s":
            shape_a = "square"
        elif shape_a == "r":
            shape_a = "rectangle"
        elif shape_a == "t":
            shape_a = "triangle"
        elif shape_a == "z":
            shape_a = "trapezium"
        elif shape_a == "p":
            shape_a = "parallelogram"
        shape_a_hist.append(shape_a)

        unit = input_checker("Unit: ", checklist=units_list, error_msg="Please enter a valid unit!", num_ok=False)
        if unit in mm:
            unit = "mm"
        elif unit in cm:
            unit = "cm"
        elif unit in m:
            unit = "m"
        elif unit in km:
            unit = "km"
        shape_a_hist.append(unit)

        if shape_a == "circle" or shape_a == "c":
            r = input_checker("Radius: ")
            area = pi*(r**2)
            shape_a_hist.append(area)

        elif shape_a in bh_list:
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            area = base * height
            shape_a_hist.append(area)

        elif shape_a == "triangle" or shape_a == "t":
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            area = (base * height)/2
            shape_a_hist.append(area)

        elif shape_a == "trapezium" or shape_a == "z":
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            top_length = input_checker("Top length: ")
            area = ((top_length + base) * height)/2
            shape_a_hist.append(area)

        # don't need area=0 bc not adding onto previous numbers
        print("Area: {:.2f}{}".format(area, unit))
        all_a_history.append(shape_a_hist)
        print("==============================================")

        rerun = input_checker("Would you like to calculate the area for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
        if rerun == "n":
            loop = False

else:
    loop = False

history_ask = input_checker("Would you like a history of your previously calculated perimeters/areas? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
print("===========================================================================")
if ask_p == "y":
    if history_ask != "n":
        print("Perimeter History:")
        for item in all_p_history:
            print("{}: {:.2f}{}".format(item[0], item[2], item[1]))
print()
if ask_a == "y":
    if history_ask != "n":
        print("Area History:")
        for item in all_a_history:
            print("{}: {:.2f}{}".format(item[0], item[2], item[1]))

# blank test
# what is shape history, is it needed bc it keeps all the info for each shape 'together'
# change the ask pa bc doesn't give both as an option
