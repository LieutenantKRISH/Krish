"""(Q1) Write a program which will find all such numbers which are divisible by 7 but
are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a
single line.
(ANS) """
l = []
for i in range(2000,3201):
    if(i%7 == 0)and (i%5 != 0):
        l.append(str(i))
print (','.join(l))

"""(Q2) Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.

(ANS) """
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input("Enter the Number for factorial:-"))
print (fact(x))

""" (Q2)
"""
# Initialize an empty list
my_list = []

# Read the number of commands
n = int(input())

# Process each command
for _ in range(n):
    command = input().split()
    
    # Perform the specified operation
    if command[0] == "insert":
        position = int(command[1])
        value = int(command[2])
        my_list.insert(position, value)
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "remove":
        value = int(command[1])
        my_list.remove(value)
    elif command[0] == "append":
        value = int(command[1])
        my_list.append(value)
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()

