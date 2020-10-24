'''
Performs three likes on most recent 40 green and 10 yellow profiles
It'll modify username_prev and username_cur before the session starts
It'll modify username_g, username_y, and username_recycle after session ends
'''

import datetime
import Utils
from instapy import InstaPy
from instapy import smart_run

NUM = input("Number of profiles to like (recommended 50): ")
if (NUM == ''):
  NUM = 50
NUM_G = int(int(NUM)*.8)
NUM_Y = int(int(NUM)*.2)
MAX_L_H = 50
MAX_L_D = 580

insta_username = 'mrjoyang'
insta_password = 'JoecLean423!'
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)
session.set_quota_supervisor(enabled=True, sleep_after=["likes_h", "likes_d"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=MAX_L_H, peak_likes_daily=MAX_L_D)

with smart_run(session):
  #activity
  session.set_comments(["I love your pic!", "Love your style :)", "This is fire!", "Gorgeous!",
                        "You have a great profile", "This is just great :)", "Nothing beats this :)",
                        "Wow! I wish I have posts like that", "Sheesh! I needa step up my photo-game",
                        "This is just simply amazing lol", "Stay safe!", "Stay Safe out there!",
                        "Safety is always first :)", "Hope we all stay safe!", "Safety first!"])
  session.set_do_comment(enabled=True, percentage=20)
  session.set_do_like(True, percentage=80)
  
  #load data
  username_g = Utils.load_pickle("username_g")
  username_y = Utils.load_pickle("username_y")
  username_recycle = Utils.load_pickle("username_recycle")
  username_cur = Utils.load_pickle("username_cur")

  #grab 40 greens and 10 yellows to create username_cur
  Utils.store_pickle('username_prev', username_cur) #store the previous session's info 
  l1 = username_g[:NUM_G]
  l2 = username_y[:NUM_Y]
  username_cur = l1 + l2
  Utils.store_pickle('username_cur', username_cur)  #store the current session's info

  #start session
  session.interact_by_users(username_cur, amount=3, randomize=False, media='Photo')

  #load the new data back to memory
  del username_g[:NUM_G]
  del username_y[:NUM_Y]
  for user in username_cur:
    username_recycle[user] = datetime.date.today()

  Utils.store_pickle("username_g", username_g);
  Utils.store_pickle("username_y", username_y);
  Utils.store_pickle("username_recycle", username_recycle);