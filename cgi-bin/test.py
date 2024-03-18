#! /usr/bin/env python3
import datetime

print("Content-type: text/html")
print("")
print("<html>")
print(" <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print(" <body>")
print("    <h1>システムアーキテクトプログラミング演習</h1>")
print("    これはテストページです。")
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(" </body>")
print("</html>")