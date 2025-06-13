import nltk as nlp
import json as js
import dictionaryclass as dc


def skip_grams(tokens, window_size=2):
    pairs = []
    for i, target in enumerate(tokens):
        for j in range(max(0, i - window_size), min(len(tokens), i + window_size + 1)):
            if i != j:
                pairs.append((target, tokens[j]))
    return pairs

with open("DATAS/azleks_data.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))

fullText = ""

i = 0
for des in fullData:
    if des.explanation:
        fullText += " " + des.explanation
        i+=1

#print(fullText)

tokens = nlp.tokenize.word_tokenize(fullText)
pairs = skip_grams(tokens, window_size=2)

print("Skip-gram bitti, " + str(len(pairs)) + " cüt tapıldı")

text = ""

for item in pairs:
    exp = "[" + item[0] + " , " + item[1] + "]\n"
    text += exp
    # print(exp)


with open("DATAS/skip_gram_data.txt", "w",encoding="utf8") as file:
    file.write(text)
