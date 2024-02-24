#girlschannel.netのコメントに自動投票します

import requests
import time
import random, string

print('トピックのURL末の数字を入力してください')
input_topicid = input('https://girlschannel.net/topics/')
input_good_or_bad = input('バッドの場合は0, グッドの場合は1: ')

print('全ての悲しき女性に対し、平等に投票を開始します')

def random_code(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])

def send_request():
    cookies = {
        'CakeCookie[p72_cookie_id]': f'{random_code(12)}.{random_code(30)}',
        '_ss_pp_id': random_code(32),
        '_td': f'{random_code(8)}-{random_code(4)}-{random_code(4)}-{random_code(4)}-{random_code(12)}',
    }

    headers = {
        'authority': 'girlschannel.net',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'referer': f'https://girlschannel.net/topics/{input_topicid}',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    params = {
        'value': input_good_or_bad,
        'topic_id': input_topicid,
        'comment_id': f'vbox{counter}',
    }

    response = requests.get('https://girlschannel.net/topics/post_value', params=params, cookies=cookies, headers=headers)

    try:
        res = str(response.json())

        if response.status_code==200 and res=='True':
            print('成功しました')
        else:
            print('失敗しました')
    except:
        print('既に投票済みです')

counter = 1
    
while True:
    send_request()
    counter+=1