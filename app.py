from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#Instantiate our Webdriver Object
driver = webdriver.Chrome()

driver.get("http://www.smartystreets.me")
time.sleep(1)

# find signup button and click
signup_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/header/div/div[2]/nav/div/li/a/div")
signup_button.click()
time.sleep(2)

#Continue with free trial
free_trial_btn = driver.find_element(By.CLASS_NAME, "btn--blue-large")
free_trial_btn.click()
time.sleep(2)

#Click checkbox and click continue with email
checkbox = driver.find_element(By.CLASS_NAME, "PrivateSwitchBase-input")
checkbox.click()
time.sleep(2)

continue_with_email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/a[3]/div")
continue_with_email.click()
time.sleep(2)

# action = ActionChains(driver)
# action.key_down(Keys.CONTROL)
# action.key_down(Keys.SHIFT)
# action.send_keys("+")
email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[1]/form/div[1]/div/input")
element.send_keys(Keys.CONTROL, Keys.SHIFT, '=')
time.sleep(2)


#Navigate Forward
# driver.forward()
#
# #Navigate Backward
# driver.back()
#
# #refresh the page
# driver.refresh()
#
# time.sleep(1)
#
#
# time.sleep(1)
#
#
# time.sleep(1)
#
#
# time.sleep(1)
#
#
# time.sleep(1)
#
#
# driver.quit()
