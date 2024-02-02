#自動でMicrosoftのアカウントを作成します
#Recaptchaのみ手動です

import random, string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from os import path

inputMode = str(input('IDを手動設定しますか? Noの場合、自動でランダムなIDが割り当てられます (y/n): '))

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def get_proxies(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

if inputMode=='y':
    print('メールアドレスは 8 文字以上にする必要があり、一文字目は数字以外である必要があります。')
    print('パスワードは 8 文字以上にする必要があり、大文字、小文字、数字、記号のうち 2 種類以上を含んでいる必要があります。')
    inputEmail = str(input('メールアドレス: '))
    inputPassword = str(input('パスワード: '))
else:
    inputEmail = randomname(10)
    inputPassword = randomname(10)

inputProxyMode = str(input('Proxy (Http) を使用しますか (y/n): '))

inputNameLast = randomname(6)
inputNameFirst = randomname(6)
inputDate = '2000'
inputMonth = '1'
inputDay = '1'

urls = ['https://www.microsoft.com']
s = Service(path.join(path.dirname(__file__), 'chromedriver.exe'))

if inputProxyMode=='y':
    proxies_list = get_proxies('proxies.txt')
    for url in urls:
        print('プロキシ接続中...')
        selected_proxy = random.choice(proxies_list)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={selected_proxy}')
        driver = webdriver.Chrome(service=s, options=chrome_options)
        driver.get(url)
else:
    for url in urls:
        driver = webdriver.Chrome(service=s)
        driver.get(url)

def solver(webID, sendMode, oklog, failedlog, afterSleepTime):
    try:
        setterID = driver.find_element(By.ID, webID)
        if sendMode=='click':
            setterID.click()
        if sendMode=='email':
            setterID.send_keys(inputEmail)
        if sendMode=='password':
            setterID.send_keys(inputPassword)
        if sendMode=='lastname':
            setterID.send_keys(inputNameLast)
        if sendMode=='firstname':
            setterID.send_keys(inputNameFirst)
        if sendMode=='year':
            setterID.send_keys(inputDate)
        if sendMode=='month':
            setterID.send_keys(inputMonth)
        if sendMode=='day':
            setterID.send_keys(inputDay)
        print(oklog)
    except:
        print(failedlog)
    sleep(afterSleepTime)

solver('mectrl_headerPicture', 'click', 'OpenUI True', 'OpenUI False', 0)
solver('signup', 'click', 'SignUp True', 'SignUp False', 0)
solver('liveSwitch', 'click', 'liveSwitch True', 'liveSwitch False', 1)
solver('MemberName', 'email', 'Email True', 'Email False', 0)
solver('iSignupAction', 'click', 'Email Press True', 'Email Press False', 1)
solver('PasswordInput', 'password', 'Password True', 'Password False', 0)
solver('iSignupAction', 'click', 'Password Press True', 'Password Press False', 1)
solver('LastName', 'lastname', 'LastName True', 'LastName False', 0)
solver('FirstName', 'firstname', 'FirstName True', 'FirstName False', 0)
solver('iSignupAction', 'click', 'Name Press True', 'Name Press False', 1)
solver('BirthYear', 'year', 'Date True', 'Date False', 0)
solver('BirthMonth', 'month', 'Month True', 'Month False', 0)
solver('BirthDay', 'day', 'Day True', 'Day False', 0)
solver('iSignupAction', 'click', 'Profile True', 'Profile False', 1)

print('Recaptcha完了を待っています...')
print('アカウント情報を保存して終了しますか？')

inputField = str(input('y/n: '))

if inputField=='y':
    f = open('saved-accounts.txt', 'a')
    f.write(f'{inputEmail}@outlook.jp:{inputPassword}')
    f.write('\n')
    f.close()
    print('アカウント情報を saved-accounts.txt に保存しました')
else:
    print('終了します')