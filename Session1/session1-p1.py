from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_field=driver.find_element("name","q")
search_field.send_keys("hello")
search_field.send_keys(Keys.RETURN)
sleep(100)
