import pdfReader as pr
import cv2
import imageClipper as ic
import numpy as np

#----------------TextManiplators----------------
#Setrleri birlesdirib
def TextFormat(text):
    temp_text = ''
    lines = text.split("\n")
    for i in range(0, len(lines) - 1):
        if len(lines[i]) == 0:
            temp_text += "\n"
            continue
        if lines[i][-1] == '-':
            lines[i] = lines[i][:-1]
        else:
            if(lines[i][-1] not in ['.','?','!']): 
                lines[i] += " "
        if (lines[i][0] in ['*','x']):
            # Kamalin kodu
            continue
        else:
            temp_text += lines[i]
        print(lines[i])
    print("-------------------------------------------------\n" + temp_text)
    return temp_text
    
def FindTopic(text):
    founded = False
    if(len(text) > 0 and text[0] >= '0' and text[0] <= '9'):
        temp_text = text.split(".")


        if (len(temp_text) != 2 or temp_text[0] is None or temp_text[1] is None): return False

        number = temp_text[0]
        topicName = temp_text[1]
        if(len(topicName) == 1): return False
        #eger noqteden evvel gelen reqemdise, ve ondan sonra gelenler boyukdurse
        if(number[-1] >= '0' and number[-1] <= '9'):
            for i,letter in enumerate(topicName):
                if((letter >= "A" and letter <= "Z") or (letter >= "0" and letter <= "9") or letter in ['Ö','Ə','Ü','İ',' ', '-','—', 'Ç','Ş']):
                    founded = True
                    continue
                else:
                    return False
        else: return False
    
        
    #if(founded): print("000000000000000000000000000000000000000")
    return founded

def IsValidSentence(line):
    if(line[-1] not in['.', '?', '!'] or line[-2] == ' '): return False
    if(not(line[0] >= "A" and line[0] <= "Z" or line[0] in ['Ö','Ə','Ü','İ',' ', '-','—', 'Ç','Ş']) and not(line[0] >= '0' and line[0] <='9')): False
    return True

def SplitToPoints(lines):
    resultSentences = []
    
    for line in lines:
        add = False
        sentences = line.split('.')
        if(len(sentences) <= 1): continue
        for i,_ in enumerate(sentences):
            if(len(sentences[i]) == 0): continue
            if(not (sentences[i][-1] > '0' and sentences[i][-1] <'9')):
                if not add:
                    resultSentences.append(sentences[i] + '.')
                else:
                    resultSentences[-1] += sentences[i]
            else:
                add = True
                resultSentences.append(sentences[i] + '.')

    #Do somethings
    
    return resultSentences
            
        
        

def ClearText(text):
    result = ''
    if(text is None): return "There is not text"
    abzas = text.split('\n')
    lines = SplitToPoints(abzas)
    
    for i in range(0, len(lines) - 1):
        if FindTopic(lines[i]): 
            result += "\n"
            result += lines[i] 
            result += "\n"
            continue
        if(IsValidSentence(lines[i])):
            if(lines[i][0] != ' '): lines[i] = " " + lines[i]
            result += lines[i]
        else: print("(" + lines[i][0] + "), (" + lines[i][-1] + ") ->>>>" + lines[i])
    
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

def PageToImages(images):
    result = []
    for i in images:
        image = images[0]
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


leftMargin = 0.125
topMargin = 0.1
rightMargin = 0.915
bottomMargin = 0.875
#-------------------------------

print("Converting...")

images = pr.PDFtoImage(pdfPath,dpi,startPage,endPage)

myImages = PageToImages(images)

print("Images converted to PNGs! Length of PDF: " + str(len(myImages)))

pr.WriteImagesToTXT_OCR(myImages, pdfname, "--psm 6 --oem 3", imageClipper, 50, 50, repate=False, treshHold=treshHold, doBinary=doBinary)

# image = ic.ConverToMatlike(image.resize((int(image.size[0] * 0.25), int(image.size[1] * 0.25))))
# cv2.imshow('image', image)
# cv2.moveWindow('image',0,0)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


