#! /usr/bin/env python3
import sys
import os
import urllib.parse
import io
import sqlite3
import csv

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
print(" <body bgcolor = \"#ffffe0\">")
print("<font size = \"6\">")
print("<p style=\"text-align:center;\">")
print("<b>\"")
print(param_str)
print("\"")
print("検索結果一覧")
print("</b> </p>")
print("</font>")
print(" </body>")
print("</html>")

db_path = "bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)	# データベースに接続
con.row_factory = sqlite3.Row	# 属性名で値を取り出せるようにする
cur = con.cursor()				# カーソルを取得

try:
	TITLE = param_str
	AUTUOR = param_str
	# SQL文の実行
	cur.execute("select * from BOOKLIST where (TITLE like ?) OR (AUTUOR like ?)", ('%' + TITLE + '%','%' + AUTUOR + '%',))
	rows = cur.fetchall()		# 検索結果をリストとして取得
	if not rows:
		print("<p style=\"text-align:center\">")			# リストが空のとき
		print("検索結果なし")
		print("</p>")
	else:
		print("<table border=\"1\" width = \"1000\" align = \"center\">")
		print("<tr bgcolor = \"#87cefa\">")
		print("<th>ID</th> <th>タイトル</th> <th>著者</th> <th>出版社</th> <th>価格</th> <th>IBSN</th>")
		print("</tr>")
		for row in rows:		# 検索結果を1つずつ処理
			print("<tr bgcolor = \"#f0f8ff\">")
			print("<td>%s</td>" % str(row['ID']))
			print("<td>%s</td>" % str(row['TITLE']))
			print("<td>%s</td>" % str(row['AUTUOR']))
			print("<td>%s</td>" % str(row['PUBLISHER']))
			print("<td>%s</td>" % str(row['PRICE']))
			print("<td>%s</td>" % str(row['ISBN']))
			print("</tr>")
		print("</table>")
		
except sqlite3.Error as e:		# エラー処理
	print("Error occurred:", e.args[0])

con.commit()
con.close()