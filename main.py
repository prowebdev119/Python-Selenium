from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import Select
chromedriver_autoinstaller.install() 

userName= "testuser"
userFull="testname"
dateOfBirth= "Feb 3, 2013"
userEmail = "testemail@gmail.com"
bravePath = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"






def main():
  ## [SETUP] ##
  option = webdriver.ChromeOptions()
  option.binary_location = bravePath
  browser = webdriver.Chrome(options=option)
  print("here")
  browser.get("https://help.instagram.com/contact/723586364339719")

  username = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/form/div[1]/input')
  username.send_keys(userName)

  fullName = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/form/div[2]/input')
  fullName.send_keys(userFull)
  email = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/form/div[5]/input')
  email.send_keys(userEmail)

  select = Select(browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[4]/select'))
  select.select_by_index(3)

  sleep(1)
  year = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/form/div[3]/div[2]/div/div/div/a')
  year.click()

  yearCount = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/div/div/ul/li[11]/a/span/span')
  yearCount.click()

  sleep(1)
  month = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/form/div[3]/div[2]/div/div[2]/div/a')
  month.click()

  monthCount = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div/div[1]/div/div/ul/li[3]/a/span/span')
  monthCount.click()



  sleep(1)
  day = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/form/div[3]/div[2]/div/div[3]/div/a')
  day.click()

  dayCount = browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div[1]/div/div/ul/li[14]/a/span/span')
  dayCount.click()

  button = browser.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div[2]/div/form/button')
  button.click()

  sleep(15)

  browser.close()

main()
