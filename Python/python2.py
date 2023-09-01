q = int(input())
while q != 6:
    if q <= 5 and q >= 1:
        a = int(input())
        b = int(input())
    if q == 1:
        print(a + b)
    if q == 2:
        print(a - b)
    if q == 3:
        print(a * b)
    if q == 4:
        print(a//b)
    if q == 5:
        print(a%b)
    elif q > 6:
        print("Invalid Operation")
    q = int(input())