# Countdown script for rocket launch

# Use a for loop with range to create the countdown
for i in range(10, -1, -1):
    print(i)

# After the loop completes, print "Liftoff!"
print("Liftoff!")

Explanation:

We use a for loop with the range() function to create the countdown.

The arguments in range(10, -1, -1) are explained as follows:

The first argument 10 is the start value.
The second argument -1 is the end value (not included). We use -1 because we want to include 0 in our countdown.
The third argument -1 is the step, indicating that we're counting down by 1 each time.
This range() will generate the sequence: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

In each iteration of the loop, we use print(i) to print the current number. Python's print() function by default adds a newline after each call, so each number will be printed on a new line.

After the loop ends, we use print("Liftoff!") to print the final message.


### something I did 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
for x in range(len(a) - 1, -1, -1):
    print(f"{x}")

print("Liftoff!")
