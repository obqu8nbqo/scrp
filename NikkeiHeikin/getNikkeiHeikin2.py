import requests
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/markets/kabu/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

span = soup.find_all("span")

nikkei_heikin = ""

for tag in span:
    # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
    # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
    # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
    try:
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        if string_ in "mkc-stock_prices":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin = tag.string
            break
    except:
        # パス→何も処理を行わない
        pass

print(nikkei_heikin)