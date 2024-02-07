#ouo.269seahorse.me (太鼓ウェブ) 用のアカウントを登録できます

import requests
import random, string

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

countInput = int(input('アカウント作成数: '))

print(f'{countInput}個作成します')

def get_csrftoken():
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': '4c290c6a-7f7c-4966-9c93-e2d80387d288',
    }

    headers = {
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

    response = requests.get('https://ouo.269seahorse.me/api/csrftoken', cookies=cookies, headers=headers)

    if response.status_code==200:
        return response.json()['token']
    else:
        return False

def send_register():
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': '4c290c6a-7f7c-4966-9c93-e2d80387d288',
    }

    headers = {
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
        'X-CSRFToken': userToken,
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'username': nameInput,
        'password': passwordInput,
    }

    response = requests.post('https://ouo.269seahorse.me/api/register', cookies=cookies, headers=headers, json=json_data)

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
        with open("saved-accounts.txt", "a") as f:
            f.write(f'{nameInput}:{passwordInput}\n')
    else:
        print('register failed')
        realCount -= 1