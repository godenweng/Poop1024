from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

browser =Chrome()
browser.get("https://www.momoshop.com.tw/main/Main.jsp")
searchFileld = browser.find_element_by_id("keyword")
searchFileld.clear()
searchFileld.send_keys("電視")
searchFileld.send_keys(Keys.RETURN)
time.sleep(100)
browser.close()