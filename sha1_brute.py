#!/usr/bin/env python3

import hashlib
import sys

print("""\n\n
 __  __ ____  ____    _   _    _    ____  _   _ 
|  \/  |  _ \| ___|  | | | |  / \  / ___|| | | |
| |\/| | | | |___ \  | |_| | / _ \ \___ \| |_| |
| |  | | |_| |___) | |  _  |/ ___ \ ___) |  _  |
|_|  |_|____/|____/  |_| |_/_/   \_\____/|_| |_|
                                                
  ____ _   _ _____ ____ _  _______ ____  
 / ___| | | | ____/ ___| |/ / ____|  _ \ 
| |   | |_| |  _|| |   | ' /|  _| | |_) |
| |___|  _  | |__| |___| . \| |___|  _ < 
 \____|_| |_|_____\____|_|\_\_____|_| \_\
\n\n
""")



def usage():
    print ("Usage: python3 hash_checker.py <md5-hash> <wordlist>")

def calculate_hash(word):
    l = len(word)
    w = word[0:l-1]
    h = hashlib.sha1(w.encode()).hexdigest()
    return h

if len(sys.argv) != 3:
    usage()
    sys.exit(1)

current_hash = sys.argv[1]
name_of_file = sys.argv[2]
count = 0
try:
    f = open(name_of_file, 'r')

    for word in f:
        print (f"[!] Trying word: {word}", end="")
        md5hash = calculate_hash(word)
        if md5hash == current_hash:
            print(f'[+] Found hash: {current_hash} : {word}')
            print("[!] Do you wish to continue?(y/n)")
            check = str(input(''))
            if not (check == "y"):
                print("See ya! ;)")
                break

    f.close()
except FileNotFoundError:
    print("[-] File not found")
except KeyboardInterrupt:
    print("See ya! ;)")
