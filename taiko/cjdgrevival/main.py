#cjdgrevival.com (太鼓ウェブ) 用のアカウントを登録できます

import requests
import random, string
import time
import concurrent.futures

countInput = int(input('アカウント作成数 x20: '))

print(f'{countInput*20}個作成します')

def sendRequest():
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]

    nameInput = ''.join(randlst)
    passwordInput = ''.join(randlst)

    token_cookies = {
        'session': 'b13e4c3d-27a2-4c47-ae1f-a430857cf389',
        'cf_clearance': '0cfo1hkpS_15Jj7aHYOWP2DsVJxtfdYq7xXsEqgCj_I-1704790958-0-2-b68b5ed1.ea6ca617.f914c988-0.2.1704790958',
    }

    token_headers = {
        'authority': 'cjdgrevival.com',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'referer': 'https://cjdgrevival.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    token_response = requests.get('https://cjdgrevival.com/api/csrftoken', cookies=token_cookies, headers=token_headers)

    register_cookies = {
        'session': 'b13e4c3d-27a2-4c47-ae1f-a430857cf389',
        'cf_clearance': '0cfo1hkpS_15Jj7aHYOWP2DsVJxtfdYq7xXsEqgCj_I-1704790958-0-2-b68b5ed1.ea6ca617.f914c988-0.2.1704790958',
    }

    register_headers = {
        'authority': 'cjdgrevival.com',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://cjdgrevival.com',
        'referer': 'https://cjdgrevival.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-csrftoken': token_response.json()['token'],
    }

    register_json_data = {
        'username': nameInput,
        'password': passwordInput,
    }

    register_response = requests.post('https://cjdgrevival.com/api/register', cookies=register_cookies, headers=register_headers, json=register_json_data)

    if register_response.status_code==200:
        print(f'success {nameInput}:{passwordInput}')
        with open("saved-accounts.txt", "a") as f:
            f.write(f'{nameInput}:{passwordInput}\n')
    else:
        print('failed')

for i in range(countInput):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    time.sleep(2)