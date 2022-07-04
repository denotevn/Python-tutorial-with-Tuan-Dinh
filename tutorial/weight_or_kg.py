weight = input("Weight: ")

C = input("(L)bs or (K)g: ")

if C == 'K' or C == 'k':
    a = int(weight) * 2
    print(f"You are {a} pounds")
if C == 'L' or C == 'l':
    weight = int(weight) / 2
    print(f"You are {weight} kilogram")