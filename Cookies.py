from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# The elements cookie and cookie_count won't exist on the page instantly when we load it, so we need an implicit wait
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)] #  Goes from 1 (inclusive) to -1 
#(exclusive)



for i in range(1000):
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    # for item in items:
    #     value = int(item.text)
    #     if value <= count:
    #         upgrade_actions = ActionChains(driver)
    #         upgrade_actions.move_to_element(item)
    #         upgrade_actions.click()
    #         upgrade_actions.perform()
    if count >= int(items[0].text):
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(random.choice(items))
        upgrade_actions.click()
        upgrade_actions.perform()
