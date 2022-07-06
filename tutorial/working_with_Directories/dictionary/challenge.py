phone_numbers = {
    "1":"one",
    "2":"true",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nice"
}

num_phone = input("Phone: ")

output = ""
for c in num_phone:
    output += phone_numbers.get(c,"") + " "

print(output)

