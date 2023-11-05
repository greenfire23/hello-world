lname = "becker" # assigns a default value to lname variable
fname = "ethan" # assigns a default value to fname variable
GPA = 0 # assigns default value to GPA variable
while True:
    lname = input("Enter students last name:") # Asks for students last name
    if lname == "ZZZ": # Breaks loop if "ZZZ" is entered
        break
    fname = input("Enter students first name: ") # Asks for students first name
    GPA = float(input("Enter students GPA as a decimal: ")) # Asks for GPA assigns the value as a float to GPA variable
    # If statements to evaluate the entered GPA to determine if studnent made Honor Roll or Dean's List
    if GPA >= 3.5:
        print(fname, lname, " has made the Dean's List")
    elif GPA >= 3.25:
        print(fname, lname, "has made the Honor Roll")
