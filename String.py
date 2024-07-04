name = "AIML"
print("Hi "+name)

sentence = '''Hello everyone,
'Good Morning'
Good Afternoon
"Good Night"'''
print(sentence)

print(name[0])
print(name[3])
#print(name[4]) # This will throw an index error

print("Lets use for loop\n")
for char in name:
    print(char)

print("Lets use for loop for sentence\n")
for char in sentence:
    print(char)