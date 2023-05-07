# Author: Youtube.com/@wqnted420 / github.com/wqnted420 / wqnted#6255

import os
import shutil
import time
import ctypes

# """ Delete the files and folders inside the specified directories """

os.system('title Steamcleaner')
wqnted = """\u001B[31m
                wqnted420 on youtube:) 
 █     █░  █████   ███▄    █ ▄▄▄█████▓▓█████ ▓█████▄ 
▓█░ █ ░█░▒██▓  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌
▒█░ █ ░█ ▒██▒  ██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ░██   █▌
░█░ █ ░█ ░██  █▀ ░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌
░░██▒██▓ ░▒███▒█▄ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░▒████▓ 
░ ▓░▒ ▒  ░░ ▒▒░ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒ 
  ▒ ░ ░   ░ ▒░  ░ ░ ░░   ░ ▒░    ░     ░ ░  ░ ░ ▒  ▒ 
  ░   ░     ░   ░    ░   ░ ░   ░         ░    ░ ░  ░ 
    ░        ░             ░             ░  ░   ░    """


def cleaner():
    text = "[+] Loading.."
    loading_dots(text)
    os.system('cls')
    for dir_path in ["C:\\Program Files (x86)\\Steam\\userdata", "C:\\Program Files (x86)\\Steam\\appcache", "C:\\Program Files (x86)\\Steam\\config", "C:\\Program Files (x86)\\Steam\\logs", "C:\\Program Files (x86)\\Steam\\dumps", "C:\\Program Files (x86)\\Steam\\temp"]:
        try:
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                try:
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"[+] Deleted directory {file_path}")
                    else:
                        os.remove(file_path)
                        print(f"[+] Deleted file {file_path}")
                except PermissionError:
                    print(f"[!] Permission denied for {file_path}")
                    time.sleep(2)

        except FileNotFoundError:
            print(f"{dir_path} not found")
            time.sleep(2)

    # Delete registry keys
    try:
        os.system('cls')
        os.system(
            'reg delete "HKEY_CURRENT_USER\\SOFTWARE\\Facepunch Studios LTD\\Rust"')
        print(
            "[+] Deleted registry key HKEY_CURRENT_USER\\SOFTWARE\\Facepunch Studios LTD\\Rust")
    except:
        print("[-] Failed to delete registry key HKEY_CURRENT_USER\\SOFTWARE\\Facepunch Studios LTD\\Rust")
        time.sleep(2)

    try:
        os.system('cls')
        os.system('reg delete "HKEY_CURRENT_USER\\SOFTWARE\\Valve\\Steam\\Users"')
        print(
            "[+] Deleted registry key HKEY_CURRENT_USER\\SOFTWARE\\Valve\\Steam\\Users")
    except:
        print(
            "[-] Failed to delete registry key HKEY_CURRENT_USER\\SOFTWARE\\Valve\\Steam\\Users")
        time.sleep(2)

    # Delete files inside the depotcache directory
    try:
        text = "[+] Loading.."
        loading_dots(text)
        os.system('cls')
        dir_path = "C:\\Program Files (x86)\\Steam\\depotcache"
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            try:
                os.remove(file_path)
                print(f"Deleted file {file_path}")
            except PermissionError:
                print(f"Permission denied for {file_path}")
                time.sleep(2)
    except FileNotFoundError:
        print(f"{dir_path} not found")
        time.sleep(2)
        os.system('cls')

    # Delete Eos_seed.bin
    try:
        text = "[+] Loading.."
        loading_dots(text)
        os.system('cls')
        os.remove("C:\\Eos_seed.bin")
        print("[+] Deleted C:\\Eos_seed.bin")
        os.system('cls')
        exit()
    except FileNotFoundError:
        print("[-] C:\\Eos_seed.bin was not found")
        time.sleep(2)
        os.system('cls')
        exit()


def slowtype(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def loading_dots(text="Loading", delay=0.5, cycles=3):
    for i in range(cycles):
        print(f"\r{text}...", end="", flush=True)
        time.sleep(delay)
        print("\r" + " " * len(text) + "\r", end="", flush=True)


def main():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("This script requires administrator privileges. Please run it as an administrator.")
        time.sleep(5)
        os._exit(0)
    else:
        print(wqnted)
    text = "\u001B[37m[$] Steam cleaner made by wqnted#6255\n"
    slowtype(text)
    time.sleep(1)
    text = "[!] Press Enter to continue.."
    slowtype(text)
    input("")
    os.system('cls')
    text = "[!] \u001B[31mWARNING:\u001B[37m To continue, please log out of Steam and press Enter again."
    slowtype(text)
    input("")
    text = "[+] Please wait 7 seconds.."
    slowtype(text)
    time.sleep(7)
    os.system('taskkill /im steam.exe /f')
    os.system('cls')
    cleaner()


def exit():
    os.system('cls')
    print(wqnted)
    text = "\u001B[37m[+] Done."
    slowtype(text)
    text = "[+] Everything should be cleaned and you're ready to cheat again!"
    slowtype(text)
    text = "[!] Auto closing in 5 seconds."
    slowtype(text)
    time.sleep(3)


if __name__ == '__main__':
    main()
