#ouo.269seahorse.me (太鼓ウェブ) 用のアカウントを、最大スコアと共に登録できます

import requests
import random, string
import time
import concurrent.futures

countInput = int(input('アカウント作成数: '))
threadInput = int(input('スレッド数: '))

print(f'{countInput*threadInput}個作成します')

def token_generate(sessionInput, name, password):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': sessionInput,
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

def account_verify(sessionInput, token, name, password):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': sessionInput,
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

def cheat_token(sessionInput, name, password):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': sessionInput,
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

def cheat_score(sessionInput, token, name, password):
    cookies = {
        '_ga': 'GA1.1.76857572.1693120866',
        '_ga_ME8M5G343E': 'GS1.1.1703738176.4.1.1703739428.0.0.0',
        'session': sessionInput,
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

def gen():
    name = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
    password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    session_code = f"{''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])}-{''.join([random.choice(string.ascii_letters + string.digits) for i in range(4)])}-{''.join([random.choice(string.ascii_letters + string.digits) for i in range(4)])}-{''.join([random.choice(string.ascii_letters + string.digits) for i in range(4)])}-{''.join([random.choice(string.ascii_letters + string.digits) for i in range(12)])}"
    token = token_generate(session_code, name, password)
    if token:
        verify = account_verify(session_code, token, name, password)
        if verify:
            token_hack = cheat_token(session_code, name, password)
            if token_hack:
                score_hack = cheat_score(session_code, token, name, password)
                if score_hack:
                    print(f'Successfully Generated [{name}:{password}]')
                    f = open("saved-accounts.txt", "a")
                    f.write(f'{name}:{password}\n')

for i in range(countInput):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=threadInput)
    for i in range(threadInput):
        executor.submit(gen)
    time.sleep(2)