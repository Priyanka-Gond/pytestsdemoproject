from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver using Service and ChromeDriverManager
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)

# Launch the Google homepage
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.ID, "user-name").send_keys("priyanka")
driver.find_element(By.ID, "password").send_keys(12345)
driver.find_element(By.NAME, "login-button").click()
msg=driver.find_element(By.XPATH, "//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
print(msg.text)
# Optional: Close the browser after a delay
import time
time.sleep(5)
driver.quit()
