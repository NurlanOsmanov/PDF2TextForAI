import pdfReader as pr

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
    
#topiclere ayirma yerine yetirmek ucun:


#App isleyecek:

pdfPath = "PDFs/az_tarixi_6.pdf"
startPage = 31
endPage = 33

useOCR = True
deqiqlik = 500
#Islemir bu hele
imageClipper = True

print("Converting...")

text = pr.WritePDFtoTXT(pdfPath,"Tests/misalOCR.txt",useOCR,deqiqlik,startPage,endPage,clipper=imageClipper,mode= r'--psm 6', x_accuracy=75,y_accuracy=75,repate=False)

text = TextFormat(text)

f = open("Tests/misalLast.txt", "w", encoding="utf-8")
f.write(text)  

text = text[2:]

#print(text)
text = ClearText(text)

f = open("Tests/misalResult.txt", "w", encoding="utf-8")
f.write(text)  


