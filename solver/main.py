import os
import sys
import requests
from nextcaptcha import NextCaptchaAPI

def req_register():
    cookies = {
        '__dcfduid': '382a10d0f00f11ed8c277d32b3f46620',
        '__sdcfduid': '382a10d1f00f11ed8c277d32b3f4662063f03a5c831975cd0e2eba750299f0c7372c7bac5b519cc18b22508d5d28a4e5',
        '__stripe_mid': '674ff9e5-65fe-4787-b393-9cc5ff7bb9fd9bbca0',
        'cf_clearance': 'DSdl66unh6nz1yK6zqY53qYGc1skk13GuI8.eu9TfNE-1714968484-1.0.1.1-UnDtI5sw0PfYF6HvUGT70d.hOmA5HuTk1jeQrgGQiBlKEtfZwK83tp8WiMmVf3Zs1lZeeGNqXoZBwRS9SnWHgQ',
        '__cfruid': '842b79d744ad39f3bfe628819da2ba42fe7c03a4-1714968666',
        '_cfuvid': 'wJ4sENhVyeKNlmwE7wOA4zDNWUoS7oYYPyAI7QvBmiE-1714968666295-0.0.1.1-604800000',
        'locale': 'ja',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+May+06+2024+13%3A11%3A56+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'priority': 'u=1, i',
        'referer': 'https://discord.com/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-fingerprint': '1236893171502551073.afNMXS5Im8hv1gKxxHx9x4iAQQA',
        'x-track': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImphIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjM3NTAyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
    }

    json_data = {
        'consent': True,
        'fingerprint': '1236893171502551073.afNMXS5Im8hv1gKxxHx9x4iAQQA',
        'global_name': 'wtfmoments',
        'unique_username_registration': True,
    }

    response = requests.post('https://discord.com/api/v9/auth/register', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==400:
        key = response.json()["captcha_sitekey"]
        print(f'got capkey {key}')
        return key
    else:
        print('failed to register')

def req_token():
    cookies = {
        '__dcfduid': '382a10d0f00f11ed8c277d32b3f46620',
        '__sdcfduid': '382a10d1f00f11ed8c277d32b3f4662063f03a5c831975cd0e2eba750299f0c7372c7bac5b519cc18b22508d5d28a4e5',
        '__stripe_mid': '674ff9e5-65fe-4787-b393-9cc5ff7bb9fd9bbca0',
        'cf_clearance': 'DSdl66unh6nz1yK6zqY53qYGc1skk13GuI8.eu9TfNE-1714968484-1.0.1.1-UnDtI5sw0PfYF6HvUGT70d.hOmA5HuTk1jeQrgGQiBlKEtfZwK83tp8WiMmVf3Zs1lZeeGNqXoZBwRS9SnWHgQ',
        '__cfruid': '842b79d744ad39f3bfe628819da2ba42fe7c03a4-1714968666',
        '_cfuvid': 'wJ4sENhVyeKNlmwE7wOA4zDNWUoS7oYYPyAI7QvBmiE-1714968666295-0.0.1.1-604800000',
        'locale': 'ja',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+May+06+2024+13%3A11%3A56+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'authorization': 'MTIzNjg5MzE3MTUwMjU1MTA3Mw.GXF1cE.pu2Nt6_vlVCFSJIPTvhwxHHQp9VOmZaSJaFnSM',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'priority': 'u=1, i',
        'referer': 'https://discord.com/channels/@me',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'ja',
        'x-discord-timezone': 'Asia/Tokyo',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImphIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI5MDQ1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
    }

    json_data = {
        'date_of_birth': '2000-01-23',
    }

    response = requests.patch('https://discord.com/api/v9/users/@me', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==200:
        token = response.json()["token"]
        print(f'got token [{token}]')
        return token
    else:
        print('failed to get token')
 
def solver(key):
    api = NextCaptchaAPI(client_key="next_0b3a0fb669d9199c07e37e1d1a68f95e3a")
    result = api.hcaptcha(website_url="https://discord.com/api/v9/auth/register", website_key=key)
    sys.exit('solved: ' + str(result))
    return True

capkey = req_register()
if capkey:
    solver(capkey)
    if solver:
        token = req_token()
        if token:
            print('completed')