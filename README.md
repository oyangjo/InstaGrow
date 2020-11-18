# InstaGrow
The goal of this repo is to gain profile exposure by liking target audiences' posts. We retrieve the target audiences' username through inputing posts' URL's. For example, I really like @kingjames post. So, I input his specific post URL. InstaGrow will record all the commenters on the post. Then, base on user define criteria, it will classify these users, commenters, into three different groups: green, yellow, and red. Green is users who have good criteria or higher chance to follow you; yellow is mediocore criteria with lower chance to follow you; red is bad criteria that will very unlikely to follow you or a private account. Lastly, you can run ThreeLikes.py and define the amount of users to like per session. We grab 80% green profiles and 20% yellow profiles. Instagrow will automatically like the most recent three posts of the commenters. 

Third Party plug-ins: InstaTouch, BeautifulSoup4, and InstaPy

# Instructions
0. Add url's to URL.txt (one url per line) to parse commenters info
1. Run `python3 Run1.py` to classify commenters into three different groups
2. Run `python3 ThreeLikes.py` to start liking session

## Special Instructions
### Clearing data
Instagram been changing a bunch of bot monitor critera, so do the following to decrease the chances getting caught:
- Clear cookies on firefox
- Run `python3 ClearLogs.py` to clear all the logs on your device

### Getting memory
Since the memory of username green, yellow, and red is changing constantly. You can run the folloing to keep track:
- `python3 GetMemory`

### Crashed Repair
There might be times when the program crashes in the middle of the session: instagram blocked you or computer died.
- Run `python3 CrashRepair.py`
- Enter the number when the program crashed

### Changing g, y, r criteria
- Go to __ProcessInfo.py__ 
- Edit the constants on top

### Changing num of likes, possibility of like and comment, and comment content
- Go to __ThreeLikes.py__ 
- Edit the constants on top
