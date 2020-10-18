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

FLAG = 1
F_NUM = 37
NUM_G = 40
NUM_Y = 10

insta_username = 'mrjoyang'
insta_password = 'JoecLean423'
session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)

with smart_run(session):
  #activity		
  session.set_do_like(True, percentage=100)
  
  #load data
  username_g = Utils.load_pickle("username_g")
  username_y = Utils.load_pickle("username_y")
  username_recycle = Utils.load_pickle("username_recycle")
  username_cur = Utils.load_pickle("username_cur")

  #grab 40 greens and 10 yellows to create username_cur
  l1 = username_g[:NUM_G]
  l2 = username_y[:NUM_Y]
  username_org = l1 + l2

  #if crashed the previous time
  if (FLAG):
    del username_cur[:F_NUM]
    print(username_cur)

  #start session
  session.interact_by_users(username_cur, amount=3, randomize=False, media='Photo')

  #load the new data back to memory
  del username_g[:NUM_G]
  del username_y[:NUM_Y]
  for user in username_org:
    username_recycle[user] = datetime.date.today()

  Utils.store_pickle("username_g", username_g);
  Utils.store_pickle("username_y", username_y);
  Utils.store_pickle("username_recycle", username_recycle);