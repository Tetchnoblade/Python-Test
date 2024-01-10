#自動でstresser.zone用のアカウントを作成します (作成途中)
#Recaptchaのみ手動です

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

inputUsername = 'OmgAspwMoment'
inputPassword = 'awawa1919!'

urls = ['https://stresser.zone/register']
s = Service(r'C:\Users\0kcab\Documents\Python\automicrosoft\chromedriver.exe')

for url in urls:
    driver = webdriver.Chrome(service=s)

driver.get(url)

try:
    setUser = driver.find_element(By.ID, '#ここ取得できなくて困ってる')
    setUser.send_keys(inputUsername)
    print('ぱすおっけー')
except:
    print('パスダメ～')

try:
    setPass = driver.find_element(By.ID, 'password')
    setPass.send_keys(inputPassword)
    print('ぱすおっけー')
except:
    print('パスダメ～')

captchaPos = driver.find_element(By.NAME, 'captcha')
print('captchaすたーと')
while True:
    if len(str(captchaPos))==5:
        print('多分captcha終わった')
        setPass.submit()