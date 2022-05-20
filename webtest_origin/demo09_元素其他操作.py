import time

from selenium import webdriver

path = r"C:\python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

url = r"E:\webtest01\webtest_origin\source\注册A.html"
driver.get(url)
# 元素大小
print("size,", driver.find_element_by_id("AAA").size)
print("text:", driver.find_element_by_id("AAA").text)
print("属性值", driver.find_element_by_id("AAA").get_attribute("href"))
print("当前页面的title", driver.title)
print("当前页面的url", driver.current_url)

print("span标签是否可见", driver.find_element_by_tag_name("span").is_displayed())
print("标签是否可用", driver.find_element_by_id("cancelA").is_enabled())

driver.quit()

