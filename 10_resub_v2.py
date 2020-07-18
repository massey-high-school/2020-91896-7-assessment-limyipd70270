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
PA_user = input_checker("Have you used this Perimeter/Area Calculator before? (Y/N) ", checklist=["y", "yes", "n", "no"], error_msg="Please enter Y or N", num_ok=False)
if PA_user == "n" or PA_user == "no":
    print("\nThis tool helps you to calculate the perimeter and/or area for multiple different shapes (listed \nbelow) and your calculation history may be printed at the end if you wish. You can choose a\n"
    "shape and then choose to calculate the area, perimeter or both. Each time you will have to enter\nthe unit and measurements, just type your answer at the end of each question then press 'enter',\n"
    "and don't leave anything blank! Please make sure that the measurements you enter for each shape\nare numbers above zero and each length is in the same unit! All the perimeters/areas will be\nrounded to 2s.f.\n"
    "\nShape choices: \ncircle (c), square (s), rectangle (r), triangle (t), trapezium (z), parallelogram (p)\nUnit choices: \nmillimetres (mm), centimetres (cm), metres (m), kilometres (km)")
else:
    print("\nShape choices: \ncircle (c), square (s), rectangle (r), triangle (t), trapezium (z), parallelogram (p)\nUnit choices: \nmillimetres (mm), centimetres (cm), metres (m), kilometres (km)")
print("\n=================================================================================================")

loop = True
while loop:
    shape_p_hist = [] # shape_p_hist is the list for the individual shape's perimeter, unit and shape name
    shape_a_hist = [] # shape_a_hist is the list for the individual shape's area, unit and shape name
    p_shape_lengths = []
    a_shape_lengths = []
    shape = input_checker("Shape: ", error_msg="Please choose one of the shapes from the list!", num_ok=False, checklist=shapes_list)
    if shape == "c": # these allow for the letters associated with the shape
        shape = "circle"
    elif shape == "s":
        shape = "square"
    elif shape == "r":
        shape = "rectangle"
    elif shape == "t":
        shape = "triangle"
    elif shape == "z":
        shape = "trapezium"
    elif shape == "p":
        shape = "parallelogram"
    shape_p_hist.append(shape), shape_a_hist.append(shape)

    pab_ask = input_checker("Would you like to find the perimeter (P), area (A) or both (B)? ", checklist=["p", "perimeter", "a", "area", "b", "both"], error_msg="Please enter P, A or B!", num_ok=False)
    if pab_ask == "p" or pab_ask == "perimeter":
        r_p_list = ["rectangle", "r", "parallelogram", "p"]
        print("PERIMETER")
        loop = True
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

        if shape == "circle" or shape == "c":
            raw_r = input_checker("Radius: ")
            r = "Radius: {}".format(raw_r)
            perimeter = 2*pi*raw_r
            shape_p_hist.append(r), shape_p_hist.append(perimeter)

        elif shape == "square" or shape == "s":
            raw_side = input_checker("Side: ")
            side = "Side: {}".format(raw_side)
            perimeter = raw_side*4
            shape_p_hist.append(side), shape_p_hist.append(perimeter)

        elif shape in r_p_list:
            length_1 = input_checker("Length 1: ")
            length_2= input_checker("Length 2: ")
            p_shape_lengths.append(length_1), p_shape_lengths.append(length_2)
            perimeter = 2*length_1 + 2*length_2
            shape_p_hist.append(p_shape_lengths), shape_p_hist.append(perimeter)

        elif shape != "circle" or shape != "c": # https://www.w3schools.com/python/ref_func_range.asp got sister to help/explain
            num_lengths = shapes_list[shape] # the no. next to the shapes in shapes_list, https://www.iteanz.com/tutorials/python/accessing-values-in-dictionary/
            perimeter = 0 # need perimeter=0 bc adding onto previous numbers, outside 'for' loop bc if it was in, each time it asks for the length, perimeter would go back to zero and won't add
            for i in range(num_lengths): # gets number associated with the shape chosen
                length = input_checker("Length {}: ".format(i+1)) # increases each time it asks for length
                p_shape_lengths.append(length)
                perimeter += length
            shape_p_hist.append(p_shape_lengths), shape_p_hist.append(perimeter) # the no. next to the shapes is the nth number in the i array/range since i starts from zero,
            # e.g. triangle:3, i=2 bc 2 is 3rd number in i range/array, for {} in Length: to be printed, it must be i+1, but technically
            # '3' is the amount of times to ask for the length
        print("{}'s Perimeter: {:.2f}{}".format(shape, perimeter, unit).capitalize())
        all_p_history.append(shape_p_hist)
        print("=================================================================================================")
        rerun = input_checker("Would you like to calculate the perimeter/area for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
        if rerun == "n":
            loop = False

    if pab_ask == "a" or pab_ask == "area":
        bh_list = ["rectangle", "r", "parallelogram", "p"]
        print("AREA")
        loop = True
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

        if shape == "circle" or shape == "c":
            raw_r = input_checker("Radius: ")
            r = "Radius: {}".format(raw_r)
            area = pi*(raw_r**2)
            shape_a_hist.append(r), shape_a_hist.append(area)

        elif shape == "square" or shape == "s":
            raw_side = input_checker("Side: ")
            side = "Side: {}".format(raw_side)
            area = raw_side**2
            shape_a_hist.append(side), shape_a_hist.append(area)

        elif shape in bh_list:
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            a_shape_lengths.append(base), a_shape_lengths.append(height)
            area = base * height
            shape_a_hist.append(a_shape_lengths), shape_a_hist.append(area)

        elif shape == "triangle" or shape == "t":
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            a_shape_lengths.append(base), a_shape_lengths.append(height)
            area = (base * height)/2
            shape_a_hist.append(a_shape_lengths), shape_a_hist.append(area)

        elif shape == "trapezium" or shape == "z":
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            top_length = input_checker("Top length: ")
            a_shape_lengths.append(base), a_shape_lengths.append(height), a_shape_lengths.append(top_length)
            area = ((top_length + base) * height)/2
            shape_a_hist.append(a_shape_lengths), shape_a_hist.append(area)
        print("{}'s Area: {:.2f}{}\u00b2".format(shape, area, unit).capitalize())
        all_a_history.append(shape_a_hist)
        print("=================================================================================================")

        rerun = input_checker("Would you like to calculate the perimeter/area for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
        if rerun == "n":
            loop = False

    if pab_ask == "b" or pab_ask == "both":
        r_p_list = ["rectangle", "r", "parallelogram", "p"]
        print("PERIMETER")
        loop = True
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

        if shape == "circle" or shape == "c":
            raw_r = input_checker("Radius: ")
            r = "Radius: {}".format(raw_r)
            perimeter = 2*pi*raw_r
            shape_p_hist.append(r), shape_p_hist.append(perimeter)

        elif shape == "square" or shape == "s":
            raw_side = input_checker("Side: ")
            side = "Side: {}".format(raw_side)
            perimeter = raw_side*4
            shape_p_hist.append(side), shape_p_hist.append(perimeter)

        elif shape in r_p_list:
            length_1 = input_checker("Length 1: ")
            length_2= input_checker("Length 2: ")
            p_shape_lengths.append(length_1), p_shape_lengths.append(length_2)
            perimeter = 2*length_1 + 2*length_2
            shape_p_hist.append(p_shape_lengths), shape_p_hist.append(perimeter)

        elif shape != "circle" or shape != "c": # https://www.w3schools.com/python/ref_func_range.asp got sister to help/explain
            num_lengths = shapes_list[shape] # the no. next to the shapes in shapes_list, https://www.iteanz.com/tutorials/python/accessing-values-in-dictionary/
            perimeter = 0 # need perimeter=0 bc adding onto previous numbers, outside 'for' loop bc if it was in, each time it asks for the length, perimeter would go back to zero and won't add
            for i in range(num_lengths): # gets number associated with the shape chosen
                length = input_checker("Length {}: ".format(i+1)) # increases each time it asks for length
                p_shape_lengths.append(length)
                perimeter += length
            shape_p_hist.append(p_shape_lengths), shape_p_hist.append(perimeter) # the no. next to the shapes is the nth number in the i array/range since i starts from zero,
            # e.g. triangle:3, i=2 bc 2 is 3rd number in i range/array, for {} in Length: to be printed, it must be i+1, but technically
            # '3' is the amount of times to ask for the length
        print("{}'s Perimeter: {:.2f}{}".format(shape, perimeter, unit).capitalize())
        all_p_history.append(shape_p_hist)
        print("=================================================================================================")

        bh_list = ["rectangle", "r", "parallelogram", "p"]
        print("AREA")
        loop = True
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

        if shape == "circle" or shape == "c":
            raw_r = input_checker("Radius: ")
            r = "Radius: {}".format(raw_r)
            area = pi*(raw_r**2)
            shape_a_hist.append(r), shape_a_hist.append(area)

        elif shape == "square" or shape == "s":
            raw_side = input_checker("Side: ")
            side = "Side: {}".format(raw_side)
            area = raw_side**2
            shape_a_hist.append(side), shape_a_hist.append(area)

        elif shape in bh_list:
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            a_shape_lengths.append(base), a_shape_lengths.append(height)
            area = base * height
            shape_a_hist.append(a_shape_lengths), shape_a_hist.append(area)

        elif shape == "triangle" or shape == "t":
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            a_shape_lengths.append(base), a_shape_lengths.append(height)
            area = (base * height)/2
            shape_a_hist.append(a_shape_lengths), shape_a_hist.append(area)

        elif shape == "trapezium" or shape == "z":
            base = input_checker("Base: ")
            height = input_checker("Height: ")
            top_length = input_checker("Top length: ")
            a_shape_lengths.append(base), a_shape_lengths.append(height), a_shape_lengths.append(top_length)
            area = ((top_length + base) * height)/2
            shape_a_hist.append(a_shape_lengths), shape_a_hist.append(area)
        print("{}'s Area: {:.2f}{}\u00b2".format(shape, area, unit).capitalize())
        all_a_history.append(shape_a_hist)
        print("=================================================================================================")

        rerun = input_checker("Would you like to calculate the perimeter/area for another shape? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N!", num_ok=False)
        if rerun == "n":
            loop = False

# HISTORY
history_ask = input_checker("Would you like the history of your previously calculated perimeters/areas? (Y/N) ", checklist=["y", "yes", "n", "no"], error_msg="Please enter Y or N!", num_ok=False)
print("=================================================================================================")

if history_ask == "y" or history_ask == "yes":
    for item in all_p_history:
        print("{}".format(item[0]).upper())
        print("Perimeter: {:.2f}{}".format(item[3], item[1]))
        print("{}{}\n".format(item[2], item[1]))

    for item in all_a_history:
        print("{}".format(item[0]).upper())
        print("Area: {:.2f}{}\u00b2".format(item[3], item[1]))
        print("{}{}\n".format(item[2], item[1]))

print("Thank you for using the Perimeter/Area Calculator!")
