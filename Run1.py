'''
Reads url.txt 
Calls instatouch for each url to save csv at RawData
Calls GetInfo.py to categorize the csv to memory

'''

import os
import logging
import validators
import Utils

URL = "https://www.instagram.com/p/B6bxEkoJUkU/"
NUM = input("Number of commenters to scrape per posts: ")

#truncate the log file
with open('current.log', 'w'):
    pass
Utils.my_logger()

logging.info("OOOOOOOOOOOOOOOOOOOOOOOOOO")
logging.info("Starting to RUN!!!")
logging.info("OOOOOOOOOOOOOOOOOOOOOOOOOO")

logging.info("-----Fetching url's from url.txt-----")
#creating list of urls from url.txt
urls = []
f = open("url.txt", "r")    #read url
for u in f:
    u = u.split('\n')[0]
    u = u.split(' ')[0]
    if(validators.url(u)):
        urls.append(u)
logging.info("You have " + str(len(urls)) + " url's")

logging.info("-----Calling instatouch to convert url's to csv's-----")
#calling instatouch for each url to make csv's
os.chdir("RawData")     
for i, url in enumerate(urls):
    logging.info(str(i) + ". " + url)
    os.system("instatouch comments " + url + " -c " + str(NUM) + " -t csv")
    logging.info("Complete!!!")
os.chdir("..")

#calling ProcessInfo to categorize csv usernames to memory
logging.info("-----Calling ProcessInfo.py to categorize and store usernames in memory-----")
os.system("python3 ProcessInfo.py")

logging.info("-----Clearing url.txt-----")
#delete txt file data
with open('url.txt', 'w') as fp: 
    pass
logging.info("Done!!!")