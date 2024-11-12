from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
l=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
print(l)
for i in l:
    if i.get_attribute("value")=="radio2":
        i.click()
        time.sleep(2)
        assert i.is_selected()
        break
for i in l:
    print(i.get_attribute("value"))
