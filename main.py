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
This script created by Aryan
Contact us: T.me/Ikvenom
Professional WhatsApp Banning tools
{Fore.CYAN}
*************************************************
   {Fore.WHITE} ''')
banner_display()
#
#
def program():
    number = input("[+] Put Number with country code like +91: +")
    realnumber = "+"+number
    check = number.isnumeric()
    lennber = len(number)
    if (check == True):
        if (lennber < 10 or lennber > 10):
            delay_print(f"{Fore.RED}Number must be 10 digits\n")
            program()
        elif (lennber==10):
            delay_print(f"{Fore.YELLOW}1) Ban number\n")
            delay_print(f"{Fore.YELLOW}2) Information about this number\n")
            option = input(f"{Fore.YELLOW}[+] Choose an option: ")
            if (option=="1"):
                delay_print(f"{Fore.YELLOW}Are you sure to ban "+realnumber+"?\n")
                yesorno1 = input("(Y/N): ")
                delay_print("8579 reports Have been send and "+realnumber+" will be banned in less than 8 hours!")
                data.lockout()

            elif (option=="2"):
                delay_print(f"{Fore.YELLOW}Gather information for "+realnumber+"?\n")
                yesorno2 = input("(Y/N): ")
                delay_print("Name: 47hxl-53r\nStatus: Take-Down by VeNoM!")
                data.lockout()

            else:
                delay_print(f"{Fore.RED}It's not an option\n")
                program()


    else:
        delay_print(f"{Fore.RED}Number is incorrect... Please try again . . .\n")
        print("")
        program()
program()
