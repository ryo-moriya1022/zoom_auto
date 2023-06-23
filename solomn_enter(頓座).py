import requests as rq
from bs4 import BeautifulSoup
url="https://solomon.mc.chitose.ac.jp/ael/Index;jsessionid=DD09301DAE3026319EEF043C1D7338BE?0"
login_url="https://solomon.mc.chitose.ac.jp/wbt/Index?0"
username="b2222380"
password="EVA1022moriya"
response_0=rq.get(url)
soup_login=BeautifulSoup(response_0.text) 
session=rq.Session()
response_1=session.post(url=login_url,
data=
{
    "j_username":username,"j_password":password
})
soup = BeautifulSoup(response_1.text, "html.parser")
text = soup.get_text()

print(response_1.text)
