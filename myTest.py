import random

t = [3, 52, 20, 40, 69]
temp = []

idx = random.sample(range(len(t)), 2)
print("original" + str(t))
print(idx)
for i in idx:
    temp.append(t[i])
for elem in temp:
    t.remove(elem)

print(t)



#stuff relating to cache

# print('123')
# today = datetime.date.today()
# print(yesterday)
# print(today)
# print(today - yesterday > datetime.timedelta(days = 21))
# cur = Utils.load_pickle("username_cur")
# rec = Utils.load_pickle("username_recycle")

# for c in cur:
#     if(c not in rec):
#         rec[c] = datetime.date.today()
#         print(c)

# print(len(rec))
