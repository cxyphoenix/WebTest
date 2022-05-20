import time

from selenium import webdriver
from selenium.webdriver import ActionChains

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.implicitly_wait(10)
url = r"https://www.baidu.com"
driver.get(url)

action = ActionChains(driver)

more = driver.find_element_by_name("tj_briicon")
print(more)

action.move_to_element(more).perform()

time.sleep(10)

driver.quit()