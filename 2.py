#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup



URL = "http://localhost/login.php"

PASSWORD_WORDLIST = "./password_wordlist.txt"
USERNAME_WORDLIST = "./username_wordlist.txt"

def check():
    r1 = requests.get(URL)
    headers = r1.headers
    cookie = headers["Set-Cookie"]
    print(cookie)
    soup = BeautifulSoup(r1.text, 'html.parser')
    token = soup.find("input", {"name": "user_token"})["value"]
    


if __name__ == "__main__":
    
    usernames = open(USERNAME_WORDLIST, "r").read().splitlines()
    passwords = open(PASSWORD_WORDLIST, "r").read().splitlines()

    for user in usernames:
        for password in passwords:
            pass
        

check()
