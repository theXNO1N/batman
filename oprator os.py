import os
import sys
print("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n': sys.exit()
if choice == 'y': os.system("apt upgrade -y > /dev/null 2>&1")
os.system("apt update -y >/dev/null")
os.system("apt install python -y > /dev/null 2>&1")
os.system("apt install python2 -y > /dev/null 2>&1")
os.system("apt install php -y > /dev/null 2>&1")
os.system("apt install python-dev -y > /dev/null 2>&1")
os.system("apt install python3 -y > /dev/null 2>&1")
os.system("apt install java -y > /dev/null 2>&1")
os.system("pkg install root-repo -y > /dev/null 2>&1")
os.system("pkg install unstable-repo -y > /dev/null 2>&1")
os.system("pkg install x11-repo -y > /dev/null 2>&1")
os.system("apt install git -y > /dev/null 2>&1")
os.system("apt install perl -y > /dev/null 2>&1")
os.system("apt install bash -y > /dev/null 2>&1")
