from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

exp_url = "https://github.com/artbilan/Hilel"
driver = Chrome("/home/art/Projects/My_Project/chromedriver/chromedriver")


def test_to_correct_open_url():
    driver.get("https://github.com/artbilan?tab=repositories")
    driver.maximize_window()
    search_button = driver.find_element(By.XPATH, '//a[@href="/artbilan/Hilel"]')
    search_button.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    driver.close()
    driver.quit()
