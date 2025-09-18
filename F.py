numbers = [5, 2, 5, 2, 2]

for number in [5, 2, 5, 2, 2]:
    print("x" * number)

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
#range(n) means a sequence of numbers from 0 up to n-1. It repeats the loop body n times.
#Example: If x_count = 5: 1st loop → "x"; 2nd loop → "xx"; 3rd loop → "xxx"; 4th loop → "xxxx"; 5th loop → "xxxxx"
#Final result = "xxxxx" → printed.


