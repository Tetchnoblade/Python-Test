#cjdgrevival.com (太鼓ウェブ) 用のアカウントを登録できます
#pythonもっと勉強したら複数垢同時とか頑張ります

import requests

nameInput = str(input('登録ユーザー名: '))
passInput = str(input('登録パスワード: '))

userInfo = [nameInput, passInput]

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
        'username': userInfo[0],
        'password': userInfo[1],
    }

    response = requests.post('https://cjdgrevival.com/api/register', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        return False

userToken = get_csrftoken()
if userToken:
    print('')
    print('トークンをゲットしました')
    canRegister = send_register()
else:
    print('')
    print('トークンのゲットに失敗しました')

if canRegister:
    print('アカウント生成に成功しました')
    print('')
    print('='*10,'アカウント情報','='*10)
    print('ユーザー名:',userInfo[0])
    print('パスワード:',userInfo[1])
    print('トークン:',userToken)
    print('='*36)
else:
    print('')
    print('アカウント作成に失敗しました')