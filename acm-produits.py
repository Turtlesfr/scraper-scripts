from selenium import webdriver
import urllib.request
import os
from time import sleep 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions    import StaleElementReferenceException
from selenium.common.exceptions    import WebDriverException
from selenium.common.exceptions    import TimeoutException as SeleniumTimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
#driver = webdriver.PhantomJS(executable_path=r'C:\Users\Alexandre\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe')
driver.set_window_size(800, 550)
with open("acm-produits.txt") as in_file:
    for url in in_file:
        driver.get(url.strip())
        main_window = driver.current_window_handle
        _serie = ""
        _modele = ""
        _fichetechnique = ""
        _image = ""

        couleurs_list = []
        
        options = driver.find_elements_by_xpath('.//*[@class="options"]')
        couleurs = options[0].find_elements_by_tag_name("a")
        for item in couleurs:
            couleurs_list.append(item.get_attribute("href"))
        for couleur in couleurs_list:
            driver.get(couleur)
            options2 = driver.find_elements_by_xpath('.//*[@class="options"]')
            formats = options2[1].find_elements_by_tag_name("a")
            format_list = []
            for item_f in formats:
                format_list.append(item_f.get_attribute("href"))
            for taille in format_list:
                driver.get(taille)
                _serie = driver.find_elements_by_tag_name('h1')[6].text
                _modele = driver.find_elements_by_tag_name('h2')[0].text
                _fichetechnique = driver.find_elements_by_class_name("right")[0].text
                _fichetechnique = "<br />".join(_fichetechnique.split("\n"))
                img_prod_box = driver.find_elements_by_class_name("swipebox")[0].get_attribute("href")
                #print(img_prod_box)
                image_name = img_prod_box.rsplit('/',1)[1]
                new_image_name = _serie.replace("/","#").replace("É","E").replace(" ","-").replace("Ê","E").replace("Ú","U")+"_"+_modele.replace("/","#").replace(".","_").replace(" ","").replace("~","-")+"_"+image_name
                full_img_filename = os.path.join('D:/PYTHON/acl', new_image_name)
                #print(new_image_name)
                _image = new_image_name
                _current_product_url = driver.current_url
                print(_serie+";"+_modele+";"+_fichetechnique+";"+_image+";"+_current_product_url)
                urllib.request.urlretrieve(img_prod_box, full_img_filename)
