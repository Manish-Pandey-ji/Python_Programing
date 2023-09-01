# I'm wirteing Pseudo Code for the given problem
# Take the number N as input from the user
n = int(input())
# Create a variable to store the sum
sum = 0
# i  for using the whilw loop
i = 1
# while i is less than and equal to n:
while i <= n:
    # Find Even number for calculate sum
    if n % 2 == 0:
        # Store sum on the variable
        sum += n
    # For stop the whilw loop
    n -= 1
# Print the result
print(sum)

'''Alternate Program

n = int(input())
sum = 0
i = 2
while i <=n:
    sum += i
    i += 2
print(sum)

'''