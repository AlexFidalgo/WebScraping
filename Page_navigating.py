import time
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming") # with this we don't need to inspect the page
link.click()

try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")))
    element.click()
    # Now we'll inspect the 'Get Started' button
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "sow-button-19310003")))
    element.click()
    # Now let's return to the home page
    driver.back() # We also have driver.forward()
    driver.back()
    driver.back()
except:
    driver.quit()

