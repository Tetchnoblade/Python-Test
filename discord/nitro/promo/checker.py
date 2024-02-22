#discord.com用のプロモーションNitroを作成します

import requests
import random, string
import time
import sys
import os
import concurrent.futures

generateCount = int(input("Amount: "))

def randomCode(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])

def sendRequest():
    code = f"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..{randomCode(11)}_{randomCode(4)}.{randomCode(29)}-{randomCode(34)}-{randomCode(42)}-{randomCode(101)}-{randomCode(39)}_{randomCode(37)}"

    cookies = {
        '__dcfduid': '382a10d0f00f11ed8c277d32b3f46620',
        '__sdcfduid': '382a10d1f00f11ed8c277d32b3f4662063f03a5c831975cd0e2eba750299f0c7372c7bac5b519cc18b22508d5d28a4e5',
        '__stripe_mid': '674ff9e5-65fe-4787-b393-9cc5ff7bb9fd9bbca0',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+Feb+12+2024+23%3A32%3A22+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false',
        '__cfruid': 'dc357a569ef24205b997cca2f809610e80f88287-1708596619',
        '_cfuvid': 'hrwkH..JfbXVCybVoJ5jXuA7fNicYJcCmcK_2La9zqY-1708596619914-0.0-604800000',
        'cf_clearance': 'KNRwzvoDmWIQcrM_NrEgGgWoW2jCgTP2eDZH26J.w8Y-1708596621-1.0-AWIHebWOz0L1FJocUMxPuFRSIRmrrWyO5jmpHcFtZXoba1dDW5YYoLHdFjCVjhOqV04NAg/ZJvyCfR5aX/sUfVo=',
    }

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': 'MTAwNTM0NjE1MzAzNjAwNTQ2Ng.GKNch9.WlzxY9rS1k7DWs8l1mnlrMP7NwIlHLvUILkeeI',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': f'https://discord.com/billing/partner-promotions/1180231712274387115/{code}',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'ja',
        'x-discord-timezone': 'Asia/Tokyo',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImphIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI2NzIyMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
    }

    json_data = {
        'jwt': code,
    }

    response = requests.post('https://discord.com/api/v9/entitlements/partner-promotions/1180231712274387115',cookies=cookies,headers=headers,json=json_data,)
    
    if response.status_code==200:
        print(f'Valid Promo Code - [{code}]')
        f = open("generated.txt", "a")
        f.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{code}\n")
    elif response.status_code==400:
        print(f'Invalid Promo Code - [{code}]')
    else:
        print('Failed to check!')

print(f'Generating... (x{generateCount})')

for i in range(generateCount):
    sendRequest()
    time.sleep(2)