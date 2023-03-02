import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
	if "32" in arch:
		import a332
	elif "64" in arch:
		import a364
except:
	print("An error occured")
