import csv
import requests
from selenium import webdriver
import time


with open('file.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)


    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('') #website link in the brackets

        time.sleep(2)
        name_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input') #xpath
        name_field.send_keys(line[0])

        age_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input') #xpath
        age_field.send_keys(line[1])

        score_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input') #xpath
        score_field.send_keys(line[2])

        submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span') #xpath
        submit.click()

