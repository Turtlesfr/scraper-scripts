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
#driver = webdriver.Firefox()
driver = webdriver.PhantomJS(executable_path=r'C:\Users\Alexandre\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe')
driver.set_window_size(800, 550)
with open("c95-produits.txt") as in_file:
    for url in in_file:
        driver.get(url.strip())

        product_name = ""
        price_code = ""
        serie = ""
        size = ""
        uso = ""
        aspecto = ""
        acabado = ""
        material = ""
        color_type = ""
        antislip = ""
        repetitivo = ""
        absorption = ""
        destonificado = ""
        ice_resistant = ""
        images_url = []
        packing = ""
        pdf = ""

        product_name = driver.find_element_by_tag_name("h1").text
        #print(product_name.text)
        price_code = driver.find_element_by_xpath('.//*/h1/span[2]').text
        #print(price_code.text)
        serie = driver.find_element_by_xpath('.//*[@class="sub"][1]').text.replace("Taco, ","").replace("Base, Serie ","").replace("Base decorada, ","").replace("Serie ","").replace(",","")
        #print(serie)
        size = driver.find_element_by_xpath('.//*/h1/span[1]').text
        #print(size)

        p_list1 = driver.find_elements_by_xpath('.//*[@class="info"]/p')
        for idx, val in enumerate(p_list1) :
            if "Uso: " in val.text :
                uso = val.text.replace("Uso: ","").replace("\n","")
            if "Aspecto: " in val.text :
                aspecto = val.text.replace("Aspecto: ","").replace("\n","")
            if "Acabado: " in val.text :
                acabado = val.text.replace("Acabado: ","").replace("\n","")
            if "Tipo de cerámica: " in val.text :
                material = val.text.replace("Tipo de cerámica: ","").replace("\n","")
        p_list2 = driver.find_elements_by_xpath('.//*[@class="texto-caract"]/div/p')
        for idx, val in enumerate(p_list2) :
            if "Agrupación de color: " in val.text :
                color_type = val.text.replace("Agrupación de color: ","").replace("\n","")
            if "Deslizamiento: " in val.text :
                antislip = val.text.replace("Deslizamiento: ","").replace("\n","")
            if "Repetitivo: " in val.text :
                repetitivo = val.text.replace("Repetitivo: ","").replace("\n","")
            if "Absorción: " in val.text :
                absorption = val.text.replace("Absorción: ","").replace("\n","")
            if "Destonificado: " in val.text :
                destonificado = val.text.replace("Destonificado: ","").replace("\n","")
            if "Resistente a la helada: " in val.text :
                ice_resistant = val.text.replace("Resistente a la helada: ","").replace("\n","")
        photos = driver.find_elements_by_class_name("photosw")
        images_url = ""
        for photo in photos:
            photo_url = photo.get_attribute('href')
            image_name = photo_url.rsplit('/',1)[1]
            new_image_name = "carrelage-c-95-"+serie.replace(" ","-").replace("/","-")+"-"+product_name.replace(" ","-").replace(".","").replace(",","").replace(";","")+"-"+image_name
            new_image_name = new_image_name.replace(" ","-").replace(",","")
            full_image_filename = os.path.join('D:/PYTHON/c95', new_image_name)
            urllib.request.urlretrieve(photo_url, full_image_filename)
            images_url += "//"+new_image_name
        array_caract = driver.find_elements_by_xpath('.//*[@class="packing"]/table/tbody/tr[2]/td')
        for idx, val in enumerate(array_caract) :
            packing = packing+","+val.text.replace(",",".")
        packing = packing[1:]
        
        pdf = driver.find_element_by_xpath('.//*[@class="download-pdf"]/a').get_attribute('href')
        pdf_name = "carrelage-c-95-"+serie.replace(" ","-").replace("/","-")+"-"+product_name.replace(" ","-")+".pdf"
        pdf_name = pdf_name.replace(",","")
        full_pdf_filename = os.path.join('D:/PYTHON/c95', pdf_name)
        urllib.request.urlretrieve(pdf, full_pdf_filename)

        current_product_url = driver.current_url
        print(product_name+";"+price_code+";"+serie+";"+size+";"+uso+";"+aspecto+";"+acabado+";"+material+";"+color_type+";"+antislip+";"+repetitivo+";"+absorption+";"+destonificado+";"+ice_resistant+";"+images_url+";"+packing+";"+pdf_name+";"+current_product_url)
