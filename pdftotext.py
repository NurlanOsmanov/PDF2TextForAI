import PyPDF2 as p2

def PDFtoTXT(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        
        text = ''
        
        pdf_reader = p2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    print("PDF converted to text successfully")
    return text

def MakeOneSentecne(text):
    text = text.replace("\n", " ")
    text = text.strip()
    return text

#--------------------------------------------

fileName = "felsefe"

textData = PDFtoTXT(f"PDFs/{fileName}.pdf")

#butun metni bir cümle halına gətir
textData = MakeOneSentecne(textData)

with open(f"PDFToText/{fileName}.txt", 'w', encoding='utf-8') as txt_file:
        txt_file.write(textData)
