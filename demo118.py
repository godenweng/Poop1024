from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys
browser =Chrome()
browser.get("https://www.python.org")
searchField = browser.find_element_by_name("q")
searchField.clear()
searchField.send_keys("tensorflow")
searchField.send_keys(Keys.RETURN)
time.sleep(10)
browser.close()