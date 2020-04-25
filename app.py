from selenium import webdriver
from bs4 import BeautifulSoup
import os 
import time

#DataSet
videoNames = []
links = []

#Enter Name of Song
songNames = input("Enter Song Names(Seperated by ,):\t")
songs_list = songNames.split(",")
download_directory = '/home/madhav/Music'

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', download_directory)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'audio/mpeg')


#Open Driver
driver = webdriver.Firefox(profile)
for i in range(len(songs_list)):
    #Open 
    videoNames = []
    links = []
    Youtube = "https://www.youtube.com"
    driver.get(Youtube)

    #Search Song
    element = driver.find_element_by_name("search_query")
    element.send_keys(songs_list[i])
    driver.find_element_by_id("search-icon-legacy").click()

    #Show Results
    content = driver.page_source
    soup = BeautifulSoup(content,"html.parser")
    x = 0
    #tag = soup.find("div", id = "primary")
    for a in soup.find_all("a", href = True , id = "video-title"):
        if x == 10:
            break
        link = Youtube + a.get("href")
        links.append(link)
        videoNames.append(a.get_text())
        x+=1

        #Video Options
        #print("Video #",x,"\nName:",videoNames[x-1],"\n")

    """ch = int(input("Enter the Video Number you want to download:\t"))
    while ch not in range(1,11,1):
        print("Enter correct number!")
        ch = int(input("Enter the Video Number you want to download:\t"))
    """
    ch=0
    Ytmp3 = "https://ytmp3.cc/en13/"
    driver.get(Ytmp3)

    element = driver.find_element_by_name("video")
    element.send_keys(links[ch])
    driver.find_element_by_id("submit").click()
    time.sleep(3)
    div = driver.find_element_by_link_text("Download").click()
    #name_final = videoNames[ch].strip()
    #file_name = download_directory + "/" + name_final + ".mp3"
    #file_name = file_name.strip()
    #print("\n",file_name)

time.sleep(1000)
driver.close()
