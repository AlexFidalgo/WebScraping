from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
s = 5

driver = webdriver.Chrome("C:/Users/AlexFidalgoZamikhows/chromedriver.exe")
driver.get("https://linkedin.com")

time.sleep(5)
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys("arturtinem1995@yahoo.com.br")
password.send_keys("calculus")
time.sleep(s)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(s)

driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=ZSq")
time.sleep(s)
all_buttons = driver.find_elements_by_tag_name("button")
message_button = [btn for btn in all_buttons if btn.text == 'Message']

message_button[0].click()
time.sleep(s)
#note that the div class for the text box changes once we click on the box to fill it (is-active now)
main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__contenteditable t-14')]")
main_div.click()
paragraphs = driver.find_elements_by_tag_name("p")
paragraphs[-5].send_keys("que belo perfil")
time.sleep(s)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
#data-control-name="overlay.close_conversation_window"
close_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]").click()

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
    
   



