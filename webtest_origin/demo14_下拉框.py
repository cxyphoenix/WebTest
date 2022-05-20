import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.implicitly_wait(10)
url = r"E:\webtest01\webtest_origin\source\注册A.html"

driver.get(url)

select = Select(driver.find_element_by_id("selectA"))

# select.select_by_index(1)

# select.select_by_value(select_by_index)

# select.select_by_visible_text("")
print(select.options)
print(len(select.options))

for option in select.options:
    option.click()
    time.sleep(2)

time.sleep(11)
driver.quit()