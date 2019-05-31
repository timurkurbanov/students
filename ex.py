listing = [
    [None, "Pumpkin", None, None],
    ["Socks", None, "Mimi", None],
    ["Gismo", "Shadow", None, None],
    ["Smokey","Toast","Pacha","Mau"]
]
#(1)
print("Row 1 seat 1 is free. Row 1 seat 3 is free. Row 1 seat 4 is free. Row 2 seat 2 is free. Row 3 seat 3 is free. Row 3 seat 4 is free.")


#(2)
print("Row 1 seat 1 is free. Do you want to sit there? (y/n)")
user= input()
if user == "y":
    print("What is your name?")
    name = input()
    listing[0][0] = name
    print(listing)

print("Row 1 seat 3 is free. Do you want to sit there? (y/n)")
user= input()
if user == "y":
    print("What is your name?")
    name = input()
    listing[0][2] = name
    print(listing)

print("Row 1 seat 4 is free. Do you want to sit there? (y/n)")
user= input()
if user == "y":
    print("What is your name?")
    name = input()
    listing[0][3] = name
    print(listing)

print("Row 2 seat 2 is free. Do you want to sit there? (y/n)")
user= input()
if user == "y":
    print("What is your name?")
    name = input()
    listing[1][1] = name
    print(listing)

print("Row 3 seat 3 is free. Do you want to sit there? (y/n)")
user= input()
if user == "y":
    print("What is your name?")
    name = input()
    listing[2][2] = name
    print(listing)

print("Row 3 seat 4 is free. Do you want to sit there? (y/n)")
user= input()
if user == "y":
    print("What is your name?")
    name = input()
    listing[2][3] = name
    print(listing)