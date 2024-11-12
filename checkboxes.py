from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# Initialize the Chrome driver using Service and ChromeDriverManager
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)

# Launch the Google homepage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
lst=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for i in lst:
    if i.get_attribute("value")=="option3":
        i.click()
        assert i.is_selected()
        break
time.sleep(2)
for j in lst:
    print(j.get_attribute("value"))

