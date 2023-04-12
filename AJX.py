import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
    if "32" in arch:
        import bb32
    elif "64" in arch:
        import bb
except:
        
        print("An error occured")
