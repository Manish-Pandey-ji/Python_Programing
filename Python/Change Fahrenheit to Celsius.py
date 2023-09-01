# Pseudo Code for the problem
# start , end, step = input
# Current Value = Start
start = int(input())
# Last Value = end
end = int(input())
# Step the fahenhiet jump
step = int(input())
# Current Value = Start
CurrentFahenhietvalue = start
#While Current Value is less than equal to end:
while CurrentFahenhietvalue <= end:
    # Fahrenheit = (5.0 / 9) * (Current Value -32)
    celsiusValue = (5 / 9) * (CurrentFahenhietvalue - 32) 
    # print (Fahrenheit Current Value)
    print("Current Fahenhiet value: " + str(CurrentFahenhietvalue) + "\t" + "Celsius Value: "  + str(float(celsiusValue)))
    # Current Value = Current Value + Step to jump.
    CurrentFahenhietvalue += step