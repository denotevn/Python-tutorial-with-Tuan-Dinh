message = input(">>")
# Em nha que
words = message.split(' ') # Em nha que

emojis = {
    ":)":"💁",
    ":(":"😍"
}
print(emojis)

output = ""
for word in words:
    output += emojis.get(word,word) + " "
print(output)
