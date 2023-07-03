################################################
#                                              #
#  Este script recupera e ordena os links dos  #
#  conteúdos do antigo site sindcelma.com.br   #
#                                              #
################################################

import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

links = [
    "https://www.sindcelma.com.br/search/label/Sindcelma",
    "https://www.sindcelma.com.br/search/label/Sindcelma#archive-page-2",
    "https://www.sindcelma.com.br/search/label/Sindcelma#archive-page-3",
    "https://www.sindcelma.com.br/search/label/Celulose%20e%20Papel",
    "https://www.sindcelma.com.br/search/label/Celulose%20e%20Papel#archive-page-2",
    "https://www.sindcelma.com.br/search/label/Vagas",
    "https://www.sindcelma.com.br/search/label/Educa%C3%A7%C3%A3o%20Sindical",
    "https://www.sindcelma.com.br/search/label/Pautas"
]

meses = [
    '',
    'Janeiro',
    'Fevereio',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

class Item:
    
    def __init__(self, element):
        
        self.data = element.find_element(By.CLASS_NAME, 'meta-item-date').get_attribute('innerText')
        self.link = element.find_element(By.CLASS_NAME, 'item-title').find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        print(self.link)

        match = re.search("(\d+)[de\s]+([^\s]{3,})[de\s]+(\d+)", self.data)
        grups = match.groups()
        mesi  = meses.index(grups[1])
        mess  = "0"+str(mesi) if mesi < 10 else str(mesi)

        self.index = int(grups[2]+mess+grups[0])

    def getLink(self):
        return self.link

    def getData(self):
        return self.data
    
    def getIndex(self):
        return self.index
    
itens = []

for link in links:
    success = False
    print("RESGATANDO EM ======")
    print(link)
    time.sleep(1)

    driver = webdriver.Chrome('chromedriver')
    driver.get(link)
    while not success:
        try:
            element  = driver.find_element(By.CLASS_NAME, 'archive-page-content')
            elements = element.find_elements(By.CLASS_NAME, 'item')
            success  = True
        except:
            print("nao encontrou elemento... tentando novamente")
            time.sleep(1)
    print("Total encontrado: "+str(len(elements)))
    for el in elements:
        itens.append(Item(el))
    

itens.sort(key=lambda x: x.getIndex())

f = open("list.txt", "w")

content = ""
for item in itens:
    content += item.getLink()+"\n"

f.write(content)
f.close()