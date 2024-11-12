import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver using Service and ChromeDriverManager
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
name="priyanka"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys(name)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alertobj=driver.switch_to.alert
alerttext=alertobj.text
print(alerttext)
alertobj.accept()
assert name in alerttext

