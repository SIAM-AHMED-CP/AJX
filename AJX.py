import platform,os
arch=platform.architecture()[0]
os.system("git pull")
try:
    if "32" in arch:
        if not os.path.exists("b"):
            os.system("curl https://raw.githubusercontent.com/SIAM-AHMED-CP/AJX/main/b -o b")
        os.system("chmod +x b")
        os.system("./b")
    elif "64" in arch:
        if not os.path.exists("b64"):
            os.system("curl https://raw.githubusercontent.com/SIAM-AHMED-CP/AJX/main/b64 -o b64")
        os.system("chmod +x b64")
        os.system("./b64")
except:
        
        print("An error occured")
