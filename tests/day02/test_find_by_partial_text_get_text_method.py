from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

def test_find_by_partial_text_get_text_method():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://practice.cydeo.com")
    driver.title

    time.sleep(3)

    driver.quit