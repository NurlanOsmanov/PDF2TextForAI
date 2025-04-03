import re
import pdfReader as pr
import cv2
import imageClipper as ic
import numpy as np
import dictionaryclass as dc
import json

#----------------TextManiplators----------------
#Setrleri birlesdirib
def TextFormat(text):
    temp_text = ''
    lines = text.split("\n")
    
    connectSentece = False
    for i in range(0, len(lines) - 1):
        if len(lines[i]) == 0:
            if (not connectSentece):
                temp_text += "\n"
            continue
        if lines[i][-1] == '-':
            lines[i] = lines[i][:-1]
            connectSentece = True
        else:
            temp_text += " "
            connectSentece = False
                
        temp_text += lines[i]
        print(lines[i])
    print("-------------------------------------------------\n" + temp_text)
    return temp_text
    
    
def FindWord():
    found = True
    
    
    
    
    return found
    
    
def TextData():
    result = ''
    
    
    return result
    


def GetListOfDictionary(text):
    dictionary:list[dc.dictionary] = []

    text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)
    
    # Abzaslara ayır
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    print("\n--------------------------------------------------------\n")
    lastWord = dc.dictionary()
    
    for para in paragraphs:
        para = para.replace("\n", " ")
        
        thisWord = dc.dictionary()
        
        first_word = re.split(r'\s+', para, maxsplit=1)[0]   
        
        if is_main_word(first_word):
            main_word = clean_main_word(first_word)
            
            thisWord.word = main_word
            thisWord.explanation,thisWord.type,thisWord.origin = process_explanation(para[len(first_word):])
            
            lastWord = thisWord
        else:
            if lastWord == None:
                continue
            else:
                thisWord.word = lastWord.word
                thisWord.explanation,thisWord.type,thisWord.origin = process_explanation(para, lastWord.type, lastWord.origin)
                if thisWord.type == "":
                    thisWord.type = lastWord.type
                if thisWord.origin != lastWord.origin:
                    thisWord.origin = lastWord.origin
                
        dictionary.append(thisWord)
        #entry = dc.dictionary()

    return dictionary



    
def process_dictionary_text(text):
    # Sətir sonundakı "-" işarələrini birləşdir
    text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)
    
    # Abzaslara ayır
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    entries = []
    current_entry = None
    
    for para in paragraphs:
        # İlk sətri götür
        first_line = para.split('\n')[0] if '\n' in para else para
        first_word = re.split(r'\s+', first_line, maxsplit=1)[0]
        
        # Əsas sözü yoxla
        if is_main_word(first_word):
            # Yeni giriş yarat
            if current_entry:
                entries.append(current_entry)
            
            main_word = clean_main_word(first_word)
            explanation,_ = process_explanation(para[len(first_word):])
            current_entry = {'word': main_word, 'explanation': explanation}
        else:
            # Əvvəlki girişə əlavə et
            if current_entry:
                additional_explanation = process_explanation(para)
                if additional_explanation:
                    if current_entry['explanation']:
                        current_entry['explanation'] += ' ' + additional_explanation
                    else:
                        current_entry['explanation'] = additional_explanation
    
    # Son girişi əlavə et
    if current_entry:
        entries.append(current_entry)
    
    # Nəticəni formatla
    result = []
    for entry in entries:
        if entry['explanation']:
            result.append(f"{entry['word']}\n{entry['explanation']}")
    
    return '\n\n'.join(result) if result else ""

def is_main_word(word):
    # Əsas söz olub-olmadığını yoxla (böyük hərflə başlayır və ya tam böyükdür)
    return (word[0].isupper() if word else False) or word.isupper()

def clean_main_word(word):
    # Əsas sözü təmizlə
    return re.sub(r'[^A-ZƏÜÖĞŞÇİ]', '', word.upper())

def process_explanation(text, wordtype = "", wordorgin = dc.WordOrgin.azərbaycanca.name):
    # Bütün sətirləri birləşdir
    lines = [line.strip() for line in text.split('\n')]
    full_text = ' '.join(lines)
    
    # İlk böyük hərfli sözə və ya rəqəmə qədər kəsilir
    match = re.search(r'([A-ZƏÜÖĞŞÇİ][a-zəüöğşçi]+|\d+\.)', full_text) 
    if match:
    #Sozun tipini burdan hell ediirk
        wordtypeandorgin = full_text[:match.start()]
        wordtype,wordorgin = Search_WordTypeAndOrgin(wordtypeandorgin)
    
    
    if match:
        full_text = full_text[match.start():]
    
    # Lazımsız hissələri təmizlə
    full_text = re.sub(r'\[.*?\]', '', full_text)  # Kvadrat mötərizələr
    full_text = re.sub(r'\{.*?\}', '', full_text)  # Fiğurlu mötərizələr
    #full_text = re.sub(r'\(.*?\)', '', full_text)  # Dairəvi mötərizələr
    full_text = re.sub(r'\|.*?\]', '', full_text)  # Kvadrat mötərizələr
    full_text = re.sub(r'\[.*?\|', '', full_text)  # Kvadrat mötərizələr
    full_text = re.sub(r'[|:]', '', full_text)     # | və : işarələri
    full_text = re.sub(r'\s+', ' ', full_text).strip()
    
    return full_text, wordtype, wordorgin


def Search_WordTypeAndOrgin(text):   
    _type = ""
    _origin = dc.WordOrgin.azərbaycanca.name
    
    for member in dc.WordType:
        if member.value in text:
            _type = member.name
            break
        
    for member in dc.WordOrgin:
        if member.value in text:
            _origin = member.name
            break
        
    return _type, _origin

def ClearText(text):
    result = ""
    
    result = TextFormat(text)
    
    return result
#----------------------Image Manuplator-----------------------------------------------

def CutImageToHalf(image):
    images = []
    width, height = image.size
    left = 0
    top = 0
    right = width // 2
    bottom = height 
    
    images.append(image.crop((left, top, right, bottom)))
    images.append(image.crop((right, top, width, bottom)))
    
    return images

def CutImage2Piece(raitox, image):
    images = []
    width, height = image.size
    
    images.append(image.crop((0, 0, width * raitox, height)))
    images.append(image.crop((width*(raitox), 0, width, height)))
    
    return images

def CropImage(image, left, top, right, bottom):
    return image.crop((left, top, right, bottom))

def PageToImages(images, formation:bool = False, StartPageFormayion: bool = False):
    result = []
    _formation = StartPageFormayion

        
    for i in images:
        image = i
        
        leftMargin = 0
        topMargin = 0
        rightMargin = 1
        bottomMargin = 1
        
        if(formation):
            if(not _formation):
                leftMargin = leftMargin0
                topMargin = topMargin0
                rightMargin = rightMargin0
                bottomMargin = bottomMargin0
            else:
                leftMargin = leftMargin1
                topMargin = topMargin1
                rightMargin = rightMargin1
                bottomMargin = bottomMargin1
                
            _formation = not _formation
                
        image = CropImage(image, leftMargin * image.size[0], topMargin * image.size[1], rightMargin * image.size[0], bottomMargin * image.size[1])
        corpedImages = CutImage2Piece(0.51,image)
        result.append(corpedImages[0])
        result.append(corpedImages[1])
    return result


#----------------------App isleyecek:----------------------------------------------------------

pdfPath = "PDFs/azərbaycan_dilinin_izahli_lügeti0.pdf"
pdfname = "azərbaycan_dilinin_izahli_lügeti0"
startPage = 26
endPage = 27

useOCR = True
dpi = 600
imageClipper = False
doBinary = False
treshHold = 250

"""
    pdfPath - oxunacaq pdfin path'i
    pdfname - fennin adi (testler ucun)
    startPage - hardan baslamali oldugu sehife
    endPage - harda bitmeli oldugu sehife
    useOCR - OCR isledir
    dpi - DPI deyisdirir
    imageClipper - sekildeki artiq formalari yox edir
    doBinary - yalnzi ag qara edir sekili
    treshHold - ne qeder aga yaxin olanlari ag, digerlerini ise full qara edecek

"""

#1-ci formation margins
leftMargin0 = 0.125
topMargin0 = 0.1
rightMargin0 = 0.915
bottomMargin0 = 0.875

#2-ci formation margins
leftMargin1 = 0.085
topMargin1 = 0.1
rightMargin1 = 0.875
bottomMargin1 = 0.875

#-------------------------------

print("Converting...")

images = pr.PDFtoImage(pdfPath,dpi,startPage,endPage)

myImages = PageToImages(images, True, False)

print("Images converted to PNGs! Length of PDF: " + str(len(myImages)))

ocrResult = pr.WriteImagesToTXT_OCR(myImages, pdfname, "--psm 6 --oem 3", imageClipper, 50, 50, repate=False, treshHold=treshHold, doBinary=doBinary)


dic = GetListOfDictionary(text=ocrResult)
for i in dic:
    print("word: " + i.word + "\ntype: " + i.type + "\norgin: "+i.origin + "\nexplanation: " +  i.explanation + "\n\n")
    
jsonText = json.dumps([entry.__dict__ for entry in dic], ensure_ascii=False, indent=4)

with open(pdfname + ".json", "w", encoding="utf-8") as f:
    f.write(jsonText)

# result = process_dictionary_text(ocrResult)

# f = open(pdfname+"result", "w", encoding="utf-8")
# f.write(result)   



# myImage = myImages[3]
# image = ic.ConverToMatlike(myImage.resize((int(myImage.size[0] * 0.25), int(myImage.size[1] * 0.25))))
# cv2.imshow('image', image)
# cv2.moveWindow('image',0,0)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


