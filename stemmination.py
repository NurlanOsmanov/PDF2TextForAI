import json as js
import dictionaryclass as dc




def Remove_Suffix_From_RootWord(word, suffix_enum, root_words):
    for suffix in sorted(suffix_enum, key=lambda x: len(x.value), reverse=True):
        if word.endswith(suffix.value):
            possible_root = word[:-len(suffix.value)]
            if possible_root in root_words:
                return possible_root
    return word

def Remove_Suffix(word, suffix_enum):
    done = True
    _word = word
    while done and len(_word) > 2:
        
        for suffix in sorted(suffix_enum, key=lambda x: len(x.value), reverse=True):
            
            if _word.endswith(suffix.value):
                possible_root = _word[:-len(suffix.value)]
                _word = possible_root
                done = True
                break
            else: 
                done = False

    return _word

#------------------------------------------------------------------

with open("DATAS/lemmas.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))
    


unique_dict = {}

for i in fullData:
    word = Remove_Suffix(i, dc.LexicalSuffix)
    if word not in unique_dict:
        unique_dict[word] = word

lemmas = list(unique_dict.values()) 

with open("DATAS/roots.json", "w",encoding="utf8") as file:
    js.dump(lemmas, file, ensure_ascii=False, indent=4)

    