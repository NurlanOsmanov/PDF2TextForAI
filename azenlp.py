import dictionaryclass as dc
import json as js


fullData:list[dc.dictionary] = []

with open("DATAS/azleks_data.json", "r",encoding="utf8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))
    
for i in fullData:
    while True:
        #print(i.word + "|")
        if i.word.endswith(" "):
            i.word = i.word[:-1]
            print("" + i.word + "|")
        else:
            break
        
print("Data yükləndi " + str(len(fullData)) + " ədəd söz var")

    
with open("DATAS/azleks_data.json", "w",encoding="utf8") as file:
    file.write(js.dumps([entry.__dict__ for entry in fullData], ensure_ascii=False, indent=4))





