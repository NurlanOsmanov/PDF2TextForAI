import dictionaryclass as dc
import json as js


fullData:list[dc.dictionary] = []

with open("DATAS/azleks_data.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))
    
    
bosCount = 0
for i in fullData:
    if len(i.word) == 0:
        bosCount += 1
        
        
print("Data yuklendi " + str(len(fullData)) + " eded soz var, " + str(bosCount) + " eded bos soz var")