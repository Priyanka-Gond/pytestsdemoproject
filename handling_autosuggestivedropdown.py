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
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("ind")
time.sleep(5)
lst=driver.find_elements(By.CSS_SELECTOR,"ul[id='ui-id-1'] li")
time.sleep(5)
for i in lst:
    if i.text=="India":
        i.click()
        break
msg=driver.find_element(By.XPATH,"//input[@id='autocomplete']").get_attribute("value")
print(msg)
assert msg == "India"
#print(len(lst))
time.sleep(5)
