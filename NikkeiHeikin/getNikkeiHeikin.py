import requests
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.nikkei.com/"

# 取得
r = requests.get(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(r.content, "html.parser")

# タイトル要素を取得
title_tag = soup.title

# 要素の文字列を取得
title = title_tag.string

print(title_tag)

print(title)