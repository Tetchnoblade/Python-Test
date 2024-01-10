#nyanpass.comのにゃんぱすーボタンを指定した回数クリックします

import requests

count = int(input('クリック回数: '))

def press():
    headers = {
        'authority': 'nyanpass.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://nyanpass.com',
        'referer': 'https://nyanpass.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'nyan': 'pass',
    }

    response = requests.post('https://nyanpass.com/add.php', headers=headers, data=data)

    if response.status_code==200:
        return response.json()['cnt']
    else:
        return False

counter = 1

for i in range(count):
    process = press()

    if process:
        print('='*10)
        print(f'クリックに成功しました ({counter}回目)')
        print(process)
        print('='*10)
        counter += 1
    elif not process:
        print(f'クリックに失敗しました ({counter}回目)')