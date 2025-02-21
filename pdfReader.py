import pytesseract
from pdf2image import convert_from_path

#Setrleri birlesdirib
def TextClear(text):
    temp_text = ''
    lines = text.split("\n")
    for i in range(0, len(lines) - 1):
        if len(lines[i]) == 0:
            temp_text += "\n"
            continue
        if FindTopic(lines[i]): print("<-----------\n\n")
        if lines[i][-1] == '-':
            lines[i] = lines[i][:-1]
        else:
            lines[i] += " "
        temp_text += lines[i]
    print(temp_text)
    return temp_text
    
def FindTopic(text):
    founded = False
    beginsWithNumner = False
    if(len(text) > 0 and text[0] >= '0' and text[0] <= '9'): 
        beginsWithNumner = True
    if(beginsWithNumner):
        temp_text = text.split(".")[0] 
        print(temp_text + " - " + temp_text[-1])
        #Burani deyismek lazim olacaq
        if(len(temp_text) > 0 and temp_text[-1] >= '0' and temp_text[-1] <= '9'):
            founded = True
            print("--> " + text)
    return founded



#---------------------------------------------------------

#C:\Users\nurla\OneDrive\Masaüstü\Python\PDF readers\PDFs\az_tarixi_6.pdf
# 200 normaldi mence, neqeder artsa o qedere yavas isleyir proqram
startPage = 9
endPage = 12
deqiqlik = 400
images = convert_from_path("PDFs/az_tarixi_6.pdf", deqiqlik, first_page= startPage, last_page=endPage)
print(len(images))

fullText = ' '

for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang="aze")
    f = open(f"texts/_az_tarixi_6_original_page{i + startPage}.txt", "w", encoding="utf-8")
    f.write(text)
    text = TextClear(text)
    fullText += '\n' + text
    a = open(f"texts/_az_tarixi_6_page{i + startPage}.txt", "w", encoding="utf-8")
    a.write(text)
    
f = open(f"texts/az_tarixi_6_full.txt", "w", encoding="utf-8")
f.write(fullText)

print("OCR tamamlandı! Mətn çıxarıldı.")





