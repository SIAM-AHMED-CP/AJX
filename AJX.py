import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
    if "32" in arch:
        os.system("chmod +x b")
        os.system("./b")
    elif "64" in arch:
        pass
except:
        
        print("An error occured")
