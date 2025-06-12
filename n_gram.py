import azenlp as nlp
import json as js
import dictionaryclass as dc

def generate_ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

with open("DATAS/azleks_data.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))

fullText = ""
print("Program basladi")
i = 0
for des in fullData:
    if des.explanation:
        fullText += " " + des.explanation
        # print(des.explanation)


#print(fullText)
print("Tokenlesmeye kecilir")

tokens = []
tokens = nlp.Tokenization(fullText)

print("Tokenlesme bitti, ngrama kecilir")
text = ""
elements = generate_ngrams(tokens, 2)
for item in elements:
    exp = "[" + item[0] + " , " + item[1] + "]\n"
    text += exp
    # print(exp)


with open("DATAS/n_gram_data.json", "w",encoding="utf8") as file:
    file.write(text)