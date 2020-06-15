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


# Initialise lists
# all_lengths includes every shapes' dimensions
all_lengths = []

# get all dimensions, will use the needed dimensions later to calculate the perimeter
print("Please enter the lengths for your shape (or radius if it's a circle), pressing 'enter' after each one. Print the number '000' once you have entered all of them")

length = ""
while length != "000":
    # shapes_lengths is the list for the individual shape's lengths added
    shapes_lengths = []

    # length is for each side of the shape
    length = num_check("Length: ")

    # If user enters exit code, break out of loop
    if length == "000":
        break

    shapes_lengths.append(length)
    all_lengths.append(shapes_lengths)

print(shapes_lengths)
print(all_lengths)

