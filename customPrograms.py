import pdfReader as pr

#----------------TextManiplators----------------
#Setrleri birlesdirib
def TextClear(text):
    temp_text = ''
    lines = text.split("\n")
    for i in range(0, len(lines) - 1):
        if len(lines[i]) == 0:
            #temp_text += "\n"
            continue
        if FindTopic(lines[i]): temp_text += "\n"
        
        if lines[i][-1] == '-':
            lines[i] = lines[i][:-1]
        else:
            lines[i] += " "
        if (lines[i][0] in ['*','x']):
            # Kamalin kodu
            continue
        else:
            temp_text += lines[i]
    print(temp_text)
    return temp_text
    
def FindTopic(text):
    founded = False
    if(len(text) > 0 and text[0] >= '0' and text[0] <= '9'):
        temp_text = text.split(".")
        number = temp_text[0]
        topicName = temp_text[1]
        if (len(topicName) == 0 or len(number) == 0): return False
        
        #eger noqteden evvel gelen reqemdise, ve ondan sonra gelenler boyukdurse
        if(number[-1] >= '0' and number[-1] <= '9'):
            for letter in topicName:
                if(letter >= "A" and letter <= "Z" or letter in ['Ö','Ə','Ü']):
                    founded = True
                    continue
                else:
                    return False
        else: return False
        
        #if(founded) print()
    return founded




#topiclere ayirma yerine yetirmek ucun:


#App isleyecek:

pdfPath = "PDFs/az_tarixi_6.pdf"
startPage = 10
endPage = 16

useOCR = True
deqiqlik = 400
#Islemir bu hele
imageClipper = True

print("Converting...")

text = pr.WritePDFtoTXT(pdfPath,"Tests/misalOCR.txt",useOCR,deqiqlik,startPage,endPage,clipper=imageClipper,mode= r'--psm 6', x_accuracy=100,y_accuracy=100)

text = TextClear(text)

f = open("Tests/misalResult.txt", "w", encoding="utf-8")
f.write(text)  
