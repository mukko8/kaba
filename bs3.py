import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第1引数にhtml1文字列、第2引数にパーサーを指定する。今回は追加ライブラリ不要な'html.parser'を指定
soup=BeautifulSoup(res.text,'html.parser')

#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
#print(soup)

#タグで要素取得
ele=soup.find('title') #<title>コビトカバ</title>
#要素のtextコンテントを表示
print(ele.text) #コビトカバ

#要素を結果セット(ResultSet)として取得
imgs=soup.find_all('img')
for img in imgs:
    #属性にアクセスするにはgetメソッドを使う
    print(img.get('src'))
