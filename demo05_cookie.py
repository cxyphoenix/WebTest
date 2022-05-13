import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("")

driver.add_cookie({"name":"BDUSS","ff":""})

time.sleep(1)

driver.refresh()

driver.quit()