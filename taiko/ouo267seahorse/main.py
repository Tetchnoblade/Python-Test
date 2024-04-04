#ouo.269seahorse.me (太鼓ウェブ) 用のアカウントを、最大スコアと共に登録できます

import requests
import random, string
import time
import concurrent.futures

countInput = int(input('アカウント作成数: '))
threadInput = int(input('スレッド数: '))
print('スコアチートを有効にしますか？(ベータ)')
cheatInput = input('(y/n): ')

print(f'{countInput*threadInput}個作成します')

def token_generate(name, password, cookie):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': cookie,
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
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

def account_verify(token, name, password, cookie):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': cookie,
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ouo.269seahorse.me',
        'Referer': 'https://ouo.269seahorse.me/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'X-CSRFToken': token,
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'username': name,
        'password': password,
    }

    response = requests.post('https://ouo.269seahorse.me/api/register', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        return False

def cheat_token(name, password, cookie):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': cookie,
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://ouo.269seahorse.me/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://ouo.269seahorse.me/api/csrftoken', cookies=cookies, headers=headers)

    if response.status_code==200:
        return True
    else:
        return False

def cheat_score(token, name, password, cookie):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': cookie,
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ouo.269seahorse.me',
        'Referer': 'https://ouo.269seahorse.me/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'X-CSRFToken': token,
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'scores': [
            {
                'hash': 'avDvskwHM+SO8kFAGrNjQw',
                'score': '2lepa,bp,1n,0,dc,98;1c8w8,dc,4d,1f,7x,g',
            },
        ],
    }

    response = requests.post('https://ouo.269seahorse.me/api/scores/save', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        print(f'<{name}:{password}> Failed')
        return False

def random_string(long):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(long)])

def gen():
    name = random_string(8)
    password = random_string(6)
    cookie_session = f"{random_string(8)}-{random_string(4)}-{random_string(4)}-{random_string(4)}-{random_string(12)}"
    token = token_generate(name, password, cookie_session)
    if token:
        verify = account_verify(token, name, password, cookie_session)
        if verify:
            print(f'Successfully Generated [{name}:{password}]')
            f = open("saved-accounts.txt", "a")
            f.write(f'{name}:{password}\n')
            if cheatInput=='Y' or cheatInput=='y':
                token_hack = cheat_token(name, password, cookie_session)
                if token_hack:
                    score_hack = cheat_score(token, name, password, cookie_session)
                    if score_hack:
                        print(f'Added Cheat Scores [{name}:{password}]')

for i in range(countInput):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=threadInput)
    for i in range(threadInput):
        executor.submit(gen)
    time.sleep(2)