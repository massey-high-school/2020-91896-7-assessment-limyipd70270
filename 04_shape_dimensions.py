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

# get all dimensions, will use the needed dimensions later to calculate the area and/or perimeter
all_lengths = ""
while all_lengths() != "xxx":
    #
    shapes_lengths = []
    print("Please enter each length for your shape (or radius if it's a circle) and enter 'xxx' once you have entered all of them")
    length = num_check("length: ")
""
circle = pi(r^2)
square = base * height
rectangle = base * height
triangle = (base * height)/2
trapezium = ((top length + base) * height)/2
parallelogram = base * height

pi= 3.14159265

circle = 2pir
square = get all input in square length and add items in there
rectangle =
triangle =
trapezium =
parallelogram =

    # list for each row of expenses
    single_expense = []
    expense = not_blank("Item Name: ", "You can't leave this blank, please enter the item name", "yes")

    # If user enters exit code, break out of loop
    if expense.lower() == "xxx":
        break

#How do I separate it for the fixed costs list since it doesn't need an amount for each???

    # Ask user how many of each item is needed
    expense_amount = num_check("How many do you need?", "Please enter a whole number more than zero", int)

     # Get the item costs
    single_cost = num_check("Item Cost: $", "Please enter a number more than zero", float)

    single_expense.append(expense)
    single_expense.append(single_cost)

    # adds each row of costs to cost list
    expense_list.append(single_expense)


for item in expense_list:
    print("{}: {}".format(item[0], item[1]))
