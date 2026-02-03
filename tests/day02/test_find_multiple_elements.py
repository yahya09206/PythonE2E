from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

def test_find_multiple_elements():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://practice.cydeo.com")

    all_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "A")
    print(len(all_links))

    for link in all_links:
        print(link.text)

    first_item = all_links[0]
    print(first_item.text)

    
    time.sleep(10)

    driver.quit()