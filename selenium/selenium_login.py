from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Import 'Service' to get rid of deprecation error in terminal
serv = Service("/Users/David/Revature/chromedriver")
# Otherwise just include the path for chromedriver inside parentheses after 'Chrome'
driver: WebDriver = webdriver.Chrome(service=serv)
try:
    driver.get("http://localhost:5000/")
    sleep(1)

    # searchbar: WebElement = driver.find_element_by_name()  <- Deprecated find-by method
    username: WebElement = driver.find_element(by=By.ID, value="user")
    password: WebElement = driver.find_element(by=By.ID, value="pass")
    username.send_keys("Heather")
    username.send_keys(Keys.ENTER)
    password.send_keys("1")
    password.send_keys(Keys.ENTER)

    # sleep(1)
    # searchbar.send_keys(Keys.ARROW_DOWN)
    # sleep(2)
    # searchbar.send_keys(Keys.ENTER)

    # searchbar.send_keys("Super Smash Characters" + Keys.ENTER)
    # searchbar.send_keys("Super Smash Characters\n")
    assert "TRMS User Page" == driver.title
except AssertionError as a:
    print("Incorrect Title of Page Found")
finally:
    sleep(2)
    driver.quit()
