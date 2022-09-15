import platform
import time
from requests import get
import socket
import platform
from getpass import getuser
import subprocess
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from colorama import Fore , init
init()

print("\n\n\n\n\n\n\n\n")
time.sleep(2)
print(Fore.YELLOW+"""

        ░██████╗██████╗░██╗░░░██╗
        ██╔════╝██╔══██╗╚██╗░██╔╝
        ╚█████╗░██████╔╝░╚████╔╝░
        ░╚═══██╗██╔═══╝░░░╚██╔╝░░
        ██████╔╝██║░░░░░░░░██║░░░
        ╚═════╝░╚═╝░░░░░░░░╚═╝░░░
                                        ▄▄▄▄▄            ▄▄▌  .▄▄ · 
                                        •██   ▄█▀▄  ▄█▀▄ ██•  ▐█ ▀. 
                                         ▐█.▪▐█▌.▐▌▐█▌.▐▌██▪  ▄▀▀▀█▄
                                         ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
                                         ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ 
""")
print(Fore.RED + "")
time.sleep(1)
print("""
                                ___          
                               (  _ \        
                               | (_) ) _   _ 
                               |  _ ( ( ) ( )
                               | (_) )| (_) |
                               (____/  \__  |
                                      ( )_| |
                                       \___/ 
""")
print(Fore.LIGHTGREEN_EX+"")
time.sleep(2)
print("""

                        ███╗░░░███╗░█████╗░███╗░░░███╗░█████╗░██████╗░░██████╗░░█████╗░███╗░░░███╗███████╗██████╗░░░███╗░░
                        ████╗░████║██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░████║██╔════╝██╔══██╗░████║░░
                        ██╔████╔██║███████║██╔████╔██║███████║██║░░██║██║░░██╗░███████║██╔████╔██║█████╗░░██████╔╝██╔██║░░
                        ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██║██║░░██║██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░██╔══██╗╚═╝██║░░
                        ██║░╚═╝░██║██║░░██║██║░╚═╝░██║██║░░██║██████╔╝╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██║░░██║███████╗
                        ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
""")
print(Fore.RED+"Welcome To Spy-Tools :D\n This Program Made By: mamadgamer1 BBG MG1")
print(Fore.LIGHTBLUE_EX+"")
frn = print("[1] Spy Friends ")
time.sleep(1)
print(Fore.LIGHTBLACK_EX+"")
phn = print("[2] Spy Phones ")
time.sleep(1)
print(Fore.GREEN+"")
symip = print("[3] System Ip")
time.sleep(1)
print(Fore.LIGHTYELLOW_EX+"")
whs = print("[4] Who Is ")
time.sleep(1)
print(Fore.RED+"")
oths = print("[5] Other Tools . . . ")
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX+"")
dvlp = print("[6] Developer/info \n ")
time.sleep(1)
egst = print("[7] Exit ")

print(Fore.CYAN+"")
chs = int(input("Select---> "))

if chs ==1:
    print(Fore.MAGENTA+"")
    print("Spy Friends Has Been Picked!\n")
    print(Fore.RED + "")
    username = input("\nEnter Target UserName: ")
    sites = ["http://github.com","http://instagram.com","https://www.dalfak.com","https://www.namasha.com","https://www.discord.com","http://aparat.com","https://www.youtube.com/c","https://www.facebook.com"]
    for site in sites:
            url = site + "/{}".format(username)
            response = get(url)
            if response.status_code == 200:
                    print(Fore.GREEN+"[+] {} Target Found In {}".format(username,site))
            elif response.status_code == 404:
                    print(Fore.RED+"[-] {} Target Not Found In {}".format(username,site))
                    print(Fore.RED + "")

elif chs ==2:
    print(Fore.LIGHTRED_EX+"")
    print("Spy Phones Has Been Picked!\n")
    print(Fore.GREEN + "\tThis Program Made By:\n\tmamadgamer1 BBG MG1")
    cntn = input("Press Enter To Continue: ")
    print(Fore.GREEN + """
    
    
                ██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗
                ██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝
                ██████╔╝███████║██║░░██║██╔██╗██║█████╗░░
                ██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░
                ██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗
                ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝
    
    """)
    print("example: +1234567890")
    Target = input("Enter ur target phone number with + : ")
    print("Please Wait . . .")
    time.sleep(1)
    print(Fore.BLACK + "\tResult: ")
    number = parse(Target)
    print(Fore.RED + geocoder.description_for_number(number,"en"))
    print(carrier.name_for_number(number,"en"))

    print(Fore.BLUE + "The Country of phone is: " +geocoder.description_for_number(number,"en"))
    print("The Operator of phone is: " +carrier.name_for_number(number,"en"))
    print(Fore.CYAN+"")

    exit = input("Press Enter To exit: ")

elif chs ==3:
    print("System Ip Has Been Picked!\n")
    print(Fore.YELLOW +"")
    print("""
    
    
            ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
            ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
            ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
            ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
            ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
            ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝
    """)
    print("Please Wait While We Are Getting Your System Info . . .")
    time.sleep(3)
    nm = platform.uname()[0]
    nm2 = platform.uname()[4]
    nm3=socket.gethostname()
    nm4=getuser()
    nm5=platform.uname()[1]
    SysIp=socket.gethostbyname(nm3)
    print(Fore.RED+f"Your System Is: {nm}")
    print(f"Your System Name Is: {nm5}")
    print(f"Your System Machine Is: {nm2}")
    print(f"Your System Name Is: {nm4}")
    print(f"Your System Ip is: {SysIp}")

elif chs ==4:
    print("Who Is Has Been Picked!\n")
    print(Fore.LIGHTGREEN_EX+"")
    print("""
    
    
            ░██╗░░░░░░░██╗██╗░░██╗░█████╗░ ██╗░██████╗
            ░██║░░██╗░░██║██║░░██║██╔══██╗ ██║██╔════╝
            ░╚██╗████╗██╔╝███████║██║░░██║ ██║╚█████╗░
            ░░████╔═████║░██╔══██║██║░░██║ ██║░╚═══██╗
            ░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝ ██║██████╔╝
            ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░ ╚═╝╚═════╝░
    
    
    """)
    print(Fore.GREEN+"")
    Target = input("\n \t       Enter Your Target Website: ")
    Target = Target.replace("http://","")
    Target = Target.replace("https://","")
    Target = Target.replace("www.","")
    if Target[-3:] == "org" or Target[-3:] == "com" or Target[-3:] == "net" or Target[-3:]=="ir" or Target[-3:]=="in" or Target[-3:]=="is" or Target[-3:]=="co" or Target[-3:]=="tor" or Target[-3:]=="en" or Target[-3:]=="Us" or Target[-3:]=="onion" or Target[-3:]=="ru" or Target[-3:]=="cz":
        whois_server = "whois.internic.net"
    else:
        whois_server =  "whois.iana.org"
    print(Fore.WHITE+"")
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((whois_server,43))
    s.send((Target+"\r\n").encode())
    msg = s.recv(10000)
    print(msg.decode())
    print(Fore.CYAN+"")
    ex = input("\n\tPress Enter To Exit: ")
    print("\t Exiting . . .")
    time.sleep(1)
    while True:
           break

elif chs ==5:
    print("Page 2:\n")
    print(Fore.LIGHTBLUE_EX+"")
    print("""
    [1] Cmd shell
    [2] Exit
    """)
    print(Fore.MAGENTA+"")
    chos = int(input("Select--> "))
    if chos ==1:
        print(Fore.GREEN+"")
        print("Welcome To The CMD(aka command prompt) Shell\nPlease Note That This Shell Does Not Work At All!")
        while True:
            cmdshell = input("\n CMD---> ")
            m = subprocess.check_output(cmdshell , shell=True)
    if chos ==2:
        print(Fore.RED+"")
        print("Bye :D")
        while True:
            break

elif chs ==6:
    print(Fore.RED+"")
    print("""
    Program By:
    
     / \---------------------------, 
    \_,|                          | 
    |    mamadgamer1 BBG MG1      | 
    |  ,-------------------------
    \_/________________________/ 
    
    \nThis Tools Made By mamadgamer1 BBG MG1
    All responsibility for improper use of this program is on the person himself!\n We do not accept any responsibility\n Thanks You!
    """)

elif chs ==7:
    print(Fore.CYAN+"")
    print("Thanks For Using Our Program :D")
    while True:
        break
