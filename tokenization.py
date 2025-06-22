import nltk.tokenize
import json as js

data = ""
with open("az_tarixi_6.txt", "r",encoding="utf8") as file:
    data = file.read()

data = data.lower()

tokens =  nltk.tokenize.word_tokenize(data)

tokensJson = js.dumps(tokens, ensure_ascii=False, indent=4)

with open("tokens_exp.json", "w",encoding="utf8") as file:
    file.write(tokensJson)
