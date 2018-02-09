from selenium import webdriver
import urllib.request 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions    import StaleElementReferenceException
from selenium.common.exceptions    import WebDriverException
from selenium.common.exceptions    import TimeoutException as SeleniumTimeoutException
from selenium.webdriver.support.ui import WebDriverWait

pages = ["http://www.fl.com/71302_es/ATLAS/","http://www.fl.com/71332_es/CEYLAN/","http://www.fl.com/71295_es/CORFU/","http://www.fl.com/71333_es/LEVANTE/","http://www.fl.com/71296_es/LORD/","http://www.fl.com/71294_es/VELVET/","http://www.fl.com/71299_es/ATLAS/","http://www.fl.com/71298_es/CORFU/","http://www.fl.com/71204_es/habitat/","http://www.fl.com/71334_es/LEVANTE/","http://www.fl.com/71203_es/lord/","http://www.fl.com/71337_es/SABANA/","http://www.fl.com/71247_es/velvet/","http://www.fl.com/71201_es/zement/","http://www.fl.com/71300_es/ATLAS/","http://www.fl.com/71051_es/compact/","http://www.fl.com/71052_es/daino-real/","http://www.fl.com/71053_es/habitat/","http://www.fl.com/71054_es/iridium/","http://www.fl.com/71205_es/lord/","http://www.fl.com/71056_es/millenium/","http://www.fl.com/71057_es/museum/","http://www.fl.com/71059_es/royale/","http://www.fl.com/71336_es/SABANA/","http://www.fl.com/71060_es/saturnia/","http://www.fl.com/71061_es/studio/","http://www.fl.com/71062_es/syncro/","http://www.fl.com/71249_es/velvet/","http://www.fl.com/71028_es/avenue/","http://www.fl.com/71029_es/compact/","http://www.fl.com/71215_es/forest/","http://www.fl.com/71031_es/habitat/","http://www.fl.com/71394_es/levante/","http://www.fl.com/71335_es/PEDRA/","http://www.fl.com/71032_es/syncro/","http://www.fl.com/71033_es/trek/","http://www.fl.com/71246_es/velvet/","http://www.fl.com/71202_es/zement/","http://www.fl.com/71301_es/ATLAS/","http://www.fl.com/71066_es/compact/","http://www.fl.com/71297_es/CORFU/","http://www.fl.com/71181_es/daino-real/","http://www.fl.com/71067_es/habitat/","http://www.fl.com/71207_es/house/","http://www.fl.com/71182_es/iridium/","http://www.fl.com/71208_es/lord/","http://www.fl.com/71183_es/millenium/","http://www.fl.com/71040_es/museum/","http://www.fl.com/71042_es/royale/","http://www.fl.com/71043_es/saturnia/","http://www.fl.com/71045_es/studio/","http://www.fl.com/71046_es/syncro/"]

browser = webdriver.Chrome("C:/chromedriver.exe")  # Optional argument, if not specified will search path.

#browser.maximize_window()
with open("fl-url.txt") as in_file:
    for url in in_file:
        # get website
        browser.get(url.strip())
        # get current url
        #print (browser.current_url)
        # get name & get phone number
        serieCenter = browser.find_element_by_xpath(".//*[@id='serieCenter']")
        #print(serieCenter)
        images = serieCenter.find_elements_by_xpath(".//*/div/a/img[@src]")
        #print(images)
        for image in images:
            image_raw_url = image.get_attribute('src')
            image_url = image_raw_url.replace(".preview","")
            image_url = image_url.replace(".preview(1)","")
            image_name_array = image_url.split("/")
           # print(image_url)
            try :
                urllib.request.urlretrieve(image_url, image_name_array[-1])
            except Exception:
                print("foirage")
                print(image_url)
                continue
            #print("ok")
            
