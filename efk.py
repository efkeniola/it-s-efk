#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
    import os,re,time
except IOError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 efk.py")

try:
    os.mkdir("/sdcard/it's efk 2 best")
except OSError:
    pass

abm = """
\033[1;97m      ____  ____   _____  ___    __ ______ 
\033[1;97m     welcone to itz efk hacking tool 
like my page and follow me on Facebook itz efk
\033[1;93m      efk tool
\033[1;93m      |mr eniola
\033[1;93m      
\033[1;97m       instagram efkhacker follow me
\033[1;97m call me itz efk
\033[1;97m----------+---------------------------------------------- 
\033[1;97m(~) Author  : Efk eniola
\033[1;97m(~) Github  : https://github.com/efkeniola/-itz-efk.git
\033[1;97m(~) Fb Page : https://facebook.com/itzefk.3
\033[1;97m-------------------------------------------------
"""

def main():
    os.system("clear")
    print(abm)
    os.system("cd load && python2 __loading__")
    os.system("clear")
    print(abm)
    print("\033[1;97m[\033[1;93m1\033[1;97m] Install infect tool for cloning")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m2\033[1;97m] Install infect extracting tool")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m0\033[1;97m] Tool Logout")
    time.sleep(0.05)
    print("\033[1;97m-------------------------------------------------")
    mx()
def mx():
    tech_abm = raw_input("\n[!] Select a valid option : ")
    if tech_abm =="1":
        os.system("cd data && python2 data")
    if tech_abm =="2":
        os.system("cd exts && python2 exts")
    if tech_abm =="0":
        print("")
        print("\033[1;92mTool Logout Successfull").center(50)
        print("")
        os.system("exit")
    else:
        print("")
        print("\033[1;91mPlease select a valid option").center(50)
        print("")
        time.sleep(1)
        main()
if __name__ == '__main__':
    main()
