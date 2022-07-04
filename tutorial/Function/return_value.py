import math
def square(r):
    return math.pi*r*r
r = 2
print(f"Square of Circle: {square(r)}")

def emojis_convetered(message):
    # Em nha que
    words = message.split(' ') # Em nha que

    emojis = {
        ":)":"💁",
        ":(":"😍"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    print(output)

message = input(">>")
emojis_convetered(message)