#!/usr/bin/env python3

import requests

URL = "http://localhost/login.php"

PASSWORD_WORDLIST = "./password_wordlist.txt"
USERNAME_WORDLIST = "./username_wordlist.txt"

def check():
    r1 = requests.get(URL)
    print(r1)
    
    


if __name__ == "__main__":
    
    usernames = open(USERNAME_WORDLIST, "r").read().splitlines()
    passwords = open(PASSWORD_WORDLIST, "r").read().splitlines()

    for user in usernames:
        for password in passwords:
            pass
        

check()
