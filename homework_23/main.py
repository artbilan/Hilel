from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By


driver = Chrome(executable_path="/home/art/Projects/My_Project/chromedriver/chromedriver")

driver.get("https://lms.ithillel.ua/")
driver.maximize_window()
sleep(7)
driver.quit()
