import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

types = {
    "text":  By.PARTIAL_LINK_TEXT,
    "xpath": By.XPATH,
    "tag":   By.TAG_NAME,
    "id":    By.ID,
    "name":  By.NAME,
    "class": By.CLASS_NAME
}

class Element :

    element=None 

    def __init__(self, element) -> None:
        self.element = element

    def innerText(self):
        return self.element.get_attribute('innerText')
    
    def send(self):
        # busca input ou textarea
        return self
    
    def click(self) :
        try:
            self.element.click()
            return True
        except:
            return False


class Navigator :

    driver   = None 

    def __init__(self, site) -> None:
        driver = webdriver.Chrome('chromedriver')
        driver.get(site)
        self.driver = driver

    def findElements(self, type, value) :
        return self

    def findElement(self, type, value) :
        naoEncontrou=True
        count=0
        el=None
        while naoEncontrou and count < 30:
            try:
                if type == 'text':
                    element = self.driver.find_element(types['xpath'], "//*[text()='"+finder+"']")
                else :
                    element = self.driver.find_element(types[type], value)
                naoEncontrou= False
                el = Element(element)
            except:
                time.sleep(1)
                count = count + 1

        return False if naoEncontrou else el

    def press(self):
        # preciona tecla do teclado
        return self

    
