# I'm writing Psedo Code for this problem side by side
# Step-> Input = number
num = int(input())
# Step-> Even sum = 0
evenSum = 0
# step-> Odd sum = 0
oddSum = 0
# step-> While number is greatr than 0
while num > 0 :
    # Step-> Last_digit = number module 10
    last = num % 10
    # Step-> If Last_digit Even
    if last % 2 == 0:
        # Step-> Even sum = Even sum + Last_digit
        evenSum += last
    #Else
    else:
        # Step-> Odd sum =  Odd sum + Last_digit
        oddSum += last
    # step-> number divided by 10
    num = num // 10
# Step-> Print Even sum and Odd sum
print(evenSum, " ", oddSum)