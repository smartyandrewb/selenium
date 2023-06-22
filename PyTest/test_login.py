from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

def test_setup():
	global driver
	driver = webdriver.Chrome()
	assert True

def test_navigation():
	driver.get("http://www.smartystreets.me")
	time.sleep(2)
	driver.quit()
	assert True, "Website is down"

def test_bad_test():
	assert False, "test failed"

def test_smarty_login():
	current_time = math.floor(time.time())
	email = "andrew.blonquist+" + str(current_time) + "@smarty.com"

	# Instantiate our Webdriver Object
	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(chrome_options)

	driver.get("http://www.smartystreets.me")
	time.sleep(1)

	# find signup button and click
	signup_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/header/div/div[2]/nav/div/li/a/div")
	signup_button.click()
	time.sleep(2)

	# Continue with free trial
	free_trial_btn = driver.find_element(By.CLASS_NAME, "btn--blue-large")
	free_trial_btn.click()
	time.sleep(2)

	# Click checkbox and click continue with email
	checkbox = driver.find_element(By.CLASS_NAME, "PrivateSwitchBase-input")
	checkbox.click()
	time.sleep(1)

	# find and click continue with email
	continue_with_email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/a[3]/div")
	continue_with_email.click()
	time.sleep(1)

	# find all form elements
	email_input = driver.find_element(By.ID, ":r0:")
	first_name = driver.find_element(By.ID, ":r1:")
	last_name = driver.find_element(By.ID, ":r2:")
	phone_number = driver.find_element(By.ID, ":r3:")
	company_name = driver.find_element(By.ID, ":r4:")
	password = driver.find_element(By.ID, ":r5:")
	confirm_password = driver.find_element(By.ID, ":r6:")
	lookups = driver.find_element(By.NAME, "anticipated_number_of_lookups")
	create_acc_btn = driver.find_element(By.XPATH, "//*[@id='signup-form']/button")

	# write to each form item
	email_input.send_keys(email)
	first_name.send_keys("Andrew")
	last_name.send_keys("Blonquist")
	phone_number.send_keys("800.555.1212")
	company_name.send_keys("Smarty")
	password.send_keys("asdfasdf")
	confirm_password.send_keys("asdfasdf")
	lookups.click()
	time.sleep(3)
	driver.execute_script("arguments[0].click();", create_acc_btn)

	print(email)
	print("asdfasdf")
	assert True, "sign up is broken"
