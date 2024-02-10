#discord.com用のプロモーションNitroを作成します

import requests
import random, string
import time
import sys
import os
import concurrent.futures

generateCount = int(input("Amount: "))
inputThread = int(input("Thread: "))

def randomCode(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])

def sendRequest():
    code = f"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..{randomCode(11)}_{randomCode(4)}.{randomCode(29)}-{randomCode(34)}-{randomCode(42)}-{randomCode(101)}-{randomCode(39)}_{randomCode(37)}"
    print(f'Generated - [https://discord.com/billing/partner-promotions/1180231712274387115/{code}]')
    f = open("generated.txt", "a")
    f.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{code}\n")

print(f'Generating... (x{generateCount*inputThread})')

for i in range(generateCount):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=inputThread)
    for i in range(inputThread):
        executor.submit(sendRequest)
    time.sleep(0.01)