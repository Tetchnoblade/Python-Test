import requests
import time

inputUserName = str(input("ユーザー名: "))
inputRoomId = str(input("隠れ乱闘合言葉: "))
inputMessage = str(input("送信メッセージ: "))
inputLength = int(input("送信回数: "))
inputDelay = int(input("送信遅延: "))

def createToken():
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
        awa = response.json()
        return awa['idToken']
    else:
        return False

def createPrivateRoom(idtoken):
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {idtoken}', #関数にidtokenの追加
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
        'userName': inputUserName,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/createRoom', headers=headers, json=json_data)

    if response.status_code==200:
        return response.json()['roomId']
    else:
        return False

def addRoomUser(idtoken, getRoom):
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
        'userName': inputUserName,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/addRoomUser', headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        return False

counter = 1

def sendChat(idtoken, getRoom,counter):
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
        'text': inputMessage+' '+str(counter),
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/setComment', headers=headers, json=json_data)

    if response.status_code==200:
        return True
    else:
        return False

getToken = createToken()

if getToken:
    print('='*60)
    print('トークン生成成功')
    getRoom = createPrivateRoom(getToken)
else:
    print('トークン生成失敗')

if getRoom:
    print('部屋作成成功')
    omgRoomUser = addRoomUser(getToken,getRoom)
else:
    print('部屋作成失敗')

if omgRoomUser:
    print('部屋参加成功')
    canChat = sendChat(getToken,getRoom,counter)
    print('='*20,'メッセージ送信成功','='*20)
    print(inputMessage+' '+str(counter))
    counter += 1
    time.sleep(inputDelay)
else:
    print('部屋参加失敗')

if canChat:
    for i in range(inputLength-1):
        sendChat(getToken,getRoom,counter)
        print(inputMessage+' '+str(counter))
        counter += 1
        time.sleep(inputDelay)
else:
    print('メッセージ送信失敗')