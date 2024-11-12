#https://rahulshettyacademy.com/seleniumPractise/#/
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from urllib3.util import wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

# Initialize the Chrome driver using Service and ChromeDriverManager
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
lst=driver.find_elements(By.XPATH,"(//button[@type='button'][normalize-space()='ADD TO CART'])")
sum=0
for i in lst:
    i.click()
driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
driver.implicitly_wait(2)
lst2=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
for j in lst2:
    sum =int(j.text)+sum
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()
waittime=WebDriverWait(driver,10)
waittime.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
tot=driver.find_element(By.CSS_SELECTOR,"span[class='totAmt']")
totamt=int(tot.text)
assert sum==totamt
print(sum)









