import time
#store starting time
begin = time.time()
a = int(input())
if (a%2==0):
    print("Even")
else:
    print("Odd")
end = time.time()
print(f"The time consume by the programme is",{end - begin})