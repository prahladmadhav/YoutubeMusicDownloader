from selenium import webdriver
import time


#Open Driver
driver = webdriver.Firefox()

#
Youtube = "https://www.youtube.com"
driver.get(Youtube)

time.sleep(10)
driver.close()
