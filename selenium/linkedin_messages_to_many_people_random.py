from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
s = 2

a = 'Você é uma pessoa esplêndida, nada deter-te-á'
b = 'Em rio que tem piranha, jacaré nada de costas'
c = 'O mundo é uma bola, se fossem duas, seria um saco'
d = 'Perón não teve filhos, sua mulher evita'
e = 'Com esse currículo, como voce não está na nasa?'
f = 'Solidariedade e companheirismo nos acompanham por todo o caminho. Um abraço'
g = 'Beijo'
h = '$%¨&()_+*&%$'
i = 'Good dia'
j = 'Hola, que tal? Quieres hablar, guapo?'
l = [a,b,c,d,e,f,g,h,i,j]
driver = webdriver.Chrome("C:/Users/AlexFidalgoZamikhows/chromedriver.exe")
#driver.get("https://www.linkedin.com/")
driver.get("https://www.linkedin.com/login/pt?trk=homepage-basic_ispen-login-button")

time.sleep(s)
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys("******")
password.send_keys("******")
time.sleep(s)


submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(s)

driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=ZSq")
time.sleep(s)
all_buttons = driver.find_elements_by_tag_name("button")
message_buttons = [btn for btn in all_buttons if btn.text == 'Message']

i = 0
z = 0
while (z < 4):
    for i in range(0, len(message_buttons)):
        
        driver.execute_script("arguments[0].click();", message_buttons[i])
        time.sleep(s)
        #note that the div class for the text box changes once we click on the box to fill it (is-active now)
        main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__contenteditable t-14')]")
        driver.execute_script("arguments[0].click();", main_div)
        paragraphs = driver.find_elements_by_tag_name("p")
        paragraphs[-5].send_keys(random.choice(l))
        time.sleep(s)
        submit = driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(s)
        close_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        driver.execute_script("arguments[0].click();", close_button)
        time.sleep(s)
    z = z + 1
#trecho para encontrar onde está a mensagem 'gggg' que voce escreveu na caixa de mensagem
'''
paragraphs = driver.find_elements_by_tag_name("p")
counter = 0
for p in paragraphs:
    print(counter)
    print(p.text)
    counter += 1
# no caso sabemos que é na posição paragraphs[-5]
'''
