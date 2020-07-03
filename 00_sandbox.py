possible_items = ["apple", "orange", "banana"]

thing = input("Which one? ").lower()

if thing in possible_items:
    print("OK")

else:
    for item in possible_items:
        if thing == item[0]:
            print("OK", item)

