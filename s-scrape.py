from selenium import webdriver
import urllib.request
from time import sleep 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions    import StaleElementReferenceException
from selenium.common.exceptions    import WebDriverException
from selenium.common.exceptions    import TimeoutException as SeleniumTimeoutException
from selenium.webdriver.support.ui import WebDriverWait
print("product_name;product_ref;price_code;serie;size;material;relieve;quality;exterior;rectified;sol;mur;aspect;tonalite;R_slip;C_slip;thickness;images_url;packing_list;sli_url")
#browser = webdriver.Chrome("C:/chromedriver.exe")  # Optional argument, if not specified will search path.
driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
#driver = webdriver.PhantomJS(executable_path=r'C:\Users\Alexandre\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe')
driver.set_window_size(800, 550)
#browser.maximize_window()
with open("s-url.txt") as in_file:
    for url in in_file:
        # get website
        driver.get(url.strip())
        items = driver.find_elements_by_class_name("portfolio-item")
        main_window = driver.current_window_handle
        for item in items:
            item.find_elements_by_class_name("right-icon")[0].send_keys(Keys.CONTROL + Keys.RETURN)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            driver.switch_to_window(main_window)
                
            #product_name = driver.find_element_by_xpath(".//div[2]/div[1]/h2").text
            #product_name = driver.find_element_by_xpath("fancy-title")[0].text
            #product_name_container = driver.find_elements_by_class_name("fancy-title")
            #product_name=""
            #for idx, val in enumerate(product_name_container):
                #product_name = val.text
            product_name = driver.title.replace(" | S","")
            product_ref = driver.find_elements_by_class_name("ref")[0].text
            price_code=""
            serie=""
            size=""
            material=""
            relieve=""
            quality=""
            exterior=""
            rectified=""
            p_list = driver.find_elements_by_xpath('.//*[@class="info"]/p')
            for idx, val in enumerate(p_list) :
                if "Código de precio:" in val.text :
                    price_code = val.text.replace("Código de precio:","").replace("\n","")
                if "Serie:" in val.text :
                    serie = val.text.replace("Serie:","")
                if "Formato:" in val.text :
                    size = val.text.replace("Formato:","")
            p_list2 = driver.find_elements_by_xpath('.//*[@class="info"]/div/p')
            for idx, val in enumerate(p_list2) :
                if "Group Cat:" in val.text :
                    material = val.text.replace("Group Cat:","")
                if "Relieve:" in val.text :
                    relieve = val.text.replace("Relieve:","")
                if "Calidad" in val.text :
                    quality = val.text.replace("Calidad:","")
                if "Uso exterior:" in val.text :
                    exterior = "oui"
                if "Rectificado:" in val.text :
                    rectified = "oui"
                
            sol=""
            mur=""
            aspect=""
            tonalite=""
            R_slip=""
            C_slip=""
            thickness=""
            icons = driver.find_elements_by_xpath('.//*[@class="icono"]/img')
            for idy, val in enumerate(icons) :
                if "http://rssliwebtest.s3.amazonaws.com/dms_files/R_ICON_9.jpg" in val.get_attribute('src') :
                    sol = "oui"
                if "http://rssliwebtest.s3.amazonaws.com/dms_files/CAT_79_ICO45.jpg" in val.get_attribute('src') :
                    sol = "oui"
                if "Pavimento" in val.get_attribute("title") :
                    sol = "oui"
                if "revestimiento" in val.get_attribute("title") :
                    sol = "oui"
                if "http://rssliwebtest.s3.amazonaws.com/dms_files/R_ICON_2.jpg" in val.get_attribute('src') :
                    aspect = "mat"
                if "Tonalidad" in val.get_attribute("title") :
                    tonalite = val.get_attribute("title").replace("Tonalidad ","")
                if "Lappato" in val.get_attribute("title") :
                    aspect = "lappato"
                if "http://rssliwebtest.s3.amazonaws.com/dms_files/20141202183737-E9-ICO69-150122124641.jpg" in val.get_attribute('src') :
                    R_slip = "R12"
                if "http://rssliwebtest.s3.amazonaws.com/dms_files/20141202183737-E9-ICO68-150122124623.jpg" in val.get_attribute('src') :
                    R_slip = "R11"
                if "http://rssliwebtest.s3.amazonaws.com/dms_files/20141202183737-E9-ICO67-150122124525.jpg" in val.get_attribute('src') :
                    R_slip = "R10"
                if "http://rssliwebtest.s3.amazonaws.com/dms_files/20141202183737-E9-ICO66-150122124453.jpg" in val.get_attribute('src') :
                    R_slip = "R9"
                if "R9" in val.get_attribute("title") :
                    R_slip = "R9"
                if "R10" in val.get_attribute("title") :
                    R_slip = "R10"
                if "R11" in val.get_attribute("title") :
                    R_slip = "R11"
                if "R12" in val.get_attribute("title") :
                    R_slip = "R12"
                if "Deslizamiento" in val.get_attribute("title") :
                    C_slip = val.get_attribute("title").replace("Deslizamiento: ","")
                if "Espesor" in val.get_attribute("title") :
                    thickness = val.get_attribute("title").replace("Espesor ","")
                if "Revestimiento" in val.get_attribute("title") :
                    mur = "oui"
                if "Brillo" in val.get_attribute("title") :
                    aspect = "brillant"

            packing_list = ""
            packing = driver.find_elements_by_class_name("pull-left")
            for pull in packing:
                ps = pull.find_elements_by_xpath('.//p')
                for idy, val in enumerate(ps) :
                    packing_list += val.text
                    packing_list += ";"
            #print(packing_list)
            
            photos_frame = driver.find_elements_by_class_name("slider-wrap")[0]
            photos = photos_frame.find_elements_by_class_name("photosw")
            images_url = ""
            for photo in photos:
                photo_url = photo.get_attribute('href')
                image_name = photo_url.rsplit('/',1)[1]
                new_image_name = "carrelage-sli-"+serie.replace(" ","-").replace("/","-")+"-"+product_name.replace(" ","-").replace(".","").replace(",","").replace(";","")+"-"+product_ref+"-"+image_name
                new_image_name = new_image_name.replace(" ","-")
                urllib.request.urlretrieve(photo_url, new_image_name)
                images_url += "//"+new_image_name
            #print(images_url)

            print(product_name+";"+product_ref+";"+price_code+";"+serie+";"+size+";"+material+";"+relieve+";"+quality+";"+exterior+";"+rectified
                  +";"+sol+";"+mur+";"+aspect+";"+tonalite+";"+R_slip+";"+C_slip+";"+thickness+";"+images_url+";"+packing_list+";"+driver.current_url)
            
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
            driver.switch_to_window(main_window)
            

                
            
                
            
        
            
