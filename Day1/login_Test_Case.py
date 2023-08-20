import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.set_page_load_timeout("10")
driver.get("https://hr.orbund.com/einstein-freshair/index.jsp")
driver.find_element(By.NAME, "username").send_keys("hossain9")
driver.find_element(By.NAME, "password").send_keys("hosS@IN9")
driver.find_element(By.XPATH, "//select[@name = 'role']/option[text() = 'Employee']").click()
driver.find_element(By.NAME, "B3").click()
time.sleep(4)
driver.quit()
