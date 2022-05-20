import time

from selenium import webdriver
from selenium.webdriver import ActionChains

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

url = r"E:\webtest01\webtest_origin\source\注册A.html"
driver.get(url)
action = ActionChains(driver)
time.sleep(1)

userA = driver.find_element_by_id("userA")
userA.send_keys("admin")

action.context_click(userA).perform()

action.double_click(userA).perform()

time.sleep(2)
driver.quit()
