# num_lengths is number next to these shapes, amount of times to ask for length
shapes_list = {"circle": 1,
               "square": 4,
               "rectangle": 4,
               "triangle": 3,
               "trapezium": 4,
               "parallelogram": 4}

pi= 3.14159265

# PERIMETER
shape_perimeter = {
  "circle" : circle,
  "rectangle" : rectangle,
  "square" : square
  "parallelogram" : parallelogram,
  "triangle" : triangle,
  "trapezium" : trapezium
}
circle = {
  "r" : "input_checker("Radius: ")",
  "perimeter" : "2*pi*r"
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

# AREA

shape_area = {
  "circle" : circle,
  "rectangle" : rectangle,
  "square" : square
  "parallelogram" : parallelogram,
  "triangle" : triangle,
  "trapezium" : trapezium
}

circle = {
  "r" : "input_checker("Radius: ")",
  "area" : "pi*(r**2)"
}

rectangle, square, parallelogram = {
  "base" : "input_checker("Base: ")",
  "height" : "input_checker("Height: ")"
  "area" : "base * height"
}

triangle = {
  "base" : "input_checker("Base: ")",
  "height" : "input_checker("Height: ")"
  "area" : "(base * height)/2"
}

trapezium = {
  "base" : "input_checker("Base: ")",
  "height" : "input_checker("Height: ")",
  "top_length" : "input_checker("Top length: ")"
  "area" : "((top_length + base) * height)/2"
}
