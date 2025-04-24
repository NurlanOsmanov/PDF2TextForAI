import json as js
import dictionaryclass as dc




def Remove_Suffix(word, suffix_enum, root_words):
    for suffix in sorted(suffix_enum, key=lambda x: len(x.value), reverse=True):
        if word.endswith(suffix.value):
            possible_root = word[:-len(suffix.value)]
            if possible_root in root_words:
                return possible_root
    return word

#------------------------------------------------------------------

with open("DATAS/azleks_data.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))
    
#print(lemmas[256])

unique_dict = {}

for i in range(len(fullData)):
    if fullData[i].type == "feil" or fullData[i].type == "":
        if fullData[i].word.endswith("maq") or fullData[i].word.endswith("mək") and len(fullData[i].word) > 3:
            fullData[i].word = fullData[i].word[:-3]
    
    if fullData[i].word not in unique_dict:
        unique_dict[fullData[i].word] = fullData[i].word

del fullData[i].word

lemmas = list(unique_dict.values()) 
    
with open("DATAS/lemmas.json", "w",encoding="utf8") as file:
    js.dump(lemmas, file, ensure_ascii=False, indent=4)

    