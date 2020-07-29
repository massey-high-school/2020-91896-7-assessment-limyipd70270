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

def check_unit(): # can use variables from the main bc main is global, main routine can't use variables defined in the function bc the functions is local
    mm = ["mm", "millimeters", "millimetres", "millimeter", "millimetre"]
    cm = ["cm", "centimeters", "centimetres", "centimeter", "centimetre"]
    m = ["m", "meters", "metres", "meter", "metre"]
    km = ["km", "kilometers", "kilometres", "kilometer", "kilometre"]
    units_list = mm + cm + m + km # https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/

    unit = input_checker("Unit: ", checklist=units_list, error_msg="Please enter a valid unit!", num_ok=False) # this defines it
    if unit in mm: # these make sure the abbreviations are printed no matter what the input is
        unit = "mm"
    elif unit in cm:
        unit = "cm"
    elif unit in m:
        unit = "m"
    elif unit in km:
        unit = "km"
    return unit # keep bc you call it later when unit= check_unit(), the others i didn't assign

def calculate_perimeter():
    dimension_list = [] # since it was in the main before, it kept adding both area and perimeter dimensions to it since both functions used the same variable name,
    # and it was globally defined in main, where it was not reset between uses
    r_p_list = ["rectangle", "r", "parallelogram", "p"]
    if shape == "circle" or shape == "c":
        r = input_checker("Radius: ")
        dimension_list.append("Radius: {}{}".format(r, unit))
        perimeter = 2*pi*r

    elif shape == "square" or shape == "s":
        side = input_checker("Side: ")
        dimension_list.append("Side: {}{}".format(side, unit))
        perimeter = side*4

    elif shape in r_p_list: # rectangle, parallelogram
        length_1 = input_checker("Length 1: ")
        length_2= input_checker("Length 2: ")
        dimension_list.append("Length 1: {}{}".format(length_1, unit))
        dimension_list.append("Length 2: {}{}".format(length_2, unit))
        perimeter = 2*length_1 + 2*length_2

    elif shape != "circle" or shape != "c": # trapezium/triangle
        #https://www.w3schools.com/python/ref_func_range.asp got sister to help/explain
        num_lengths = shapes_list[shape] # the no. next to the shapes in shapes_list, https://www.iteanz.com/tutorials/python/accessing-values-in-dictionary/
        perimeter = 0 # need perimeter=0 bc adding onto previous numbers, outside 'for' loop bc if it was in, each time it asks for the length, perimeter would go back to zero and won't add
        for i in range(num_lengths): # gets number associated with the shape chosen
            length = input_checker("Length {}: ".format(i+1)) # increases each time it asks for length
            dimension_list.append("Length {}: {}{}".format(i+1, length, unit))
            perimeter += length # the no. next to the shapes is the nth number in the i array/range since i starts from zero,
            # e.g. triangle:3, i=2 bc 2 is 3rd number in i range/array, for {} in Length: to be printed, it must be i+1, but technically
            # '3' is the amount of times to ask for the length
    perimeter_str = ("{}'s perimeter: {:.2f}{}".format(shape, perimeter, unit).capitalize())
    print(perimeter_str)
    shape_info.append(perimeter_str)
    shape_info.append(dimension_list)
    print("=================================================================================================")

def calculate_area():
    dimension_list = []
    bh_list = ["rectangle", "r", "parallelogram", "p"]
    if shape == "circle" or shape == "c":
        r = input_checker("Radius: ")
        dimension_list.append("Radius: {}{}".format(r, unit))
        area = pi*(r**2)

    elif shape == "square" or shape == "s":
        side = input_checker("Side: ")
        dimension_list.append("Side: {}{}".format(side, unit))
        area = side**2

    elif shape in bh_list:
        base = input_checker("Base: ")
        height = input_checker("Height: ")
        dimension_list.append("Base: {}{}".format(base, unit))
        dimension_list.append("Height: {}{}".format(height, unit))
        area = base * height

    elif shape == "triangle" or shape == "t":
        base = input_checker("Base: ")
        height = input_checker("Height: ")
        dimension_list.append("Base: {}{}".format(base, unit))
        dimension_list.append("Height: {}{}".format(height, unit))
        area = (base * height)/2

    elif shape == "trapezium" or shape == "z":
        base = input_checker("Base: ")
        height = input_checker("Height: ")
        top_length = input_checker("Top length: ")
        dimension_list.append("Base: {}{}".format(base, unit))
        dimension_list.append("Height: {}{}".format(height, unit))
        dimension_list.append("Top Length: {}{}".format(top_length, unit))
        area = ((top_length + base) * height)/2
    area_str = ("{}'s area: {:.2f}{}\u00b2".format(shape, area, unit).capitalize())
    print(area_str)
    shape_info.append(area_str)
    shape_info.append(dimension_list)
    print("=================================================================================================")

# *** Main Routine starts here ***
# Initialise lists
history = [] # sister helped with explaining what was global and local, rearranged the placing of the lists to fix the problem with printing history, less variables now

# https://www.w3schools.com/python/python_dictionaries.asp, num_lengths is no. next to each shape (amount of times to ask for length)
shapes_list = {"circle": 1, "c": 1, "square": 1, "s": 1, "rectangle": 0, "r": 0, "triangle": 3, "t": 3, "trapezium": 4, "z": 4, "parallelogram": 0, "p": 0}
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
    shape_info = [] # at the end of loop, appends to history and then refreshes the shape info, for every loop it's one shape,
    # only thing that links the main routine to the functions, if put in area and perimeter function, not in while loop, then
    # if they entered 'both', it would calculate perimeter then when calculating area, it'd reset the list bc they're both
    # added to shape_info list and in the history it would only print the shape_info for area
    pab_ask = input_checker("Would you like to find the perimeter (P), area (A) or both (B)? ", checklist=["p", "perimeter", "a", "area", "b", "both"], error_msg="Please enter P, A or B!", num_ok=False)
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

    unit = check_unit()

    if pab_ask == "p" or pab_ask == "perimeter":
        calculate_perimeter()
    elif pab_ask == "a" or pab_ask == "area":
        calculate_area()
    elif pab_ask == "b" or pab_ask == "both":
        print("PERIMETER")
        calculate_perimeter()
        print("AREA")
        calculate_area()
    history.append(shape_info)

    rerun = input_checker("Would you like to calculate the perimeter/area for another shape? (Y/N) ", checklist=["y", "yes", "n", "no"], error_msg="Please enter Y or N!", num_ok=False)
    if rerun == "n":
        loop = False

# HISTORY
history_ask = input_checker("Would you like the history of your previously calculated perimeters/areas? (Y/N) ", checklist=["y", "yes", "n", "no"], error_msg="Please enter Y or N!", num_ok=False)
print("=================================================================================================")

print("HISTORY")
if history_ask == "y" or history_ask == "yes":
    for shape_data in history:
        for element in shape_data:
            if type(element) is list: # if an element (the section) is a list (e.g. dimensions) then print the dimensions inside
                for dimensions in element:
                    print(dimensions)
            else: # if the element is not a list then just print it how it is
              print(element)
        print("")

# sister helped explain and show a way to print the history so that item() isn't used, more specific
# history = [shape_data, shape_data]
           # shape_data = [element, [dim, dim]]
                                  # (element)
# history = [[element, [dim, dim]], [Triangle's perimeter: 3m, [Length 1: 1m, Length 2: 1m, Length 3: 1m]]]

print("Thank you for using the Perimeter/Area Calculator!")
