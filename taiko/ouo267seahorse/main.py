#ouo.269seahorse.me (太鼓ウェブ) 用のアカウントを登録できます

import requests
import random, string
import time
import concurrent.futures

countInput = int(input('アカウント作成数: '))
threadInput = int(input('スレッド数: '))

print(f'{countInput*threadInput}個作成します')

def sendRequest():
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]

    nameInput = ''.join(randlst)
    passwordInput = ''.join(randlst)

    token_cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': '4c290c6a-7f7c-4966-9c93-e2d80387d288',
    }

    token_headers = {
        'Accept': '*/*',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.1.76857572.1693120866; _ga_ME8M5G343E=GS1.1.1703738176.4.1.1703739428.0.0.0; session=4c290c6a-7f7c-4966-9c93-e2d80387d288',
        'Referer': 'https://ouo.269seahorse.me/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    token_response = requests.get('https://ouo.269seahorse.me/api/csrftoken', cookies=token_cookies, headers=token_headers)

    register_cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': '4c290c6a-7f7c-4966-9c93-e2d80387d288',
    }

    register_headers = {
        'Accept': '*/*',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.76857572.1693120866; _ga_ME8M5G343E=GS1.1.1703738176.4.1.1703739428.0.0.0; session=4c290c6a-7f7c-4966-9c93-e2d80387d288',
        'Origin': 'https://ouo.269seahorse.me',
        'Referer': 'https://ouo.269seahorse.me/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'X-CSRFToken': token_response.json()['token'],
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    register_json_data = {
        'username': nameInput,
        'password': passwordInput,
    }

    register_response = requests.post('https://ouo.269seahorse.me/api/register', cookies=register_cookies, headers=register_headers, json=register_json_data)

    if register_response.status_code==200:
        print(f'success {nameInput}:{passwordInput}')
        with open("saved-accounts.txt", "a") as f:
            f.write(f'{nameInput}:{passwordInput}\n')
    else:
        print('failed')

for i in range(countInput):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=threadInput)
    for i in range(threadInput):
        executor.submit(sendRequest)
    time.sleep(2)