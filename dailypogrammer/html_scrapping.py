from bs4 import BeautifulSoup
import requests
import re

base_url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")
print(all_p_cn_text_body)
for elem in all_p_cn_text_body[7:]:
  print(elem.text)
