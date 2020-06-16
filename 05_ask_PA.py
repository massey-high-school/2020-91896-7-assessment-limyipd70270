def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
        else:
            return response


# ask user if they want to find the perimeter and/or the area

ask_pa = not_blank("Would you like to find the perimeter (P), area (A) or both (B)? ", "Please enter 'P', 'A', or 'B'", "no")
if ask_pa != use string converter
print (ask_pa)