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

# get all dimensions, will use the needed dimensions later to calculate the perimeter
print("Please enter the lengths (don't need to include the unit of measurement) for your shape (or radius if it's a circle), pressing 'enter' after each one. Print the number 'xxx' once you have entered all of them")

length = ""
while length != "xxx":
    # shapes_lengths is the list for the individual shape's lengths added
    shapes_lengths = []

    # length is for each side of the shape
    length = not_blank("Length: ", "Please enter a number that is more than zero", "yes")

    # If user enters exit code, break out of loop
    if length == "xxx":
        break

    shapes_lengths.append(length)
    all_lengths.append(shapes_lengths)

# should work if shapes_lengths???
print(all_lengths)





