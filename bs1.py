import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第1引数にhtml1文字列、第2引数にパーサーを指定する。今回は追加ライブラリ不要な'html.parser'を指定
soup=BeautifulSoup(res.text,'html.parser')

#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
print(soup)
