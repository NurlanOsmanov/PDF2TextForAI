import dictionaryclass as dc
import json as js


fullData = []

with open("tokens_exp.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read())
    
    
bosCount = 0
for i in fullData:
    i = i.lower()
        
with open("tokens_exp_low.txt", "w",encoding="utf8") as file:
    js.dump(fullData, file, ensure_ascii=False)