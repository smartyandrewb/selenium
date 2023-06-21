from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def test_setup():
	global driver
	driver = webdriver.Chrome()

def test_navigation():
	driver.get("http://www.smartystreets.me")
	time.sleep(2)
	driver.quit()

def test_smarty_login():
	return True

def test_bad_test():
	return false
