import pytesseract
import pdf2image as p2i
import PyPDF2
import imageClipper as ic
import cv2



#-------------------Convertors----------------------

def WritePDFtoTXT_OCR(images, name, mode, clipper: bool, x_accuracy:int,y_accuracy:int):
    fullText = " "
    for i,image in enumerate(images):
        print(f"Page {i} is converting...")
        #lazimsiz boxlari silir
        if(clipper):
            image = ic.ClearBoxes(ic.ConverToMatlike(image), f"PNGs/test_png{startPage + i}.png", accuracity_x=x_accuracy,accuracity_y=y_accuracy)
            image = ic.ConverToImage(image)            
        
        text = pytesseract.image_to_string(image, lang="aze", config=mode)
        #text = TextClear(text)
        fullText += '\n' + text
        #f = open(f"{name}_page{i + startPage}.txt", "w", encoding="utf-8")
        #f.write(text)
        print(f"Page {i} converted")
    f = open(name, "w", encoding="utf-8")
    f.write(fullText)    
    return fullText
    
def WritePDFtoTXT_noOCR(pdf_path, output_txt):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Initialize an empty string to store the text
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Write the extracted text to a text file
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    print("PDF converted to text successfully!")
    return text

def WritePDFtoTXT(pdfPath:str,outputName:str,ocrmode:bool, dpi:int, startPage:int, endPage:int, mode:str , clipper: bool, x_accuracy = 50, y_accuracy = 50):
    if ocrmode:
        images = p2i.convert_from_path(pdfPath, dpi, first_page= startPage, last_page=endPage)
        return WritePDFtoTXT_OCR(images, outputName, mode, clipper, x_accuracy, y_accuracy)
    else:
        return WritePDFtoTXT_noOCR(pdfPath, outputName)
    
    
    
def SavePNGs(images,name):
    for i, image in enumerate(images):
        image.save(f"PNGs/{name}{i}.png", "PNG")
    print("Images converted to PNGs!")
    
        
def SavePNG(image, name):
    image.save(f"PNGs/{name}", "PNG")
    print("Image converted to PNG!")
    
#---------------------------------------------------------

# 200 normaldi mence, neqeder artsa o qedere yavas isleyir proqram
#OCR modlari: https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/
pdfPath = "PDFs/az_tarixi_6.pdf"
startPage = 10
endPage = 13

useOCR = True
deqiqlik = 400
imageClipper = False


#---------Main-----------------------------------

#print("Converting...")

#WritePDFtoTXT(pdfPath,"Tests/misalOCR.txt",useOCR,deqiqlik,startPage,endPage, mode="--psm 3",clipper = imageClipper)

# image = convert_from_path(pdfPath,deqiqlik,first_page=startPage,last_page=endPage)
# SavePNG(image[0], "az_tarixi_6.png")

#print(f"Bu qeder sehife var: {len(images)}")

#SavePNG(images[0], "az_tarixi_6")

    
#f = open(f"texts/az_tarixi_6_full.txt", "w", encoding="utf-8")
#f.write(fullText)



