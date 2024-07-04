name = "Adithya"
name = name.lower()
for char in name:
    print(char)
    if(char=='a' or char=='i'):
        print(char," is a vowel")

Colors = ["Red","Green","Pink"]
for color in Colors:
    print(color)
    for i in color:
        print(i)

for j in range(10):
    print(j+1,end=" ")
print("\n")
for j in range(1, 101):
    if j%2==0:
        print(j,end=",")

print("\n")

for i in range(0,101,5):
    print(i,end=" ")