import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.implicitly_wait(10)
url = r"E:\webtest01\webtest_origin\source\注册A.html"

driver.get(url)

userA = driver.find_element_by_id("userA")

emailA = driver.find_element_by_id("emailA")

userA.send_keys("admin123")
time.sleep(1)

userA.send_keys(Keys.BACK_SPACE)
time.sleep(1)

# 复制
userA.send_keys(Keys.CONTROL,"a")
userA.send_keys(Keys.CONTROL, "c")
emailA.send_keys(Keys.CONTROL, "v")
time.sleep(4)
driver.quit()