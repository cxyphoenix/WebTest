import time

from selenium import webdriver
from selenium.webdriver import ActionChains

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.implicitly_wait(10)
url = r"E:\webtest01\webtest_origin\source\注册A.html"
driver.get(url)

time.sleep(3)
script = "window.scrollTo(0, 1000)"

driver.execute_script(script)

time.sleep(2)

script = "window.scrollTo(1000, 1000)"
driver.execute_script(script)

time.sleep(4)
driver.quit()