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

with open("DATAS/fullData.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))
    

lemmas = [fullData.word for fullData in fullData]
#print(lemmas[256])

unique_dict = {}

for i in range(len(lemmas)):
    lemmas[i] = lemmas[i].lower()
    if lemmas[i].endswith("maq") or lemmas[i].endswith("mək") and len(lemmas[i]) > 3:
        lemmas[i] = lemmas[i][:-3]
    
    if lemmas[i] not in unique_dict:
        unique_dict[lemmas[i]] = lemmas[i]

del lemmas
lemmas = list(unique_dict.values()) 
    
with open("DATAS/lemmas.json", "w",encoding="utf8") as file:
    js.dump(lemmas, file, ensure_ascii=False, indent=4)

    