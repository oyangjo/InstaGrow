import os
import glob
import logging
from datetime import date

import Utils
import pandas as pd

MAX_FOLLOWERS = 7400
MIN_FOLLOWERS = None
MAX_FOLLOWING = None
MIN_FOLLOWING = 100
MAXRATIO = 2
MEHRATIO = 0.8
MIN_POST = 1

def main():
    #calling logger
    Utils.my_logger()

    logging.info("***Read csv's username***")
    #------- read csv to username ---------
    file_path = "RawData/"
    files = glob.glob(file_path + '*.csv')
    username = pd.DataFrame()
    for f in files:
        df = pd.read_csv(f)
        username = pd.concat([username, df["owner.username"]])
    username = list(pd.unique(username[0]))     #only getting the unique usernames
    logging.info("Only getting unique usernames")
    num_username = len(username)
    logging.info("Complete!")

    #load all my data
    username_g = Utils.load_pickle("username_g")
    username_y = Utils.load_pickle("username_y")
    username_r = Utils.load_pickle("username_r")
    username_recycle = Utils.load_pickle("username_recycle")

    logging.info("***Start filtering each username into green, yellow, and red***")
    logging.info("You have " + str(num_username) + " usernames to filter")
    #filter each usernames into g, y, r
    green, yellow, red = [], [], set()
    for i, un in enumerate(username):

        logging.info( "(" + str(i) + "/" + str(num_username) + "): " + str(un) )

        if (un in username_r or un in username_recycle):    #if private/bad criteria or visited
            logging.info("private or visited")
            continue
        
        try:
            #------- get info -------
            followers, following, posts, ratio, is_private = Utils.scrape_data(un)   # calling scrape function 

            #------- filter ---------
            if(is_private or followers > MAX_FOLLOWERS or following < MIN_FOLLOWING or ratio > MAXRATIO or posts < MIN_POST):  #red
                red.add(un)
                logging.info("red")
            elif(ratio > MEHRATIO and following < 1000):  #yellow
                yellow.append(un)
                logging.info("yellow")
            else:   #green
                green.append(un)
                logging.info("green")
        except ValueError:
            logging.info("Could not grab {}'s meta data".format(un))

    logging.info("***Displaying Results***")
    #displaying results
    Utils.display_results(["green", "yellow", "red"], [green, yellow, red])

    ans = input("Do you want to add these data in memory? (y/n)")   #check if user wanna add the data
    if ans == 'n':
        return

    logging.info("***Update Memory***")
    #------ writing to memory -----
    Utils.store_pickle("username_g", username_g + green);
    Utils.store_pickle("username_y", username_y + yellow);
    Utils.store_pickle("username_r", set.union(username_r, red));
    logging.info("Finished!!!")


    #deleting csv's
    for f in files:
        os.remove(f)

# main function 
if __name__=="__main__": 
    main()
