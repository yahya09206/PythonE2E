from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_google_title():

	# setup
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	driver.implicitly_wait(10)

	# navigate to google
	driver.get("https://www.google.com")

	# assert title
	assert "Google" in driver.title 


	# cleanup
	driver.quit