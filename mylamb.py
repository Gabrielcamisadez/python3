#                       CREATIVITY ?
import os

ADM = "admin"
ADM_PASSWORD = "admin123"

while True in range(2):
    l = input("Login name: ")
    p = input("Password: ")

    if l != ADM and p != ADM_PASSWORD:
        print(f'\n\tError:\n\tTest:\n\tHell:\n')
    elif l == ADM and p == ADM_PASSWORD :
        os.system("ping -c 3 google.com")
        break
    