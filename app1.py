import json

data=json.load(open("076 data.json"))

type(data)

ip=input("enter the word")

print(meaning(ip))

def meaning(word):
    this.word=data[word]

    return(this.word)
