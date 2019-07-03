import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time

class KupujemProdajem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)

    def testPostAd(self):
        driver = self.driver
        driver.get("https://www.kupujemprodajem.com/index.php")
        postaviOglas = driver.find_element_by_xpath("//a[contains(@class,'bigLink submitAd')]")
        postaviOglas.click()
        username = driver.find_element_by_xpath("(//input[@name='data[email]'])[1]")
        username.clear()
        username.send_keys("nevena.miocinovic@gmail.com")
        password = driver.find_element_by_xpath("//input[@type='password']")
        password.clear()
        password.send_keys("testkupujemprodajem")
        logIn = driver.find_element_by_xpath("//input[@value='Ulogujte se']")
        logIn.click()
        usluga = driver.find_element_by_xpath("//input[@id='data[ad_kind]service']")
        usluga.click()
        #*****
        time.sleep(5)
        a = driver.find_element_by_xpath("(//span[@action-name='label'])[3]")
        a.click()
        time.sleep(1)
        a.click()
        time.sleep(1)
        poducavanje = driver.find_element_by_xpath("//div[@data-value='1412']")
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,ElementNotVisibleException)
        WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(cond.visibility_of(poducavanje))
        poducavanje.click()
        grupa = driver.find_element_by_xpath("//div[@data-value='1462']")
        grupa.click()
        naslovOglasa = driver.find_element_by_xpath("//input[@id='data[name]']")
        self.wait.until(cond.visibility_of(naslovOglasa))

        naslovOglasa.clear()
        naslovOglasa.send_keys("Casovi makroekonomije za studente")
        cenaPoducavanja = driver.find_element_by_xpath("//input[@id='price_number']")
        cenaPoducavanja.send_keys(2000)
        dinari = driver.find_element_by_xpath("//input[@id='currency_rsd']")
        dinari.click()

        action_chains = ActionChains(driver)
        action_chains.key_down(Keys.TAB)
        action_chains.key_down(Keys.TAB)
        action_chains.send_keys("Povoljni casovi")
        action_chains.perform()

        time.sleep(10)

        ## JEDNOM KADA SE KREIRA OGLAS; OVA POLJA SE POPUNJAVAJU AUTOMATSKI I TEST ZATO PUCA

        # mesto = driver.find_element_by_xpath("(//span[contains(.,'Izaberite')])[13]")
        # mesto.click()

        # mestoizbor = driver.find_element_by_xpath("// div[ @class ='uiMenuItem'][contains(., 'Borča')]")
        # mestoizbor.click()

        # ime = driver.find_element_by_xpath("//input[contains(@id,'data[owner]')]")
        # ime.click()
        # ime.clear()
        # ime.send_keys("Ne")

        sledece = driver.find_element_by_xpath("//div[@class='slide-info-top-buttons']//div[@class='adFormPostButtonHolder']//input[@class='submit-button']")
        sledece.click()

        izborpromocije = driver.find_element_by_xpath("//div[@class='adFormServiceTitle'][contains(.,'Standardna vidljivost')]")

        time.sleep(10)
        action_chains.perform()

        izborpromocije.click()

        # sledece1 = driver.find_element_by_xpath("//div[@class='slide-info-top-buttons']//div[@class='adFormPostButtonHolder']//input[@class='submit-button']")

        driver.implicitly_wait(10)

        # sledece1.click()

        fizickolice = driver.find_element_by_xpath("//label[@for='declaration_type_person'][contains(.,'fizičko lice (npr. prodaja polovne lične stvari ili nekretnine)')]")
        fizickolice.click()

        vaseime = driver.find_element_by_xpath("//input[contains(@id,'personEdit')]")
        vaseime.click()
        vaseime.clear()
        vaseime.send_keys("Nevena")

        vaseprezime = driver.find_element_by_xpath("//input[@id='personLastNameEdit']")
        vaseprezime.click()
        vaseprezime.clear()
        vaseprezime.send_keys("Miocinovic")

        mestostanovanja = driver.find_element_by_xpath("//input[@name='data[d_person_location]']")
        mestostanovanja.click()
        mestostanovanja.clear()
        mestostanovanja.send_keys("Beograd")

        ulicaibroj = driver.find_element_by_xpath("//input[@name='data[d_person_address]']")
        ulicaibroj.click()
        ulicaibroj.clear()
        ulicaibroj.send_keys("Nusica 15")

        jmbg = driver.find_element_by_xpath("//input[contains(@name,'data[d_jmbg]')]")
        jmbg.click()
        jmbg.clear()
        jmbg.send_keys("1708994715158")

        brLK = driver.find_element_by_xpath("//input[@name='data[d_id_card_number]']")
        brLK.click()
        brLK.clear()
        brLK.send_keys("00357894")

        mestoizdavanja = driver.find_element_by_xpath("//input[@name='data[d_id_card_location]']")
        mestoizdavanja.click()
        mestoizdavanja.clear()
        mestoizdavanja.send_keys("Beograd")

        garantujem = driver.find_element_by_xpath("//label[contains(.,'*Garantujem za tačnost unetih podataka')]")
        garantujem.click()

        prihvatamuslove = driver.find_element_by_xpath("//label[contains(@for,'accept_yes')]")
        prihvatamuslove.click()

        postavioglaskraj = driver.find_element_by_xpath("(//input[contains(@class,'submit-button')])[13]")
        postavioglaskraj.click()

    def testDeleteAd(self):
        driver = self.driver
        driver.get("https://www.kupujemprodajem.com/index.php")
        postaviOglas = driver.find_element_by_xpath("//a[contains(@class,'bigLink submitAd')]")
        postaviOglas.click()
        username = driver.find_element_by_xpath("(//input[@name='data[email]'])[1]")
        username.clear()
        username.send_keys("nevena.miocinovic@gmail.com")
        password = driver.find_element_by_xpath("//input[@type='password']")
        password.clear()
        password.send_keys("testkupujemprodajem")
        logIn = driver.find_element_by_xpath("//input[@value='Ulogujte se']")
        logIn.click()

        driver.get("https://www.kupujemprodajem.com/user.php?action=welcome")


        obrisi = driver.find_element_by_xpath("//a[contains(.,'Obriši')]")
        obrisi.click()

        time.sleep(5)

        #elem = driver.switch_to.active_element
        driver.switch_to.active_element

        drugirazlog = driver.find_element_by_xpath("//input[ @ id = 'data[reason]other']")
        drugirazlog.click()

        obrisiOglas = driver.find_element_by_xpath("//input[@name='submit[delete]']")
        obrisiOglas.click()

    def tearDown(self):
        self.driver.close()

