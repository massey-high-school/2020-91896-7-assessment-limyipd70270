[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2844975&assignment_repo_type=AssignmentRepo)
"Perimeter: {:.2f}".format(perimeter)
"Area: {:.2f}".format(area)

def p_history():
    for item in all_history:
        print("{}{}".format(item[3], item[1]))
        for item in p_shape_lengths:
            print("{}{}\n".format(item[2], item[1])) # dimensions

def a_history():
    for item in all_history:
        print("{}{}\u00b2".format(item[3], item[1]))
        for item in a_shape_lengths:
            print("{}{}\n".format(item[2], item[1])) # dimensions

# *** Main Routine starts here ***
# Initialise lists
all_history = []
