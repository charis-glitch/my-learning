emoji = {
    ":)": "😊",
    ":(": "😢",
}
type = input("> ")
type = type.split(" ")
output = ""
for word in type:
    #if word in emoji:
    #    word = emoji[word]
    #output += word + " "
    output += emoji.get(word, word) + " "
print(output)

