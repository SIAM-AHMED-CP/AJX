import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
    if "32" in arch:
        os.system("chmod +x b & ./b")
    #elif "64" in arch:
        #import OP
except:
        
        print("An error occured")
