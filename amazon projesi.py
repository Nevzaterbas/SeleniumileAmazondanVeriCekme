import time

from selenium import webdriver #selenium kütüphanesini yüklüyorsunuz
import time #time modüllünü çok uzun tutmanıza gerek. Görebilesiniz diye uzun tuttum.

ara=input("Aramak istediğiniz asin numarasını giriniz:")

browser=webdriver.Firefox(executable_path = "C:\\Users\\Nevzat\\Desktop\\geckodriver.exe") #ben firefox browserını kullandım

browser.get("https://www.amazon.com.au/")

time.sleep(3)

arama_cubuğu=browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
giris=browser.find_element_by_xpath("//*[@id='nav-search-submit-button']")

arama_cubuğu.send_keys(ara)

giris.click()

time.sleep(3)

eleman=browser.find_element_by_css_selector(".a-size-base-plus.a-color-base.a-text-normal")

eleman.click()
time.sleep(3)

elements=browser.find_elements_by_css_selector(".a-keyvalue.prodDetTable")
bsr=[]
for element in elements:
    bsr.append(element.text)

bsrCount=0

with open("info.txt","w",encoding="UTF-8") as file:
    for bsrs in bsr:
        file.write("\n"+"\n"+"\n")
        file.write(bsrs)







browser.close()


