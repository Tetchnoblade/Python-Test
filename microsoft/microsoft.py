#自動でMicrosoftのアカウントを作成します
#Recaptchaのみ手動です

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from os import path

print('メールアドレスは 8 文字以上にする必要があり、一文字目は数字以外である必要があります。')
print('パスワードは 8 文字以上にする必要があり、大文字、小文字、数字、記号のうち 2 種類以上を含んでいる必要があります。')

inputEmail = str(input('メルアド: '))
inputPassword = str(input('パス: '))

inputNameLast = 'tanaka'
inputNameFirst = 'tarou'
inputDate = '2000'
inputMonth = '1'
inputDay = '23'

urls = ['https://www.microsoft.com/ja-jp']
s = Service(path.join(path.dirname(__file__), 'chromedriver.exe'))

for url in urls:
    driver = webdriver.Chrome(service=s)

driver.get(url)

try:
    accPos = driver.find_element(By.ID, 'mectrl_headerPicture')
    accPos.click()
    print('accおけ')
except:
    print('accだめ')

try:
    signUpPos = driver.find_element(By.ID, 'signup')
    signUpPos.click()
    print('signupボタンおけ')
except:
    print('signupボタンだめ')

try:
    setForNewAcc = driver.find_element(By.ID, 'liveSwitch')
    setForNewAcc.click()
    print('liveSwitchおっけー')
except:
    print('liveSwitchダメ～')

sleep(1)

try:
    emailPos = driver.find_element(By.ID, 'MemberName')
    emailPos.send_keys(inputEmail)
    print('emailセットおっけー')
except:
    print('emailセットダメ～')

try:
    emailSendPos = driver.find_element(By.ID, 'iSignupAction')
    emailSendPos.click()
    print('emailボタンおっけー')
except:
    print('emailボタンダメ～')

sleep(1)

try:
    passwordPos = driver.find_element(By.ID, 'PasswordInput')
    passwordPos.send_keys(inputPassword)
    print('passwordセットおっけー')
except:
    print('passwordセットダメ～')

try:
    passwordSendPos = driver.find_element(By.ID, 'iSignupAction')
    passwordSendPos.click()
    print('passwordボタンおっけー')
except:
    print('passwordボタンダメ～')

sleep(1)

try:
    lastNamePos = driver.find_element(By.ID, 'LastName')
    lastNamePos.send_keys(inputNameLast)
    print('lastnameセットおっけー')
except:
    print('lastnameセットダメ～')

try:
    firstNamePos = driver.find_element(By.ID, 'FirstName')
    firstNamePos.send_keys(inputNameFirst)
    print('firstnameセットおっけー')
except:
    print('firstnameセットダメ～')

try:
    nameSendPos = driver.find_element(By.ID, 'iSignupAction')
    nameSendPos.click()
    print('namesボタンおっけー')
except:
    print('namesボタンダメ～')

sleep(1)

try:
    DatePos = driver.find_element(By.ID, 'BirthYear')
    DatePos.send_keys(inputDate)
    print('dateセットおっけー')
except:
    print('dateセットダメ～')

try:
    MonthPos = driver.find_element(By.ID, 'BirthMonth')
    MonthPos.send_keys(inputMonth)
    print('monthセットおっけー')
except:
    print('monthセットダメ～')

try:
    DayPos = driver.find_element(By.ID, 'BirthDay')
    DayPos.send_keys(inputDay)
    print('dayセットおっけー')
except:
    print('dayセットダメ～')

try:
    profileSendPos = driver.find_element(By.ID, 'iSignupAction')
    profileSendPos.click()
    print('profileボタンおっけー')
except:
    print('profileボタンダメ～')

sleep(1)

print('captcha完了を待っています')
print('okと入力するとアカウント情報を保存して終了します')

inputYes = str(input('Finished: '))

if inputYes=='Ok' or inputYes=='oK' or inputYes=='OK' or inputYes=='ok':
    f = open('saved-accounts.txt', 'a')
    f.write(f'{inputEmail}@outlook.jp:{inputPassword}')
    f.write('\n')
    f.close()
    print('アカウント情報を saved-accounts.txt に保存しました')
else:
    print('終了します')