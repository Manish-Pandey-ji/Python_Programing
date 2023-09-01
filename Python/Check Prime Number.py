n = int(input())
prime = False
i = 1
while i <= n:
    if (n % 2 == 0):
        prime = True
    i += 1
if prime :
    print("Not Prime")
    if n == 2:
        print(" Sorry , 2 is prime")
else:
    print("Prime")
    if n == 1:
        print(" sorry , 1 is not prime")