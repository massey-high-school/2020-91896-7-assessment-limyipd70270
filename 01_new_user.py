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

yn_list = ["yes", "y", "no", "n"]

# ask user if they want to find the perimeter and/or the area
ask_newuser = string_checker("Have you used this perimeter/area tool before? ", "Please enter 'yes' (Y) or 'no' (N)", yn_list)
print (ask_newuser)
