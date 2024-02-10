#discord.com用のプロモーションNitroを作成します

import requests
import random, string
import time
import sys
import os
import concurrent.futures

generateCount = int(input("Nitro作成数: "))
inputThread = int(input("スレッド数: "))

def randomCode(length):
    return ''.join([random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(length)])

def sendRequest():
    code = f"{randomCode(16)}"
    request = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/https://discord.gift/{code}?with_application=false&with_subscription_plan=true")

    if request.status_code == 200:
        print(f'Valid: {code}')
        f = open("valid.txt", "a")
        f.write(f"https://discord.gift/{code}\n")
    else:
        print(f'Invalid: {code}')

print(f'Generating... (x{generateCount*inputThread})')

for i in range(generateCount):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=inputThread)
    for i in range(inputThread):
        executor.submit(sendRequest)
    time.sleep(0.01)