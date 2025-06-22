import json as js
import dictionaryclass as dc

#------------------------------------------------------------------

with open("DATAS/azleks_data.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))
    


unique_dict = {}

for i,_ in enumerate(fullData):
    word = fullData[i].word
    if fullData[i].type == "feil" or fullData[i].type == "":
        if word.endswith("maq") or word.endswith("mək") and len(word) > 3:
            word = word[:-3]
    if word not in unique_dict:
        unique_dict[word] = word

roots = list(unique_dict.values()) 

with open("DATAS/roots0.json", "w",encoding="utf8") as file:
    js.dump(roots, file, ensure_ascii=False, indent=4)

 