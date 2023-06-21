from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.smartystreets.me")
time.sleep(2)
driver.quit()

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