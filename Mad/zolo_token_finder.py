#if ur selling or giving this away
#credits zolo#5269

#<--------------Imports Start & Loading-------------->
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os

os.system("title Zolo - Loading...")
print(f"""
{Fore.MAGENTA}
                                  ╔═╗╔═╗╦  ╔═╗  ╔╦╗╔═╗╦╔═╔═╗╔╗╔  ╔═╗╦╔╗╔╔╦╗╔═╗╦═╗
                                  ╔═╝║ ║║  ║ ║   ║ ║ ║╠╩╗║╣ ║║║  ╠╣ ║║║║ ║║║╣ ╠╦╝
                                  ╚═╝╚═╝╩═╝╚═╝   ╩ ╚═╝╩ ╩╚═╝╝╚╝  ╚  ╩╝╚╝═╩╝╚═╝╩╚═


                                       {Fore.WHITE}          Loading...
""")
print(f"{Fore.MAGENTA}")
progressbar = tqdm([2,4,6,8,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')

import base64, pyperclip
#<--------------Imports End-------------->

os.system("title Tokyo - Ready")
os.system("cls")
print(f"""
{Fore.MAGENTA}
                                  ╔═╗╔═╗╦  ╔═╗  ╔╦╗╔═╗╦╔═╔═╗╔╗╔  ╔═╗╦╔╗╔╔╦╗╔═╗╦═╗
                                  ╔═╝║ ║║  ║ ║   ║ ║ ║╠╩╗║╣ ║║║  ╠╣ ║║║║ ║║║╣ ╠╦╝
                                  ╚═╝╚═╝╩═╝╚═╝   ╩ ╚═╝╩ ╩╚═╝╝╚╝  ╚  ╩╝╚╝═╩╝╚═╝╩╚═ 


                                    {Fore.WHITE}        Input the User ID




""")

id = input(Fore.MAGENTA+" " + Fore.WHITE+" " + Fore.MAGENTA+"@" + Fore.WHITE+"zolo#5069" + Fore.CYAN+" - " + Fore.WHITE+"enter targets ID: " + Fore.WHITE+" ")

try:
    check = int(id)
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Valid ID!')
    data = f'{id}'
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] {encodedStr}')
    print('')
    copy = input(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Do you want copy this text? (y/n){Fore.WHITE} ')

    if copy == "y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Text Copied!')

    if copy == "Y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Text Copied!')

    else:
        print('')
        print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Press enter to Exit')
        input()

except ValueError:
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Invalid ID!')
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Press enter to Exit')
    input()
