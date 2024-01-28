#cjdgrevival.com (太鼓ウェブ) 用のアカウントを登録できます

import requests
import random, string
import threading

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

countInput = int(input('アカウント作成数: '))

print(f'{countInput}個作成します')

def get_csrftoken():
    cookies = {
        'session': 'b13e4c3d-27a2-4c47-ae1f-a430857cf389',
        'cf_clearance': '0cfo1hkpS_15Jj7aHYOWP2DsVJxtfdYq7xXsEqgCj_I-1704790958-0-2-b68b5ed1.ea6ca617.f914c988-0.2.1704790958',
    }

    headers = {
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

    response = requests.get('https://cjdgrevival.com/api/csrftoken', cookies=cookies, headers=headers)

    if response.status_code==200:
        return response.json()['token']
    else:
        return False

def send_register():
    cookies = {
        'session': 'b13e4c3d-27a2-4c47-ae1f-a430857cf389',
        'cf_clearance': '0cfo1hkpS_15Jj7aHYOWP2DsVJxtfdYq7xXsEqgCj_I-1704790958-0-2-b68b5ed1.ea6ca617.f914c988-0.2.1704790958',
    }

    headers = {
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
        'x-csrftoken': userToken,
    }

    json_data = {
        'username': nameInput,
        'password': passwordInput,
    }

    response = requests.post('https://cjdgrevival.com/api/register', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        return False

realCount = 1

for i in range(countInput):
    nameInput = randomname(8)
    passwordInput = randomname(6)
    userToken = get_csrftoken()

    if userToken:
        canRegister = send_register()
    else:
        print('token auth failed')

    if canRegister:
        print(f'{nameInput}:{passwordInput} ({realCount}/{countInput})')
        realCount += 1
        f = open('saved-accounts.txt', 'a')
        f.write(f'{nameInput}:{passwordInput}')
        f.write('\n')
        f.close()
    else:
        print('register failed')
        realCount -= 1