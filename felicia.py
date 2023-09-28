from chatterbot import ChatBot
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys




#ABRIR NAVEGADOr
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)


#buscar os contatos


contatos = ["LORENA VIDA COSTA"]
mensagem ="ola a todas teste de automação"


def buscar_contato():
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#enviar uma mensagem
    
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(3)
    campo_mensagem[1].send_keys(Keys.ENTER)
       
#buscar contatos
for contato in contatos:
    buscar_contato()
    enviar_mensagem(contato)


