from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup  
from bs4.element import NavigableString
import json
import time
import dictionaryclass as dc

#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrome-temp"
#google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-temp"



# Chrome profili və ayarları
options = Options()
# options.add_argument("--no-first-run")
# options.add_argument("--user-data-dir=/home/nurlan/.config/google-chrome")  # Chrome profilin
# options.add_argument("--profile-directory=Default")  # Müvafiq profil adı
# options.add_argument("--remote-debugging-port=9222") 
options.debugger_address = "127.0.0.1:9222"



# Chromedriver başlat
driver = webdriver.Chrome(options=options)

print(driver.title)
# golopeh977@ptiong.com "42£ko+EoA>5

# Məlumatların çəkilməsi
endpage = 2463
page = 2420
url_template = "https://azleks.az/online-dictionary/?s=4&page={}"
all_data:list[dc.dictionary] = []


allowed_classes = ['vurgu']


while page < endpage:
    try:
        url = url_template.format(page)
        driver.get(url)

        try:
            # Elementlərin yüklənməsini gözlə
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "item.rich"))
            )
        except Exception as e:
            print(f"Səhifə {page} yüklenmedi")
            break

        # Sayfanın mənbə kodunu BeautifulSoup ilə oxu
        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all("div", class_="item rich")

        if not items:
            print(f"Səhifə {page}: heç bir 'item rich' elementi tapılmadı.")
            break

        for item in items:
            word_data = {}
            h3all = item.find_all("h3", class_="bash-soz")

            first_h3 = False
            for h3 in h3all:
                if h3:
                    newEntry:dc.dictionary = dc.dictionary()
                    word_parts = ""
                    
                    if isinstance(h3, str):
                        if h3.strip():
                            word_parts += h3.strip()
                    
                    for child in h3.contents:
                        if isinstance(child, NavigableString):  # Əgər sadə mətn parçasıdırsa
                            word_parts += child.strip() + " "
                            
                            
                    for strong in h3.find_all('strong'):
                        # Orijinalı dəyişmədən nüsxə çıxar
                        strong_copy_html = str(strong)
                        strong_copy_soup = BeautifulSoup(strong_copy_html, 'html.parser')
                        strong_copy = strong_copy_soup.find('strong')

                        # Bu hissədə artıq sadəcə copy üzərində işləyirik
                        tags_to_remove = []
                        for tag in strong_copy.find_all():
                            tag_classes = tag.get('class', [])

                            if not any(cls in allowed_classes for cls in tag_classes):
                                tags_to_remove.append(tag)  # saxla, amma sonra sil

                        # İndi tagləri sil (təhlükəsiz – iterable pozulmur)
                        for tag in tags_to_remove:
                            tag.decompose()

                        clean_text = strong_copy.get_text(strip=True)
                        if clean_text.endswith("\n"):
                            clean_text = clean_text[:-1]
                        while clean_text.endswith(" "):
                            clean_text = clean_text[:-1]
                        word_parts += clean_text 
                        
                    word = word_parts 
                    newEntry.word = word
                    
                    
                    nitq_hissesi = h3.find("span", "nitq-hissesi")
                    orgin = h3.find("span","etimologiya")
                    if(orgin):
                        newEntry.origin=orgin.text
                        #print(orgin.text)
                    else:
                        newEntry.origin = dc.WordOrgin.azərbaycanca.name
                    if(nitq_hissesi):
                        newEntry.type = nitq_hissesi.text

                    # h3-dən sonra gələn elementləri topla
                    explanation_parts = []
                    for sibling in h3.find_next_siblings():
                        if sibling.name == "h3":
                            break
                        _inText = sibling.get_text(strip=True)

                        explanation_parts.append(_inText)
                    
                    newEntry.explanation = " ".join(explanation_parts)
                    all_data.append(newEntry)
            
        print(f"Səhifə {page} bitdi, {len(items)} söz tapıldı.")
        page += 1
        time.sleep(1)  # Serverə yük olmaması üçün yüngül gecikmə
        if(page % 20 == 0):
            jsonText = json.dumps([entry.__dict__ for entry in all_data], ensure_ascii=False, indent=4)
            with open("backup_data.json", "a", encoding="utf-8") as f:
                f.write(jsonText)
    except Exception as e:
        print(repr(e))
        time.sleep(5)  # Serverə yük olmaması üçün yüngül gecikmə


jsonText = json.dumps([entry.__dict__ for entry in all_data], ensure_ascii=False, indent=4)
# JSON formatında yadda saxla
with open("DATAS/azleks_data.json", "w", encoding="utf-8") as f:
    f.write(jsonText)

driver.quit()
print("-->Bütün sözlər uğurla yığıldı və fayla yazıldı.")
