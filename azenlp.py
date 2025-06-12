import dictionaryclass as dc
import json as js

def Tokenization(text:str):
    all_text = text.split(" ")
    return all_text

fullData:list[dc.dictionary] = []

# with open("DATAS/azleks_data _backup_0506 copy.json", "r",encoding="utf8") as file:
#     fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))

# for item in fullData:
#     while(True):
#         if(item.word.endswith(" ")):
#             item.word = item.word[:-1]
#         else: break

# for item in fullData:
#     while(True):
#         if(item.word.startswith(" ")):
#             item.word = item.word[1:]
#         else: break

# with open("DATAS/azleks_data.json", "w",encoding="utf8") as file:
#     #js.dump(myJsonFile, file, ensure_ascii=False, indent=4)
#     file.write(js.dumps([entry.__dict__ for entry in fullData], ensure_ascii=False, indent=4))

# myFile:dict = {}
# for i in fullData:
#     myFile[i.word] = i

# myJsonFile = []
# for i in myFile.values():
#     myJsonFile.append(i)
        
# #print(myJsonFile)
# print("Data yükləndi " + str(len(myJsonFile)) + " ədəd söz var")
    
# with open("DATAS/azleks_data.json", "w",encoding="utf8") as file:
#     #js.dump(myJsonFile, file, ensure_ascii=False, indent=4)
#     file.write(js.dumps([entry.__dict__ for entry in myJsonFile], ensure_ascii=False, indent=4))





