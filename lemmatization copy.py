import json as js
import dictionaryclass as dc
import unicodedata

def Remove_Suffix(word, suffix_enum, root_words):
    word = unicodedata.normalize("NFC", word)
    if word in root_words:
        return word
    
    for suffix in sorted(suffix_enum, key=lambda x: len(x.value), reverse=True):
        if word.endswith(suffix.value):
            possible_root = word[:-len(suffix.value)]

            if possible_root in root_words:
                return possible_root
            else: 
                return Remove_Suffix(possible_root, suffix_enum, root_words)
    return word

#------------------------------------------------------------------

fullData = []
roots = []
lemmas = []



with open("tokens_exp.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read())
    
with open("DATAS/roots.json", "r",encoding="utf8") as file:
    roots = js.loads(file.read())    
    
for i in range(len(fullData)):
        word = fullData[i]
        if len(fullData[i]) > 2:
            word = Remove_Suffix(fullData[i], dc.GrammaticalSuffix, roots)
        lemmas.append(word)
    
with open("lemmas.json", "w",encoding="utf8") as file:
    js.dump(lemmas, file, ensure_ascii=False)

    