from selenium import webdriver
from time import sleep

base_url = "https://play1.automationcamp.ir"
driver = webdriver.Chrome()
driver.get(f"{base_url}/forms.html")
sleep(5)
driver.find_element("id", "check_python").click()
checking1 = driver.find_element("id", "check_validate").text
assert checking1 == "PYTHON"
sleep(5)
