import json as js
import dictionaryclass as dc


with open("DATAS/azleks_data.json", "r", encoding="utf-8") as file:
    fullData = js.loads(file.read(), object_hook=lambda d: dc.dictionary(**d))


target_types = {"nida", "bağlayıcı", "edat"}

filtered_words = [
    entry.word for entry in fullData
    if (entry.type or "").strip().lower() in target_types
]


with open("DATAS/azerbaijani_stopwords.json", "w", encoding="utf-8") as outfile:
    js.dump(filtered_words, outfile, ensure_ascii=False)