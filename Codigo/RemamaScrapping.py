import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


url = "https://www.instagram.com/"
driver.get(url)
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("axarpa9")
driver.find_element(By.NAME, "password").send_keys("remama#134")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys(Keys.ENTER)
time.sleep(2)
urlRem = "https://www.instagram.com/remamadragaorosa/"
driver.get(urlRem)
time.sleep(7)

#links = driver.find_elements(By.TAG_NAME, "a")[40:45]
#print(len(links))
posts = driver.find_elements(By.CLASS_NAME, "x1i10hfl")[40:45]
likes = driver.find_elements(By.CLASS_NAME,"x193iq5w")[40:45]
print(likes)
print(posts)

time.sleep(2)
lista_datas = []

for post in posts:
    post.click()
    time.sleep(2)
    data = driver.find_element(By.TAG_NAME,'time').get_attribute('title')
    lista_datas.append(data)
    driver.back()
    time.sleep(1)
print(lista_datas)
"""
for post in posts:
    post.click()

    time.sleep(2)
    
    dt.append(dat)
    driver.back()
    time.sleep(1)
print(dt)
"""
