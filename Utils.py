import pickle
import logging
import requests

from bs4 import BeautifulSoup 

URL = "https://www.instagram.com/{}/"

# convert instagram follower numbers to int
def convert_to_int(s):
    if ('m' in s):
        s = s.replace('m', '')
        return int(float(s) * 1000000)
    elif ('k' in s):
        s = s.replace('k', '')
        return int(float(s) * 1000)
    elif (',' in s):
        s = s.replace(',', '')
        return int(s)
    else:
        return int(s)

def calc_ratio(a, b):
    return a/b if b != 0 else 1 
  
# scrape function 
def scrape_data(username): 
    user_info = []
    r = requests.get(URL.format(username))   # getting the request from url 
    str = BeautifulSoup(r.text, "html.parser")  # converting the text 

    meta = str.find("meta", property ="og:description")  # finding meta info
    if(meta):
        s = meta.attrs['content']
        s = s.split("-")[0] 
        s = s.split(" ") 

        # assigning the values 
        user_info.append( convert_to_int(s[0]) )  #followers
        user_info.append( convert_to_int(s[2]) )  #followings
        user_info.append( convert_to_int(s[4]) )  #num of posts
        user_info.append( calc_ratio(convert_to_int(s[0]), convert_to_int(s[2])) ) #ratio

    user_info.append( "\"is_private\":true" in str.prettify() )  # checking if private
    return user_info

def store_pickle(file_name, item):
    dbfile = open('Memory/' + file_name, 'wb') 
    pickle.dump(item, dbfile)                      
    dbfile.close() 

def load_pickle(file_name):
    dbfile = open('Memory/' + file_name, 'rb')      
    item = pickle.load(dbfile) 
    return item

def display_results(is_long, l_str, l):
    if is_long == 'y':
        for i in range(len(l)):
            print(l_str[i].upper() + ": " + str(l[i]))
            print("-------------")
    
    for i in range(len(l)):
        print("# of " + l_str[i] + ": " + str(len(l[i])))

def my_logger():
    logFormat = '[%(levelname)s] [%(asctime)s] - %(message)s'
    logging.basicConfig(level=logging.INFO, format=logFormat,
        handlers=[logging.FileHandler("current.log"), logging.StreamHandler()]
    )
    
