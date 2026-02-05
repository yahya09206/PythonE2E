from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time 

def test_find_by_id_name_link_text():

	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

	driver.get("https://www.facebook.com");

	# name: email, pass, login
	email_box = driver.find_element(By.ID, "email")
	time.sleep(3)
	email_box.send_keys("some email here")
	time.sleep(3)


	driver.quit()