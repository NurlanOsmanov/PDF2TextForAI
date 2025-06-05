import azenlp as nlp
import json as js
import dictionaryclass as dc

def generate_ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

with open("DATAS/azleks_data.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))

fullText = ""

i = 0
for des in fullData:
    if des.explanation:
        fullText += " " + des.explanation
        i+=1
    if i == 20: break

#print(fullText)

tokens = []
tokens = nlp.Tokenization(fullText)

print(generate_ngrams(tokens, 2))