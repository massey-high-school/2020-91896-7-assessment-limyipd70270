# Number checking function (number must be a float that is more than 0)
def num_check(question):
    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

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

# Initialise lists
# all_lengths includes every shapes' dimensions
all_lengths = []
# shapes_lengths is the list for the individual shape's lengths added
shapes_lengths = []

# !!!!!!!!!! what if they have a square which have the same measurements on all sides, would they put the 4 lengths repeated or just once?
# dimensions to calculate the perimeter
print("Please enter the measurements (don't include units) for your shape , pressing 'enter' after each one. Print 'xxx' once you have entered all of them")

length = ""
while length != "xxx":
    # length is for each side of the shape
    # !!!!!!! allows numbers that are negative!!!!!!!
    length = not_blank("Length: ", "Please enter a number that is more than zero", "yes")

    # If user enters exit code, break out of loop
    if length == "xxx":
        break

    shapes_lengths.append(length)
    # !!!!!!! all_lengths is for the history list, do i need to add different variable for when i add the lengths of area dimensions??????????
    # bc all_lengths would have ALL the lengths which some are repeated
    all_lengths.append(shapes_lengths)

# radius used for both area/perimeter
r = num_check("Radius: ")
# dimensions to calculate the area
base = num_check("Base: ")
height = num_check("Height: ")
top_length = num_check("Top length: ")

# put in the lists for printing for history
shapes_lengths.append(r)
shapes_lengths.append(base)
shapes_lengths.append(height)
shapes_lengths.append(top_length)
all_lengths.append(shapes_lengths)

# print differently, not blank as int and num check as float, make all answers nicely as one of these types
print(shapes_lengths)

# swap ask_PA and shape dimensions, and renumber to add the 3 as a component


