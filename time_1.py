import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
Hour = int(input("Enter the Hour: "))
print(Hour)
# Minute = time.strftime('%M')
# print(Minute)
# Second = time.strftime('%S')
# print(Second)
if (Hour>=0 and Hour<12):
    print("Good Morning!")
elif(Hour>=12 and Hour<16):
    print("Good Afternoon!")
elif(Hour>=16 and Hour<=19):
    print("Good Evening!")
elif(Hour>19 and Hour<=24):
    print("Good Night!")