from selenium import webdriver
from bs4 import BeautifulSoup
import os 
import time

#Enter Name of Song
songName = input("Enter Song Name:\t")

#Open Driver
driver = webdriver.Firefox()

#Open 
Youtube = "https://www.youtube.com"
driver.get(Youtube)

#Search Song
element = driver.find_element_by_name("search_query")
element.send_keys(songName)
driver.find_element_by_id("search-icon-legacy").click()



time.sleep(10)
driver.close()
