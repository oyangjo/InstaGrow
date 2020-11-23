import Utils
is_long = input('long? (y/n): ')
if is_long == '': is_long = 'n'

cur = Utils.load_pickle("username_cur")
cur_g_idx = Utils.load_pickle("username_cur_g_index")
cur_y_idx = Utils.load_pickle("username_cur_y_index")
prev = Utils.load_pickle("username_prev")
recycle = Utils.load_pickle("username_recycle")
green = Utils.load_pickle("username_g")
yellow = Utils.load_pickle("username_y")
red = Utils.load_pickle("username_r")

Utils.display_results(is_long, ["recycle", "red", "yellow", "green", "current", "current green index", "current yellow index", "previous"], [list(recycle.keys()), red, yellow, green, cur, cur_g_idx, cur_y_idx, prev])

# print("CURRENT: \n" + str(cur))
# print("-------------")
# print("PREVIOUS: \n" + str(prev))
# print("-------------")
# print("RECYCLE: \n" + str(recycle.keys()))
# print("-------------")
# print("RED: \n" + str(red))
# print("-------------")
# print("YELLOW: \n" + str(yellow))
# print("-------------")
# print("GREEN: \n" + str(green))
# print("-------------")
# print("# of current: " + str(len(cur)))
# print("# of previous: " + str(len(prev)))
# print("# of recycle: " + str(len(recycle)))
# print("# of red: " + str(len(red)))
# print("# of yellow: " + str(len(yellow)))
# print("# of green: " + str(len(green)))

