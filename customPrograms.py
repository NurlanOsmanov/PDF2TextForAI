import pdfReader as pr

#----------------TextManiplators----------------
#Setrleri birlesdirib
def TextClear(text):
    temp_text = ''
    lines = text.split("\n")
    for i in range(0, len(lines) - 1):
        if len(lines[i]) == 0:
            temp_text += "\n"
            continue
        if FindTopic(lines[i]): print("la\n\n")
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




#topiclere ayirma yerine yetirmek ucun:


#App isleyecek:

pdfPath = "PDFs/az_tarixi_6.pdf"
startPage = 15
endPage = 17

useOCR = True
deqiqlik = 400
#Islemir bu hele
imageClipper = True

print("Converting...")

text = pr.WritePDFtoTXT(pdfPath,"Tests/misalOCR.txt",useOCR,deqiqlik,startPage,endPage,clipper=imageClipper,mode= r'--psm 6', x_accuracy=100,y_accuracy=100)

text = TextClear(text)
print(text)
