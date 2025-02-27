import PIL.Image
import cv2
import pytesseract
import numpy as np
from datetime import datetime

'''
# Görüntüyü yükle
image = cv2.imread("PNGs/az_tarixi_6.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Kenarları belirlemek için Canny Edge Detection kullan
edges = cv2.Canny(gray, 50, 150)
cv2.imwrite("PNGs/az_tarixi_6_edge.png", edges)

# Konturları bul
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for contour in contours:
    # Konturları dikdörtgenlere çevir
    x, y, w, h = cv2.boundingRect(contour)

    # Boyut filtresi: Küçük veya çok büyük kutuları hariç tut
    if w > 50 and h > 50:
        roi = gray[y:y+h, x:x+w]  # Kutunun içindeki alan

        # OCR ile metin olup olmadığını kontrol et
        text = pytesseract.image_to_string(roi, config="--psm 6")

        if text.strip():  # İçinde yazı varsa
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), -1)  # Beyazla doldur
'''

# Sonucu kaydet veya göster

def ConverToMatlike(image: PIL.Image): 
    opencv_image = np.array(image)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)
    return opencv_image

def ConverToImage(opencv_image: cv2.typing.MatLike): 
    rgb_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    pil_image = PIL.Image.fromarray(rgb_image)
    return pil_image

def MakeBinary(image: cv2.typing.MatLike, threshold: int=250):

    # Şəkildəki ağ rəngli pikselləri tap
    white_mask = cv2.inRange(image, np.array([threshold, threshold, threshold]), np.array([255, 255, 255]))

    # Ağ olmayan pikselləri qara et
    result = np.zeros_like(image)  # Bütün pikselləri qara et
    result[white_mask == 255] = [255, 255, 255]  # Ağ pikselləri saxla


    # cv2.imshow('Result', result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return result


def ClearBoxes(image: cv2.typing.MatLike, name: str, accuracity_x: int = 50,  accuracity_y: int= 50, repate: bool=False):
    try:
        opencv_image = MakeBinary(image, 220)
        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        opencv_image = gray 
    except:
        opencv_image = image
        gray = opencv_image


    # Kenarları belirlemek için Canny Edge Detection kullan
    edges = cv2.Canny(gray, 150, 200)
    # i=datetime.now().microsecond
    # print(i)
    # cv2.imwrite(f"PNGs/az_tarixi_6_edge{i}.png", edges)
    # Konturları bul
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Konturları dikdörtgenlere çevir
        x, y, w, h = cv2.boundingRect(contour)

        # Boyut filtresi: Küçük veya çok büyük kutuları hariç tut
        if w > accuracity_x and h > accuracity_y:
            roi = gray[y:y+h, x:x+w]  # Kutunun içindeki alan

            # OCR ile metin olup olmadığını kontrol et
            text = pytesseract.image_to_string(roi, config="--psm 6")

            if text.strip():  # İçinde yazı varsa
                cv2.rectangle(opencv_image, (x, y), (x+w, y+h), (255, 255, 255), -1)
                # print(text)
                
    if(repate):
        opencv_image = ClearBoxes(opencv_image,name,accuracity_x * 0.9,accuracity_y*0.9,False)
    else:
        cv2.imwrite(filename=name,img =opencv_image)
        
    return opencv_image

#sehifedeki hundurlukleri olcur.
def GetTextSizes_Gray(image: cv2.typing.MatLike):
    # Gri tonlama
    gray = image

    # Threshold (binarizasiya)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Konturları tap
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Bounding box-ları çıxart
    bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]

    # Hündürlükləri topla
    heights = [h for _, _, _, h in bounding_boxes]

    return heights

def filter_text_by_size_range(image, size_min, size_max):
    """
    Şəkildə yalnız müəyyən edilmiş ölçü aralığında olan mətnləri saxlayır.

    Parametrlər:
        image: Giriş şəkli (grayscale olmalıdır).
        size_min: Ən kiçik qəbul edilən mətn hündürlüyü.
        size_max: Ən böyük qəbul edilən mətn hündürlüyü.
    
    Qaytarır:
        filtered_image: Yalnız seçilmiş hündürlük aralığında olan mətnlərin olduğu şəkil.
    """

    # Şəkli ikili (binary) hala gətir
    _, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Konturları tap
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Yeni boş şəkil (yalnız seçilmiş ölçüdə mətnlər üçün)
    filtered_image = np.zeros_like(image)

    # Konturları yoxla
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Hündürlük müəyyən olunmuş aralıqdadırsa, onu saxla
        if size_min <= h <= size_max:
            cv2.drawContours(filtered_image, [cnt], -1, (255, 255, 255), thickness=cv2.FILLED)

    return filtered_image

#--------------main-----------------

# image = ClearBoxes(image=cv2.imread("PNGs/az_tarixi_6.png"),name="Tests/testpng.png",accuracity_x=75,accuracity_y=75, repate=True)
# cv2.imshow('Result',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#print(GetTextSizes_Gray(image=image))
# image = cv2.imread("PNGs/az_tarixi_6.png")
# MakeBinary(image=image)

#cv2.imwrite( "Tests/testclearedpng.png",filter_text_by_size_range(image, 1,50))