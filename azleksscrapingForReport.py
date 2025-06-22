from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup  
import json
import time
import dictionaryclass


options = Options()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

endpage = 5
page = 1
url_template = "https://azleks.az/online-dictionary/?s=4&page={}"

all_data:list[dictionaryclass.dictionary] = []


while page <= endpage:
    try:
        url = url_template.format(page)
        driver.get(url)
        
        # Gözləmə məntiqi
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "item.rich"))
            )
        except:
            print(f"Səhifə {page} yüklənmədi")
            break
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all("div", class_="item rich")
        
        if not items:
            print(f"Səhifə {page}: Məlumat tapılmadı")
            break

        for item in items:
            
            dictionary_entry:dictionaryclass.dictionary = dictionaryclass.dictionary()
            
            h3 = item.find("h3", class_="bash-soz")
            # Sözün başlığı (h3 elementi)
            word = h3.get_text(strip=True).replace('"', '').split('[')[0].strip() if h3 else ""

            dictionary_entry.word = word
            
            # Nitq hissəsi (feil, isim, sifət...)
            part_of_speech = item.find("span", class_="nitq-hissesi").get_text(strip=True) if item.find("span", class_="nitq-hissesi") else ""
            dictionary_entry.type = part_of_speech

            # Etimologiya (varsa)
            etymology = item.find("span", class_="etimologiya").get_text(strip=True) if item.find("span", class_="etimologiya") else ""
            dictionary_entry.origin = etymology
            
            # İzah mətni (h3-dən sonra gələn bütün mətnlər)
            explanation = ""
            next_sibling = h3.find_next_sibling()
            while next_sibling and next_sibling.name != "h3":
                explanation += next_sibling.get_text(strip=True) + " "
                next_sibling = next_sibling.find_next_sibling()
                
            dictionary_entry.explanation = explanation
            # Məlumatları saxla
            all_data.append(dictionary_entry)

        print(f"Səhifə {page} tamamlandı | Tapılan sözlər: {len(items)}")
        page += 1
        time.sleep(1.5)  # Serveri aşırı yükləməmək üçün

    except Exception as e:
        print(f"Xəta: {str(e)}")
        time.sleep(5)
        
        
jsonText = json.dumps([entry.__dict__ for entry in all_data], ensure_ascii=False, indent=4)
# JSON formatında yadda saxla
with open("DATAS/azleks_data_test.json", "w", encoding="utf-8") as f:
    f.write(jsonText)

driver.quit()
print("-->Bütün sözlər uğurla yığıldı və fayla yazıldı.")
