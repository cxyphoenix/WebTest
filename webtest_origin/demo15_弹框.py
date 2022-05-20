import time

from selenium import webdriver
from selenium.webdriver import ActionChains

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.implicitly_wait(10)
url = r"E:\webtest01\webtest_origin\source\css_example.html"
driver.get(url)

driver.find_element_by_xpath("/html/body/input[1]").click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)

driver.find_element_by_xpath("/html/body/input[2]").click()
ater = driver.switch_to.alert
time.sleep(1)
print(ater.text)
ater.dismiss()

time.sleep(22)
driver.quit()