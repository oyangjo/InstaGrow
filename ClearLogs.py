import os

os.chdir('/users/joseph/InstaPy/logs')

for f in os.listdir():
	print("Removing " + f + "...")
	os.system("rm -rf " + f)

print('Finished removing all files')