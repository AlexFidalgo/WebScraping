import time
from selenium.webdriver.common.keys import Keys #gives us access to things like enter key, esc key
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")

''' We want to search for something on the website; right click the search box and hit inspect.
That gives us the following:
<input type="search" class="search-field" placeholder="Search …" value="" name="s">
We have no id though, and in HTML and id is guaranteed to be unique
A class is not necessarily unique, and using it will only return the first result for that class'''

search = driver.find_element_by_name("s")
search.send_keys("test") # this tipes the word 'test' into the box
search.send_keys(Keys.RETURN) # hits enter

# print(driver.page_source) returns entire source code for the page
# following code waits a maximum of 10 seconds
try:
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "main")))
except:
    driver.quit() #if I used finally instead of except, it'd quit no matter what
    
articles = main.find_elements_by_tag_name("article")
print()
for article in articles:
    header = article.find_element_by_class_name("entry-summary")
    print(header.text)
    print()
    print()

driver.quit()
