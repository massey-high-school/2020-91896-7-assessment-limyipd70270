# num_lengths is number next to these shapes, amount of times to ask for length
shapes_list = {"circle": 1,
               "square": 4,
               "rectangle": 4,
               "triangle": 3,
               "trapezium": 4,
               "parallelogram": 4}

pi= 3.14159265

shape_perimeters = {
  "circle" : 2*pi*r,
  "rectangle" : perimeter += length
  "square" : perimeter += length
  "parallelogram" : perimeter += length
  "triangle" : perimeter += length
  "trapezium" : perimeter += length
}

!= "circle":
    num_lengths = shapes_list[ask_shape_p]
    # e.g. for i in [0,1,2,3] ..... range is a function that gives an array of numbers starting from 0

    # initialise counter outside the for loop
    perimeter = 0
    for i in range(num_lengths):
        # length is for each side of the shape
        length = input_checker("Length {}: ".format(i+1))
        perimeter += length

shape_areas = {
    "circle": pi*(r**2),
    "rectangle": base * height,
    "square": base * height,
    "parallelogram": base * height,
    "triangle": (base * height)/2,
    "trapezium": ((top_length + base) * height)/2
}

shape_history.append(area)