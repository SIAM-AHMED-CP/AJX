import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
    #if "32" in arch:
        #import bb32
    if "64" in arch:
        import DON
except:
        
        print("An error occured")
