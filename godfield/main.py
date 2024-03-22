#godfield.netのスパム、嫌がらせツールです

import requests
import random, string
import time
import concurrent.futures

inputThread = int(input('アカウント数: '))
print('モードを選択してください 1.隠れ乱闘 2.真剣タイマン(テスト)')
gameMode = int(input('(1/2): '))
if gameMode==1:
    inputRoomId = input('隠れ乱闘合言葉: ')
    print('隠れ乱闘荒らしモードを選択してください 1.スパム 2.ぴょこぴょこ')
    inputMode = int(input('(1/2): '))
    if inputMode==1:
        inputMessage = input('送信メッセージ: ')
        inputLength = int(input('送信回数: '))
        inputRetry = int(input('何回送信したらアカウントを変更しますか: '))
        inputLeft = input('スパム後、部屋を退出しますか? (y/n): ')
    if inputMode==2:
        inputRoop = int(input('ぴょこぴょこ回数: '))

print('開始します')

def randomCode(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])

def get_token():
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
        return response.json()['idToken']
    else:
        return False

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
        return response.json()['roomId']
    else:
        return False

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
        return True
    else:
        return False

def add_dueluser(username, idToken):
    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {idToken}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    json_data = {
        'mode': 'duel',
        'userName': username,
        'lang': 'ja',
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/addDuelUser', headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        return False

def duel_createroom(username, token, roomid):
    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    json_data = {
        'mode': 'duel',
        'roomId': roomid, #これ取得方法わからなくて鬱 助けてくれや
        'userName': username,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/addRoomUser', headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        return False

def remove_user(username, token, roomId):
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {token}',
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
        return True
    else:
        return False

def send_chat(name, idtoken, getRoom, recount):
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

    sendtext = f'{inputMessage} {randomCode(3)}'

    json_data = {
        'mode': 'hidden',
        'roomId': getRoom,
        'text': sendtext,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/setComment', headers=headers, json=json_data)

    if response.status_code==200:
        print(f'<{name}> Sent message [{sendtext}]')
        if recount>=inputRetry:
            print(f'<{name}> Disconnecting...')
            remove_user(name, idtoken, getRoom)
    else:
        if recount<inputRetry:
            print(f'<{name}> Failed to send message!')
        do_pyoko()

def do_pyoko():
    userName = randomCode(8)
    retryCount = 0
    print(f'<{userName}> Generated Name')
    token = get_token()
    if token:
        print(f'<{userName}> Token Generated')
        if gameMode==1:
            roomid = create_room(userName, token)
            if roomid:
                print(f'<{userName}> Got RoomID')
                if inputMode==1:
                    adduser = addroom_user(userName, token, roomid)
                    if adduser:
                        print(f'<{userName}> Joined')
                        for i in range(inputLength):
                            send_chat(userName, token, roomid, retryCount)
                            retryCount += 1
                        if inputLeft=='Y' or inputLeft=='y':
                            deleteuser = remove_user(userName, token, roomid)
                            if deleteuser:
                                print(f'<{userName}> Left')
                if inputMode==2:
                    for i in range(inputRoop):
                        adduser = addroom_user(userName, token, roomid)
                        if adduser:
                            print(f'<{userName}> Joined')
                            deleteuser = remove_user(userName, token, roomid)
                            if deleteuser:
                                print(f'<{userName}> Left')
        if gameMode==2:
            dueluser = add_dueluser(userName, token)
            if dueluser:
                print(f'<{userName}> Got DuelID')
                randomroom = randomCode(20)
                room = duel_createroom(userName, token, randomroom)
                if room:
                    print(f'<{userName}> Joined Duel [{randomroom}]')
                else:
                    print(f'<{userName}> Failed to join Duel [{randomroom}]')
    else:
        print(f'<{userName}> Rate Limited!')
        inputThread -= 1

executor = concurrent.futures.ThreadPoolExecutor(max_workers=inputThread)
for i in range(inputThread):
    executor.submit(do_pyoko)