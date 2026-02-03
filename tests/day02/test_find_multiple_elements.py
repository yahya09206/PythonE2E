from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

def test_find_multiple_elements():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.navigate().to("https://practice.cydeo.com")

    all_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "A")
    print(len(all_links))

    for link in all_links:
        print(link.text)

    
    time.sleep(3)

    driver.quit()