'''
This file is used when ThreeLikes crashed in the middle of the session
When FLAG=1, set the F_NUM to the most recent profile was liked before session crashed
The program will continue liking from F_NUM to the rest of username_cur
It'll update username_g, username_y, and username_recycle correctly

1. Set FLAG to 1
2. Set F_NUM to the most recent profile
'''

import datetime
import Utils
from instapy import InstaPy
from instapy import smart_run

F_NUM = int(input("The number that fucked up on: "))

insta_username = 'mrjoyang'
insta_password = 'JoecLean423!'
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

with smart_run(session):
  #activity		
  session.set_comments(["I love your pic!", "Love your style :)", "This is fire!", "Gorgeous!",
                        "You have a great profile", "This is just great :)", "Nothing beats this :)",
                        "Wow! I wish I have posts like that", "Sheesh! I needa step up my photo-game",
                        "This is just simply amazing lol", "Stay safe!", "Stay Safe out there!",
                        "Safety is always first :)", "Hope we all stay safe!", "Safety first!",
                        "OMG!", "Oh my!", "Sheeeesh", "Nice shot!", "Sheeesh! Nice shot!"])
  session.set_do_comment(enabled=True, percentage=20)
  session.set_do_like(True, percentage=100)
  
  #load data
  username_g = Utils.load_pickle("username_g")
  username_y = Utils.load_pickle("username_y")
  username_recycle = Utils.load_pickle("username_recycle")
  username_cur = Utils.load_pickle("username_cur")
  cur_g_idx = Utils.load_pickle("username_cur_g_index")
  cur_y_idx = Utils.load_pickle("username_cur_y_index")

  #grab unfinished usernames for previous session
  username_not_done = username_cur[F_NUM:]

  #start session
  session.interact_by_users(username_not_done, amount=3, randomize=False, media='Photo')

  #load the new data back to memory
  for un in username_cur[:len(cur_g_idx)]:
    username_g.remove(un)
  for un in username_cur[len(cur_g_idx):]:
    username_y.remove(un)
  for un in username_cur:
    username_recycle[un] = datetime.date.today()

  Utils.store_pickle("username_g", username_g);
  Utils.store_pickle("username_y", username_y);
  Utils.store_pickle("username_recycle", username_recycle);