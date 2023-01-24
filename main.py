import network, urequests
import time
#from urllib.parse import urlencode
import sl
login="admin","Elteam2019","20.0.0.41"

response = sl.getvalue(login,'5/0/25')
print(response)
print("testvalue")
time.sleep(1)
