import time

from selenium import webdriver
from selenium.webdriver import ActionChains

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

url = r"E:\webtest01\webtest_origin\source\drag.html"
driver.get(url)

action = ActionChains(driver)

source = driver.find_element_by_id("div1")
target = driver.find_element_by_id("div2")

time.sleep(1)

action.drag_and_drop(source, target).perform()

driver.quit()
