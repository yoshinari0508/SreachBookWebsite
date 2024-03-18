#! /usr/bin/env python3
import sys
import os
import urllib.parse
import io



form = {} # 辞書を初期化
content_length = os.environ.get('CONTENT_LENGTH') # 入力データ長を取得
if content_length: # 入力データがある場合
  body = sys.stdin.read(int(content_length)) # 入力データを標準入力から読み込み
  params = body.split('&') # 入力データを & で分割
  for param in params: # 分割されたデータを順に処理
    key, value = param.split('=') # 分割データを = で分割
    form[key] = urllib.parse.unquote(value) # キーと値を辞書に登録（値はURLデコードする）
  
param_str = form['param1'] # ブラウザから送信されたparam1の値を辞書から取得

print(param_str)

print("Content-type: text/html")
print("")
print("<html>")
print(" <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print(" <body>")
print("入力された文字は「")
print(param_str)
print("」です。")
print(" </body>")
print("</html>")