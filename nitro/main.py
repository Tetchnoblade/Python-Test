#discord.com用のプロモーションNitroを作成します

import requests
import time
import sys
import os
import concurrent.futures

generateCount = int(input("Nitro作成数 x20: "))

def sendRequest():
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    headers = {
        "origin": "https://www.opera.com",
        "Content-Type": "application/json",
        "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
    }
    data = {
        "partnerUserId": "bc385c68-be5f-43c2-9713-cb2051fef65b"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        got = response.json()['token']
        print(f'Generated - [https://discord.com/billing/partner-promotions/1180231712274387115/{got}]')
        with open("generated.txt", "a") as f:
            f.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{got}\n")
    else:
        print(f'Failed to Generate')

print(f'生成中です... (x{generateCount*20})')

for i in range(generateCount):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    executor.submit(sendRequest)
    time.sleep(2)