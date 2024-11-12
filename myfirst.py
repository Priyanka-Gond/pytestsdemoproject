from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options (optional)
def Launchbrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Open browser in maximized mode
    options.add_argument("--disable-infobars")  # Disable infobars
    options.add_argument("--disable-extensions")  # Disable extensions
    options.add_argument("--incognito")  # Open in incognito mode

    # Initialize the Chrome driver using Service and ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Launch the Google homepage
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Optional: Close the browser after a delay
    import time
    time.sleep(5)
    return driver

#driver.quit()
Launchbrowser()
