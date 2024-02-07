#discord.com用のプロモーションNitroを作成します

import requests
import time
import sys
import os
import threading
from concurrent.futures import ThreadPoolExecutor

generateCount = int(input("Nitro作成数: "))

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
        f = open('generated.txt', 'a')
        f.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{response.json()['token']}")
        f.write('\n')
        f.close()

print(f'生成中です... (x{generateCount})')

thread = ThreadPoolExecutor(max_workers=3)

for i in range(generateCount):
    thread.submit(sendRequest)