# https://treyhunner.com/2018/04/keyword-arguments-in-python/#What_are_keyword_arguments?
# Some arguments have a default if not assigned in the function (e.g. num_ok=True means it will just be True automatically if you don't assign a value to num_ok)
# question (str): question to ask user, checklist (list): list of valid answers, error_msg (str): print statement when invalid answer entered, num_ok (bool): True- checks if it's a positive number

# string checker from Mrs GK, combined with num_checker, got sister to help combine functions for efficiency
def input_checker(question, checklist=None, error_msg=None, num_ok=True):
    if num_ok: # prints this error msg in while loop if num_ok=True
        error = "Please enter a number that is more than zero!"
    else:
        error = error_msg # otherwise prints out error_msg set in the arg when num_ok=False
    while True: # not the same as num_ok=True!! just means this will keep looping
        if num_ok: # since num_ok=True (allows numbers), checks if number is valid measurement (positive)
            try:
                response = input(question).lower()
                response = float(response) # If it's a number, need to convert 'string' number to 'float' number which is why they 'equal' each other
                if response <= 0: # if number is negative/zero, prints error msg, otherwise it uses valid answer as the response
                    print(error)
                else:
                    return response

            except ValueError:
                # Typing a non-number answers goes here bc converting to float will fail and error out
                print(error)

        else: # it checks if answer is in a list instead since it can't have numbers (num_ok=false)
            response = input(question).lower()
            if response in checklist:
                return response
            else:
                print(error)

# *** Main Routine starts here ***
# Initialise lists
all_p_history = []
all_a_history = []
# https://www.w3schools.com/python/python_dictionaries.asp, num_lengths is no. next to each shape (amount of times to ask for length)
shapes_list = {"circle": 1, "c": 1, "square": 1, "s": 1, "rectangle": 0, "r": 0, "triangle": 3, "t": 3, "trapezium": 4, "z": 4, "parallelogram": 0, "p": 0}
units_list = ["mm", "millimeters", "millimetres", "millimeter", "millimetre", "cm", "centimeters", "centimetres", "centimeter", "centimetre",
              "m", "meters", "metres", "meter", "metre", "km", "kilometers", "kilometres", "kilometer", "kilometre"]
mm = ["mm", "millimeters", "millimetres", "millimeter", "millimetre"]
cm = ["cm", "centimeters", "centimetres", "centimeter", "centimetre"]
m = ["m", "meters", "metres", "meter", "metre"]
km = ["km", "kilometers", "kilometres", "kilometer", "kilometre"]
pi= 3.14159265

# INSTRUCTIONS/INTRO
print ("=========================== Welcome to the Perimeter/Area Calculator! ===========================\n")
PA_user = input_checker("Have you used this Perimeter/Area Calculator before? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N", num_ok=False)
if PA_user == "n":
    print("\nThis tool helps you to calculate the perimeter and/or area for multiple different shapes\n(listed below) and your calculation history may be printed at the end if you wish. You can\n"
    "calculate the perimeter of different shapes unless you say 'n', and then you can calculate the\narea of different shapes. Each time you will have to enter the shape's info, just type your answer\n"
    "at the end of each question then press 'enter', and don't leave anything blank! Please make sure\nthat the measurements you enter for each shape are numbers above zero and each length is in the\n"
    "same unit! All the perimeters/areas will be rounded to 2s.f.\n"
    "\nShape choices: \ncircle (c), square (s), rectangle (r), triangle (t), trapezium (z), parallelogram (p)\nUnit choices: \nmillimetres (mm), centimetres (cm), metres (m), kilometres (km)")
else:
    print("\nShape choices: \ncircle (c), square (s), rectangle (r), triangle (t), trapezium (z), parallelogram (p)\nUnit choices: \nmillimetres (mm), centimetres (cm), metres (m), kilometres (km)")
print("\n=================================================================================================")

# PERIMETER
ask_p = input_checker("Would you like to find the perimeter of a shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
r_p_list = ["rectangle", "r", "parallelogram", "p"]

if ask_p == "y":
    loop = True
    while loop:
        shape_p_hist = [] # shape_p_hist is the list for the individual shape's perimeter, unit and shape name
        shape_p = input_checker("Shape: ", error_msg="Please choose one of the shapes from the list!", num_ok=False, checklist=shapes_list)
        if shape_p == "c": # these allow for the letters associated with the shape
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
        if unit in mm: # these make sure the abbreviations are printed no matter what the input is
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

        elif shape_p in r_p_list:
            length_1 = input_checker("Length 1: ")
            length_2= input_checker("Length 2: ")
            perimeter = 2*length_1 + 2*length_2
            shape_p_hist.append(perimeter)

        elif shape_p == "square" or shape_p == "s":
            length = input_checker("Length: ")
            perimeter = length*4
            shape_p_hist.append(perimeter)

        elif shape_p != "circle" or shape_p != "c": # https://www.w3schools.com/python/ref_func_range.asp got sister to help/explain
            num_lengths = shapes_list[shape_p] # the no. next to the shapes in shapes_list, https://www.iteanz.com/tutorials/python/accessing-values-in-dictionary/
            perimeter = 0 # need perimeter=0 bc adding onto previous numbers, outside 'for' loop bc if it was in, each time it asks for the length, perimeter would go back to zero and won't add
            for i in range(num_lengths): # gets number associated with the shape chosen
                length = input_checker("Length {}: ".format(i+1)) # increases each time it asks for length
                perimeter += length
            shape_p_hist.append(perimeter) # the no. next to the shapes is the nth number in the i array/range since i starts from zero,
            # e.g. triangle:3, i=2 bc 2 is 3rd number in i range/array, for {} in Length: to be printed, it must be i+1, but technically
            # '3' is the amount of times to ask for the length

        print("Perimeter: {:.2f}{}".format(perimeter, unit))
        all_p_history.append(shape_p_hist)
        print("=================================================================================================")

        rerun = input_checker("Would you like to calculate the perimeter for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
        if rerun == "n":
            loop = False
else:
    loop = False

# AREA
ask_a = input_checker("Would you like to find the area of a shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
bh_list = ["rectangle", "r", "parallelogram", "p"]

if ask_a == "y":
    loop = True
    while loop:
        shape_a_hist = [] # shape_a_hist is the list for the individual shape's area, unit and shape name
        shape_a = input_checker("Shape: ", checklist=shapes_list, error_msg="Please choose one of the shapes from the list!", num_ok=False)
        if shape_a == "c": # these allow for the letters associated with the shape
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
        if unit in mm: # these make sure the abbreviations are printed no matter what the input is
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

        elif shape_a == "square" or shape_a == "s":
            side = input_checker("Side: ")
            area = side**2
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

        print("Area: {:.2f}{}\u00b2".format(area, unit))
        all_a_history.append(shape_a_hist)
        print("=================================================================================================")

        rerun = input_checker("Would you like to calculate the area for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
        if rerun == "n":
            loop = False
else:
    loop = False

# HISTORY
history_ask = input_checker("Would you like the history of your previously calculated perimeters/areas? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
print("=================================================================================================")
if ask_p == "y":
    if history_ask == "y":
        print("Perimeter History:")
        for item in all_p_history:
            print("{}: {:.2f}{}".format(item[0], item[2], item[1]).capitalize())
    print()
if ask_a == "y":
    if history_ask == "y":
        print("Area History:")
        for item in all_a_history: # https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-43.php?fbclid=IwAR0-h5EDQvSts6db5OHIWqtQ_fQmO_Cex69sNV-9tqngW0lSSfBONt0woNI
            print("{}: {:.2f}{}\u00b2".format(item[0], item[2], item[1]).capitalize())
print("\nThank you for using the Perimeter/Area Calculator!")
