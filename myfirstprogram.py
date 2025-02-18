# ask input name
# wrap the name in variable and make it uppercase
# and for loop for first program and make it into straight line for your second program
# if a has capital then return success if not the correct it

x = input("what is your name?")
upper= x.capitalize()
for a in upper:
    print(a)
if upper > a:
  print("b is greater than a")

#if a
#print 
#else
#print("please put one capital letter in it")

#hypothesis: 
#the reason we create the function is so that we can use it in the variable

def check_capitalization(x):
    upper = x.capitalize()
    for a in upper:
        print(a)
    return upper == x  # Returns True if x is already capitalized, else False

x = input("What is your name? ")
result = check_capitalization(x)

if result:
    print("It is true (input is already capitalized).")
else:
    print("Running the program again...")
    # You can add logic here to rerun the program if needed



---------------------------------
#this is seperate program to show, you can do the same thing as above in simpler way. 
def check_capitalization(x):
    return x == x.capitalize()  # Check if input is already capitalized

while True:  # Keep running until the input is capitalized
    x = input("What is your name? ")
    if check_capitalization(x):
        print("It is true (input is already capitalized).")
        break  # Exit the loop if input is capitalized
    else:
        print("Input is not capitalized. Running the program again...")
