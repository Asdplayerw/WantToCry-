import time
import os
import subprocess
import webbrowser

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"
BLACK_BG = "\033[40m"

required_modules = [
    "pystyle",
    "urllib3",
    "phonenumbers",
    "colorama",
    "python-whois",
    "requests",
    "bs4",
    "faker"
]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Для переноса строки после завершения


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def check_and_install_modules():
    print_with_delay(
        GREEN_TEXT + "Вас приветствует Mactep установки Want To Cry.\nСейчас мы проведем установку всех зависимостей для правильной работы программы Want To Cry.\nУстановка не займет более 3-х минут.\n3\n2\n1\n" + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module} уже установлен.")
        except ImportError:
            print(f"Установка {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f"Установлен модуль {module}" + RESET)

    print_with_delay(GREEN_TEXT + "Запускаем программу Want To Cry..." + RESET)
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')






import platform
import os
import sys
import socket
import pystyle
import requests
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
import requests
import whois
import random
import colorama
import threading
import string
import faker
import bs4
import urllib.parse
import colorama
import concurrent.futures
import csv
from pystyle import Colorate, Colors
import hashlib
import uuid

if platform.system() == "Windows":
    import ctypes
    GWL_STYLE = -16
    WS_SIZEBOX = 262144
    WS_MAXIMIZEBOX = 65536
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
    style = style & ~WS_SIZEBOX
    style = style & ~WS_MAXIMIZEBOX
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
    enter = pystyle.Colorate.Horizontal(pystyle.Colors.green_to_cyan, ('Welcome To Want To Cry, Press "ENTER" to continue!'))
    pystyle.Anime.Fade(
    pystyle.Center.Center('''




                                    ___         ___                                                  
                                   (   )       (   )                                                 
 ___  ___  ___   .---.   ___ .-.    | |_        | |_       .--.       .--.     ___ .-.     ___  ___  
(   )(   )(   ) / .-, \ (   )   \  (   __)     (   __)    /    \     /    \   (   )   \   (   )(   ) 
 | |  | |  | | (__) ; |  |  .-. .   | |         | |      |  .-. ;   |  .-. ;   | ' .-. ;   | |  | |  
 | |  | |  | |   .'`  |  | |  | |   | | ___     | | ___  | |  | |   |  |(___)  |  / (___)  | |  | |  
 | |  | |  | |  / .'| |  | |  | |   | |(   )    | |(   ) | |  | |   |  |       | |         | '  | |  
 | |  | |  | | | /  | |  | |  | |   | | | |     | | | |  | |  | |   |  | ___   | |         '  `-' |  
 | |  ; '  | | ; |  ; |  | |  | |   | ' | |     | ' | |  | '  | |   |  '(   )  | |          `.__. |  
 ' `-'   `-' ' ' `-'  |  | |  | |   ' `-' ;     ' `-' ;  '  `-' /   '  `-' |   | |          ___ | |  
  '.__.'.__.'  `.__.'_. (___)(___)   `.__.       `.__.    `.__.'     `.__,'   (___)        (   )' |  
                                                                                            ; `-' '  
                                                                                             
    
                                        Press To Enter
                                          
                                          
                                          '''), pystyle.Colors.red_to_purple, pystyle.Colorate.Vertical, enter=True)

def popup():
    url = "https://t.me/Ilya_Reidov"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")

def Main():
    if platform.system() == "Windows":
        os.system("cls")
        check_and_install_modules()
        popup()
        os.system("cls")
        pystyle.Write.Print(pystyle.Center.XCenter('''
                                                      

⠀⠀⠀
                                    ___         ___                                                  
                                   (   )       (   )                                                 
 ___  ___  ___   .---.   ___ .-.    | |_        | |_       .--.       .--.     ___ .-.     ___  ___  
(   )(   )(   ) / .-, \ (   )   \  (   __)     (   __)    /    \     /    \   (   )   \   (   )(   ) 
 | |  | |  | | (__) ; |  |  .-. .   | |         | |      |  .-. ;   |  .-. ;   | ' .-. ;   | |  | |  
 | |  | |  | |   .'`  |  | |  | |   | | ___     | | ___  | |  | |   |  |(___)  |  / (___)  | |  | |  
 | |  | |  | |  / .'| |  | |  | |   | |(   )    | |(   ) | |  | |   |  |       | |         | '  | |  
 | |  | |  | | | /  | |  | |  | |   | | | |     | | | |  | |  | |   |  | ___   | |         '  `-' |  
 | |  ; '  | | ; |  ; |  | |  | |   | ' | |     | ' | |  | '  | |   |  '(   )  | |          `.__. |  
 ' `-'   `-' ' ' `-'  |  | |  | |   ' `-' ;     ' `-' ;  '  `-' /   '  `-' |   | |          ___ | |  
  '.__.'.__.'  `.__.'_. (___)(___)   `.__.       `.__.    `.__.'     `.__,'   (___)        (   )' |  
                                                                                            ;                                                               
                                                              \n'''), pystyle.Colors.red_to_purple, interval = 0.000001)
    else:
        os.system("clear")
        check_and_install_modules()
        popup()
        os.system("clear")
        pystyle.Write.Print(pystyle.Center.XCenter('''                                                                   
                               
             

                                                                                                                                    


██╗    ██╗ █████╗ ███╗   ██╗████████╗    ████████╗ ██████╗      ██████╗██████╗ ██╗   ██╗
██║    ██║██╔══██╗████╗  ██║╚══██╔══╝    ╚══██╔══╝██╔═══██╗    ██╔════╝██╔══██╗╚██╗ ██╔╝
██║ █╗ ██║███████║██╔██╗ ██║   ██║          ██║   ██║   ██║    ██║     ██████╔╝ ╚████╔╝ 
██║███╗██║██╔══██║██║╚██╗██║   ██║          ██║   ██║   ██║    ██║     ██╔══██╗  ╚██╔╝  
╚███╔███╔╝██║  ██║██║ ╚████║   ██║          ██║   ╚██████╔╝    ╚██████╗██║  ██║   ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝          ╚═╝    ╚═════╝      ╚═════╝╚═╝  ╚═╝   ╚═╝ 
                                                                                        

                
                                                     \n'''), pystyle.Colors.red_to_purple, interval = 0.00001)                                  
    pystyle.Write.Print(pystyle.Center.XCenter('''\n

   ┌──────────────────────────────────────────────────────────────────────────────────┐
      • 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 -  @𝙸𝚕𝚢𝚊_𝚁𝚎𝚒𝚍𝚘𝚟     • 𝚅𝚎𝚛𝚜𝚒𝚘𝚗 - 𝟷.𝟶.2    • Хочу Плакать             
   └──────────────────────────────────────────────────────────────────────────────────┘

                        ┌────────────────────────────────────┐                                  
                        │ [1] • 𝚂𝚎𝚊𝚛𝚌𝚑 𝙽𝚞𝚖𝚋𝚎𝚛                │
                        │ [2] • 𝚂𝚎𝚊𝚛𝚌𝚑 𝚂𝚒𝚝𝚎                  │
                        │ [3] • 𝚂𝚎𝚊𝚛𝚌𝚑 𝙽𝚒𝚌𝚔𝙽𝚊𝚖𝚎              │
                        │ [4] • 𝚂𝚎𝚊𝚛𝚌𝚑 𝙸𝙿                    │          
                        │ [5] • 𝚂𝚎𝚊𝚛𝚌𝚑 𝙳𝚊𝚝𝚊𝙱𝚊𝚜𝚎              │
                        │ [6] • 𝚂𝚎𝚊𝚛𝚌𝚑 𝙼𝚊𝚌-𝙰𝚍𝚛𝚎𝚜𝚜            │
                        │ [7] • 𝙱𝚘𝚖𝚋𝚎𝚛                       │
                        │ [8] • 𝚂𝚗𝚘𝚜𝚎𝚛                       │
                        │ [9] • 𝙳𝚘𝚡-𝚃𝚎𝚖𝚙𝚕𝚊𝚝𝚎                 │
                        │ [10] • 𝙼𝚊𝚗𝚞𝚊𝚕𝚜                     │
                        │ [11] • 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛                   │
                        │ [12] • 𝙲𝚛𝚎𝚊𝚝𝚎 𝙴𝚖𝚊𝚒𝚕                │  
                        └────────────────────────────────────┘
                                         
'''), pystyle.Colors.red_to_purple, interval = 0.00000001)
Main()
while True:
    choice = pystyle.Write.Input("\n\n[?] • 𝚂𝚎𝚕𝚎𝚌𝚝 𝙼𝚎𝚗𝚞 𝙸𝚝𝚎𝚖 -> ", pystyle.Colors.red_to_purple, interval = 0.001)
    if choice == "1":
        phone = pystyle.Write.Input("\n[?] • 𝙴𝚗𝚝𝚎𝚛 𝚃𝚑𝚎 𝙽𝚞𝚖𝚋𝚎𝚛 -> ", pystyle.Colors.red_to_purple, interval = 0.005)
        def phoneinfo(phone):
            try:
                parsed_phone = phonenumbers.parse(phone, None)
                if not phonenumbers.is_valid_number(parsed_phone):
                    return pystyle.Write.Print(f"\n[!] 𝙰𝚗 𝙴𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚛𝚎𝚍 -> 𝙸𝚗𝚟𝚊𝚕𝚒𝚍 𝙿𝚑𝚘𝚗𝚎 𝙽𝚞𝚖𝚋𝚎𝚛\n", pystyle.Colors.red_to_red, interval=0.005)
                carrier_info = phonenumbers.carrier.name_for_number(parsed_phone, "en")
                country = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
                region = phonenumbers.geocoder.description_for_number(parsed_phone, "ru")
                formatted_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                is_valid = phonenumbers.is_valid_number(parsed_phone)
                is_possible = phonenumbers.is_possible_number(parsed_phone)
                timezona = phonenumbers.timezone.time_zones_for_number(parsed_phone)
                print_phone_info = f"""\n[+] • 𝙿𝚑𝚘𝚗𝚎 𝙽𝚞𝚖𝚋𝚎𝚛  -> {formatted_number}
[+] Страна -> {country}
[+] Регион -> {region}
[+] Оператор -> {carrier_info}
[+] Активен -> {is_possible}
[+] Валид -> {is_valid}
[+] Таймзона -> {timezona}
[+] Telegram -> https://t.me/{phone}
[+] Whatsapp -> https://wa.me/{phone}
[+] Viber -> https://viber.click/{phone}\n"""
                pystyle.Write.Print(print_phone_info, pystyle.Colors.red_to_purple, interval=0.005)
            except Exception as e:
                pystyle.Write.Print(f"\n[!] 𝙰𝚗 𝙴𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚛𝚎𝚍 -> {str(e)}\n", pystyle.Colors.red_to_purple, interval=0.005)
        phoneinfo(phone)
    if choice == "2":
        domain = pystyle.Write.Input("\n[?] • 𝙴𝚗𝚝𝚎𝚛 𝚃𝚑𝚎 𝚂𝚒𝚝𝚎 -> ", pystyle.Colors.red_to_purple, interval = 0.005)
        def get_website_info(domain):
            domain_info = whois.whois(domain)
            print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] Зарегистрирован: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
"""
            pystyle.Write.Print(print_string, pystyle.Colors.red_to_purple, interval=0.005)
        get_website_info(domain)
    if choice == "3":
        nick = pystyle.Write.Input(f"\n[?] • 𝙴𝚗𝚝𝚎𝚛 𝚃𝚑𝚎 𝙽𝚒𝚌𝚔𝙽𝚊𝚖𝚎 -> ", pystyle.Colors.red_to_purple, interval=0.005)
        urls = [
            f"https://www.instagram.com/{nick}",
            f"https://www.tiktok.com/@{nick}",
            f"https://twitter.com/{nick}",
            f"https://www.facebook.com/{nick}",
            f"https://www.youtube.com/@{nick}",
            f"https://t.me/{nick}",
            f"https://www.roblox.com/user.aspx?username={nick}",
            f"https://www.twitch.tv/{nick}",
        ]
        for url in urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    pystyle.Write.Print(f"\n{url} - • 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙽𝚘𝚏 𝙵𝚘𝚞𝚗𝚍", pystyle.Colors.red_to_purple, interval=0.005)
                elif response.status_code == 404:
                    pystyle.Write.Print(f"\n{url} - • 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙽𝚘𝚏 𝙵𝚘𝚞𝚗𝚍", pystyle.Colors.red_to_purple, interval=0.005)
                else:
                    pystyle.Write.Print(f"\n{url} - 𝙴𝚛𝚛𝚘𝚛 {response.status_code}", pystyle.Colors.red_to_purple, interval=0.005)
            except:
                pystyle.Write.Print(f"\n{url} - 𝙴𝚛𝚛𝚘𝚛 𝚆𝚑𝚒𝚕𝚎 𝙲𝚑𝚎𝚌𝚔𝚒𝚗𝚐", pystyle.Colors.red_to_purple, interval=0.005)
        print()
    if choice == "4":
        ip = pystyle.Write.Input("\n[?] • 𝙴𝚗𝚝𝚎𝚛 𝙸𝙿 𝙰𝚍𝚛𝚎𝚜𝚜 -> ", pystyle.Colors.red_to_purple, interval = 0.005)
        def ip_lookup(ip):
            url = f"http://ip-api.com/json/{ip}"
            try:
                response = requests.get(url)
                data = response.json()
                if data.get("status") == "fail":
                    pystyle.Write.Print(f"[!] 𝙰𝚗 𝙴𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚛𝚎𝚍: {data['message']}\n", pystyle.Colors.red_to_purple, interval=0.005)
                info = ""
                for key, value in data.items():
                    info += f"[+] {key}: {value}\n"
                return info
            except Exception as e:
                pystyle.Write.Print(f"[!] 𝙰𝚗 𝙴𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚛𝚎𝚍: {str(e)}\n", pystyle.Colors.red_to_purple, interval=0.005)
        print()
        pystyle.Write.Print(ip_lookup(ip), pystyle.Colors.blue_to_cyan, interval=0.005)
    if choice == "5":
        path = pystyle.Write.Input("\n[?] 𝙴𝚗𝚝𝚎𝚛 𝙿𝚊𝚝𝚑 𝚃𝚘 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 𝙵𝚘𝚕𝚍𝚎𝚛: ", pystyle.Colors.red_to_purple, interval=0.005)
        search_text = pystyle.Write.Input("\n[?] 𝙴𝚗𝚝𝚎𝚛 𝚃𝚑𝚎 𝚃𝚎𝚡𝚝:  ", pystyle.Colors.red_to_purple, interval=0.005)
        print()
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if search_text in line:
                        pystyle.Write.Print("[+] • 𝚁𝚎𝚜𝚞𝚕𝚝: " + line.strip(), pystyle.Colors.red_to_purple, interval=0.005)
                        print()
                        break
                else:
                    pystyle.Write.Print("[!] • 𝚃𝚎𝚡𝚝 𝙽𝚘 𝙵𝚘𝚞𝚗𝚍.\n", pystyle.Colors.red_to_purple, interval=0.005)
        except:
            try:
                with open(path, "r", encoding="cp1251") as f:
                    for line in f:
                        if search_text in line:
                            pystyle.Write.Print("[+] • 𝚁𝚎𝚜𝚞𝚕𝚝: " + line.strip(), pystyle.Colors.red_to_purple, interval=0.005)
                            print()
                            break
                    else:
                        pystyle.Write.Print("[!] • 𝚃𝚎𝚡𝚝 𝙽𝚘 𝙵𝚘𝚞𝚗𝚍.\n", pystyle.Colors.red_to_purple, interval=0.005)
            except:
                try:
                    with open(path, "r", encoding="cp1252") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print("[+] • 𝚁𝚎𝚜𝚞𝚕𝚝: " + line.strip(), pystyle.Colors.red_to_purple, interval=0.005)
                                print()
                                break
                        else:
                            pystyle.Write.Print("[!] • 𝚃𝚎𝚡𝚝 𝙽𝚘 𝙵𝚘𝚞𝚗𝚍.\n", pystyle.Colors.red_to_purple, interval=0.005)
                except:
                    pystyle.Write.Print(f"[!] • 𝙴𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚛𝚎𝚍 𝙲𝚑𝚎𝚌𝚔 𝙳𝚊𝚝𝚊 𝙸𝚗𝚙𝚞𝚝\n", pystyle.Colors.red_to_purple, interval=0.005)

    if choice == "6":
      os.system("python mac.py")  # Замените 'file1.py' на имя вашего файла

    if choice == "7":
      os.system("python bomber.py")  # Замените 'file1.py' на имя вашего файла
    
    if choice == "8":
      os.system("python hloridat.py") 
    
    if choice == "9":
      os.system("python dox_template.py")
    
    if choice == "10":
      os.system("python main.py") 
    
    if choice == "11":
      os.system("python generator.py")
  
    if choice == "12":
      os.system("python genmail.py")
       
        