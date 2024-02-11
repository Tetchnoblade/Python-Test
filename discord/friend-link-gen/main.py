#discord.com用のフレンド追加URLを生成します

import requests
import time

tokenInput = str(input('トークンを入力してください: '))

headers = {
    "authorization": tokenInput,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
}

response = requests.post("https://discord.com/api/v9/users/@me/invites", headers=headers)

if response.status_code==200:
    print('フレンド追加リンクの生成に成功しました')
    print(f"https://discord.gg/{response.json()['code']}")
else:
    print('エラーが発生しました')

print('五秒後にウィンドウが削除されます')
time.sleep(5)