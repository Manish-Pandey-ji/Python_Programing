# I'm writing Pseudo Code for this problem side by side

# Step-> Input = N
n = int(input())
# Step-> temp=N, rev_num = 0
temp = n
revNum = 0
# Step-> While temp is greater than 0:
while temp > 0:
    # Step-> Last_digit = temp modulo 10
    lastDigit = temp % 10
    # Step-> temp/10
    temp = temp // 10
    # Step-> rev_num*10+last_digit 
    revNum = revNum * 10 + lastDigit
# Step-> print(rev_num)
print(revNum)