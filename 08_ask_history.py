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

history_ask = not_blank("Would you like a history of your previously calculated areas/perimeters? ", "Please enter 'yes' or 'no'", "no")
history_ask = ""

if history_ask == "yes":
    print(all_lengths)

# If user enters no, break out of loop
if history_ask != "yes":
    break
