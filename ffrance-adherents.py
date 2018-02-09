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

with open("promoteurs-f.txt") as in_file:
    for url in in_file:
        # get website
        driver.get(url.strip())
        raison_sociale=""
        adresse = ""
        telephone = ""
        email = ""
        url = ""

        rc = ""
        forme_juridique = ""
        date_creation = ""
        capital = ""
        siret = ""
        ape = ""
        chambre = ""
        dirigeants = ""

        logo = ""
        
        adherent_up = driver.find_element_by_xpath('.//*[@class="adherent-firstext"]')
        adherent_down = driver.find_element_by_xpath('.//*[@class="adherent-secondtext"]')

        logo_name = ""
        
        try:
            logo_div = driver.find_element_by_class_name('field-name-field-vignette')
            logo_link = logo_div.find_element_by_xpath('.//img').get_attribute('src')
            logo_link_clean = logo_link.rsplit('?',1)[0]
            logo_name = logo_link_clean.rsplit('/',1)[1]
            full_logo_filename = os.path.join('D:/PYTHON/f', logo_name)
            urllib.request.urlretrieve(logo_link_clean, full_logo_filename)
        except:
            pass
        
        try:
            raison_sociale = adherent_up.find_element_by_xpath('h1').text
        except:
            pass
        try:
            adresse = adherent_up.find_element_by_class_name('field-name-field-adresse').text.replace('\n', '')
        except:
            pass
        try:
            telephone = adherent_up.find_element_by_class_name('field-name-field-telephone').text.replace('\n', '')
        except:
            pass
        try:
            email = adherent_up.find_element_by_class_name('field-name-field-email').text.replace('\n', '')
        except:
            pass
        try:
            url = adherent_up.find_element_by_class_name('field-name-field-url').text.replace('\n', '')
        except:
            pass
       # print(raison_sociale+";"+telephone+";"+email+";"+url)
        try:
            rc = adherent_down.find_element_by_class_name('field-name-field-rc').text.replace('\n', '')
        except:
            pass
        try:
            forme_juridique = adherent_down.find_element_by_class_name('field-name-field-forme-juridique').text.replace('\n', '')
        except:
            pass
        try:
            date_creation = adherent_down.find_element_by_class_name('field-name-field-date-publication').text.replace('\n', '')
        except:
            pass
        try:
            capital = adherent_down.find_element_by_class_name('field-name-field-capital-social').text.replace('\n', '')
        except:
            pass
        try:
            siret = adherent_down.find_element_by_class_name('field-name-field-no-siret').text.replace('\n', '')
        except:
            pass
        try:
            ape = adherent_down.find_element_by_class_name('field-name-field-code-ape').text.replace('\n', '')
        except:
            pass
        try:
            chambre = adherent_down.find_element_by_class_name('chambre').text.replace('\n', '')
        except:
            pass
        try:
            dirigeants = adherent_down.find_element_by_class_name('field-name-field-description').text.replace('\n', '')
        except:
            pass
        print(raison_sociale+";"+adresse+";"+telephone+";"+email+";"+url+";"+rc+";"+forme_juridique+";"+date_creation+";"+date_creation+";"+capital+";"+siret+";"+ape+";"+chambre+";"+dirigeants+";"+logo_name)
        
