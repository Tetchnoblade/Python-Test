#godfield.net用のスパマーです

import requests
import random, string
import time
import concurrent.futures

inputThread = int(input('アカウント数(最大12人): '))
inputRoomId = input('隠れ乱闘合言葉: ')
inputMessage = input('送信メッセージ: ')
inputLength = int(input('送信回数: '))

discounter = 0
tokens = []
rooms = []

print('開始します')
print('アカウントを切断する場合はY、しないで終了する場合はNと入力してください')

def randomCode(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])

def get_token():
    joinName = randomCode(8)

    headers = {
        'authority': 'securetoken.googleapis.com',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CJG2yQEIpLbJAQipncoBCPeUywEIlqHLAQjvmM0BCIWgzQEIou7NAQiD8M0BGKfqzQE=',
        'x-client-version': 'Chrome/JsCore/8.10.0/FirebaseCore-web',
    }

    params = {
        'key': 'AIzaSyCBvMvZkHymK04BfEaERtbmELhyL8-mtAg',
    }

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': 'AMf-vBwT2W6HzKVweOopgMNeL2uZy0l_k4kIefACye_rv41Cknxgjdc-0JzZVB2chTYpQ3lGKapTTRIpfk5pLK0upVGBzjjkbgTGvVeh8XlqgyFML4-JOf_NLwaP9fn6KMiyTUlHVcmuL9TlBsXdXhwUvvUHb9ARNupchiGyOgZap6omQMExSxw',
    }

    response = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser', params=params, headers=headers, data=data)

    if response.status_code==200:
        print('トークンを作成しました')
        restoken = response.json()['idToken']
        tokens.append(restoken)
        create_room(joinName, restoken)
    else:
        print('トークン作成に失敗しました')

def create_room(name, idToken):
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {idToken}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'mode': 'hidden',
        'password': inputRoomId,
        'userName': name,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/createRoom', headers=headers, json=json_data)

    if response.status_code==200:
        print('ルームIDを取得しました')
        resroom = response.json()['roomId']
        rooms.append(resroom)
        addroom_user(name, idToken, resroom)
    else:
        print('ルームID取得に失敗しました')

def addroom_user(name, gotToken, roomId):
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {gotToken}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'mode': 'hidden',
        'roomId': roomId,
        'userName': name,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/addRoomUser', headers=headers, json=json_data)

    if response.status_code==200:
        print('部屋参加に成功しました')
        for i in range(inputLength):
            send_chat(gotToken, roomId)
            time.sleep(2)
    else:
        print('部屋参加に失敗しました')

def send_chat(idtoken, getRoom):
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {idtoken}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'mode': 'hidden',
        'roomId': getRoom,
        'text': f'{inputMessage} {randomCode(3)}',
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/setComment', headers=headers, json=json_data)

    if response.status_code==200:
        print('メッセージを送信しました')
    else:
        print('メッセージの送信に失敗しました')

def remove_user(counter, gotToken, roomId):
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {gotToken}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    json_data = {
        'mode': 'hidden',
        'roomId': roomId,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/removeRoomUser', headers=headers, json=json_data)

    if response.status_code==200:
        print('切断に成功しました')
        return True
    else:
        print('切断に失敗しました')
        return False

executor = concurrent.futures.ThreadPoolExecutor(max_workers=inputThread)
for i in range(inputThread):
    executor.submit(get_token)

check = input('')
if check=='y' or check=='Y':
    print('切断を開始します')
    for i in range(inputThread):
        remove_user(discounter, tokens[discounter], rooms[discounter])
        if remove_user:
            discounter += 1
else:
    print('切断せず終了します')