import pytesseract
import pdf2image
import cv2
import PIL.Image
import numpy

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

            continue
        else:
            temp_text += lines[i]
    return temp_text

def WriteImagesToTXT_OCR(images):
    fullText = " "
    for image in images:
        text = pytesseract.image_to_string(image, lang="aze")
        fullText += '\n' + text  
    return fullText


def MakeBinary(image: cv2.typing.MatLike, threshold: int=250):
    white_mask = cv2.inRange(image, numpy.array([threshold, threshold, threshold]), numpy.array([255, 255, 255]))
    result = numpy.zeros_like(image) 
    result[white_mask == 255] = [255, 255, 255] 

    return result


def ClearBoxes(image: cv2.typing.MatLike, accuracity_x: int = 50,  accuracity_y: int= 50):
    opencv_image = numpy.array(image)
    opencv_image = MakeBinary(opencv_image, threshold=250)  # Convert to binary if needed
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 175, 200)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > accuracity_x and h > accuracity_y:
            roi = gray[y:y+h, x:x+w]

            # Icinde yazi olub olmadigini yoxlayir
            text = pytesseract.image_to_string(roi, config="--psm 6")

            if text.strip():  # Içınde yazı varsa
                cv2.rectangle(opencv_image, (x, y), (x+w, y+h), (255, 255, 255), -1)
                
    cv2.imwrite(f"PNGs/az_tarixi_6_clean{0}.png",img = opencv_image)
    
    return opencv_image


#-------------------Main----------------------


pdfPath = "PDFs/az_tarixi_6.pdf"
pdfname = "az_tarixi_6"

startPage = 10
endPage = 12
dpi = 600

images = pdf2image.convert_from_path(pdfPath, dpi, first_page= startPage, last_page=endPage)

for i, image in enumerate(images):
    
    image = ClearBoxes(image, accuracity_x = 100, accuracity_y=100)
    cv2.imwrite(f"PNGs/az_tarixi_6_clean{i}.png",img = image)
    
    image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)  # Convert PIL image to OpenCV format
    images[i] = image 


fullText = WriteImagesToTXT_OCR(images)

fullText = TextFormat(fullText)

f = open(f"{pdfname}.txt", "w", encoding="utf-8")
f.write(fullText)    