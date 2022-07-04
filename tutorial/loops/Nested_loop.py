from unicodedata import numeric


for x in range(4):
    for y in range(3):
        print(f"(x,y) = {x,y}")


# challenge
numbers =[5,2,3,3,4]
for x in numbers:
    print("x" * x)

# 
print("Solution 2")
for x in numbers:
    output = ""
    for i in range(x):
        output += "x"
    print(output)