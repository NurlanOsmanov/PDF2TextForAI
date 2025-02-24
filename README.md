# PDF2TextForAI

OCR əsaslı python kodudur. Bunun üçün edilməlidir: pip install pdf2image pip install pytesseract

Windows: Tessarct Windows: 
https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe
Installiyasiya zamanı "Azərbaycan" dil packageni yükləməyi unutmayın. Əgər bunu unutsanız, sonradan aze_lan_package yükləyib Tesseract/tessdata ya əlavə edin.

Poppler for Windows:
https://github.com/oschwartz10612/poppler-windows/releases/
Download and extract. Then copy /bin path and add to PATH as system variable. More information: https://pdf2image.readthedocs.io/en/latest/installation.html

pip install pdf2image
pip install pytesseract
pip install opencv-python
pip install numpy
pip install PyPDF2

FOR Linux (Ubuntu):

sudo apt install tesseract-ocr tesseract-ocr-aze



For MAC:

brew install poppler

pip3 install pdf2image

pip3 install pytesseract


Çevriləcək pdf faylını PDFs qovluğuna at, proqramıda (customProgram.py) dəyişkənləri qeyd et və run et.
