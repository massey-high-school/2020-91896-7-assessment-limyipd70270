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

pab_list = ["p", "perimeter", "a", "area", "b", "both"]

# ask user if they want to find the perimeter and/or the area
ask_pa = string_checker("Would you like to find the perimeter (P), area (A) or both (B)? ", "Please enter 'P', 'A', or 'B'", "no", pab_list)
print (ask_pa)