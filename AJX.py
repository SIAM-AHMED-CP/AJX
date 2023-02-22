import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
	if "32" in arch:
		import c2
	elif "64" in arch:
		import c264
except:
	print("An error occured")
