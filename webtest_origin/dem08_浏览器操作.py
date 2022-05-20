import time

from selenium import webdriver

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

url = r"E:\webtest01\webtest_origin\source\注册A.html"
driver.get(url)

driver.set_window_size(500, 600)
time.sleep(1)

driver.set_window_position(500, 300)
a = driver.find_element_by_id("AAA")

a.click()
time.sleep(1)
# 回退
driver.back()
time.sleep(1)

# 刷新
driver.refresh()
time.sleep(1)

# 前进
driver.forward()

aa = driver.find_element_by_id("fwA")
aa.click()
time.sleep(2)

driver.close()
driver.quit()

