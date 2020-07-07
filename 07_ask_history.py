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
# Initialise lists
# all_lengths includes every shapes' dimensions
all_history = []

history_ask = input_checker("Would you like a history of your previously calculated areas/perimeters? (Y/N) ",
                            checklist=["y", "n"], error_msg="Please enter Y or N", num_ok=False)

history_ask = ""
if history_ask != "n":
    print("Areas:")
    print("Perimeters:")
    for item in all_history:
        print("{}: {:.2f}".format(item[0], item[1]))

history_ask = input_checker("Would you like a history of your previously calculated areas/perimeters? (Y/N) ", checklist=["y", "n"], error_msg="Please enter Y or N", num_ok=False)
if history_ask != "n":
    for item in all_history:
        print("{}: {:.2f}{}".format(item[0], item[2], item[1]))
