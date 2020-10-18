# InstaGrow
The goal of this repo is to gain profile exposure by liking target audiences' posts. We retrieve the target audiences' username through inputing posts' URL's. For example, I really like @kingjames post. So, I input his specific post URL. InstaGrow will record all the commenters on the post. Then, base on user define criteria, it will classify these users, commenters, into three different groups: green, yellow, and red. Green is users who have good criteria or higher chance to follow you; yellow is mediocore criteria with lower chance to follow you; red is bad criteria that will very unlikely to follow you or a private account. Lastly, you can run ThreeLikes.py and define the amount of users to like per session. We grab 80% green profiles and 20% yellow profiles. Instagrow will automatically like the most recent three posts of the commenters. 

Third Party plug-ins: InstaTouch, BeautifulSoup4, and InstaPy

## Instructions
1. Add url's to URL.txt (one url per line)
2. Run 'python3 Run1.py' to classify commenters into three different groups
3. Run 'python3 ThreeLikes.py' to start liking session
