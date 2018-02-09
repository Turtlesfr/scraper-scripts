from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions    import StaleElementReferenceException
from selenium.common.exceptions    import WebDriverException
from selenium.common.exceptions    import TimeoutException as SeleniumTimeoutException
from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
#browser = webdriver.Firefox()
#type(browser)
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#driver = webdriver.Chrome("C:/chromedriver.exe")  # Optional argument, if not specified will search path.
driver = webdriver.Firefox()
driver.get('http://www.pp.com/recherche.php')

linkElem = driver.find_element_by_link_text('Recherche avancée')
type(linkElem)
linkElem.click()
naf_input = driver.find_element_by_id('naf_av')
naf_input.send_keys('7490A')
geo_input = driver.find_element_by_id('geo_av')
geo_input.send_keys('01')
trouver_input = driver.find_element_by_id('bouton_trouver_av')
trouver_input.click()

companies = driver.find_element_by_id("notice_list")
company_list = companies.find_elements_by_xpath('.//*[@itemtype="http://data-vocabulary.org/Organization"]')
#print (len(company_list))

page_next = driver.find_elements_by_class_name("next")[0]
page_next.click()

for company in company_list:
    comp_name = company.find_element_by_xpath('.//span[@itemprop="name"]').text
    street_name = company.find_element_by_xpath('.//span[@itemprop="street-address"]').text
    postal_code = company.find_element_by_xpath('.//span[@itemprop="postal-code"]').text
    city_name = company.find_element_by_xpath('.//span[@itemprop="locality"]').text
    tel = company.find_element_by_xpath('.//span[@itemprop="tel"]').text
    tel2 = company.find_elements_by_xpath('.//span[@itemprop="tel"]')[1].text
    salaries = company.find_elements_by_class_name("results_data")[0].text
    siret = company.find_elements_by_class_name("results_data")[1].text
    domaine = company.find_elements_by_class_name("puce_domaine")[0].text

    print("---")
    print(comp_name)
    print(street_name)
    print(postal_code)
    print(city_name)
    print(tel)
    print(tel2)
    print(salaries.replace("Effectif établ : ",""))
    print(siret.replace("Siret : ",""))
    
    
    
    plusdinfo_btn = company.find_element_by_link_text("Plus d'infos sur l'entreprise")
    #plusdinfo_btn.click()
    findMoreUrl = plusdinfo_btn.get_attribute('onclick')
    findMoreUrl = find_between(findMoreUrl,"url: '","', options")
   # print(findMoreUrl)
    driver.execute_script("window.open('');")
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    driver.get('http://www.pp.com'+findMoreUrl)
    iframe_address = driver.find_element_by_tag_name("iframe").get_attribute("src")
    driver.get(iframe_address)

    #driver.switch_to_frame(driver.find_element_by_xpath('.//*[@id="eco_emb_body_main_back"]/iframe'))

    societe = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[1]').text
    #print(societe.replace("Société","").replace("\n","").replace(":",""))
    siege = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[2]').text
    print(siege.replace("Siège :","").replace("\n","").replace(":",""))
    rcs = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[3]').text
    print(rcs.replace("RCS :","").replace("\n","").replace(":",""))
    activite = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[4]').text
    print(activite.replace("Activité :","").replace("\n","").replace(":",""))
    date_de_creation = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[5]').text
    print(date_de_creation.replace("Date de création :","").replace("\n","").replace(":",""))
    forme_juridique = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[6]').text
    print(forme_juridique.replace("Forme juridique :","").replace("\n","").replace(":",""))
    capital_social = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[7]').text
    print(capital_social.replace("Capital social :","").replace("\n","").replace(":",""))
    dirigeant_principal = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[8]').text
    print(dirigeant_principal.replace("Dirigeant principal :","").replace("\n","").replace(":",""))
    etablissements = driver.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[9]').text
    print(etablissements.replace("Etablissements :","").replace("\n","").replace(":",""))
    print("\n")
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    # try:
    #   box = driver.wait.until(EC.presence_of_element_located(By.NAME, "q")))
    
    #hop = company.find_element_by_xpath('.//*[@id="blocHaut"]/div[1]/p[1]/a').text
    #print(hop)


