#discord.com用のアカウントを作成します (作成途中)
#hCaptchaの解決ができないので助けてください (16行目)

import requests
import random, string
import concurrent.futures

threadCount = 1
userID = ''

def random_code(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])

def captcha_solver():
    print('solving...')
    key = None #HELPME
    print('got captcha key:',key)
    return key

def send_first():
    cookies = {
        '__dcfduid': '403b77c0c7f811ee997dd9507364c78c',
        '__sdcfduid': '403b77c1c7f811ee997dd9507364c78c567ebfcb2d040d2732be566be96d6ccd4164769fb84a8b5e1bee82f765f80d49',
        '__cfruid': 'ec6550f252328189f303ce677e6755561fd0c197-1707557953',
        '_cfuvid': 'Vl7MU._NCLu.8yWMPDa31OazZVfwQUNUQGG3bPNCzs8-1707557953856-0-604800000',
        'locale': 'ja',
        'cf_clearance': 'kqWagOYVNwKEZ.MjS0y3Hpu9tTiFUszG1GF5A5WE9eY-1707557954-1-AZZXx6QuboQ6R91apiTbG64J0OtKsl95OaAF6gqrKgz+l6HwWl5bvaWHItWuTqNhLEKFJv2wGBUZcKsnRjlVWNc=',
        '_gcl_au': '1.1.1824395559.1707557957',
        '_ga': 'GA1.1.9495129.1707557957',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Sat+Feb+10+2024+18%3A39%3A43+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
        '_ga_Q149DFWHT7': 'GS1.1.1707557956.1.1.1707558008.0.0.0',
    }

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'ja',
        'content-type': 'application/json',
        # 'cookie': '__dcfduid=403b77c0c7f811ee997dd9507364c78c; __sdcfduid=403b77c1c7f811ee997dd9507364c78c567ebfcb2d040d2732be566be96d6ccd4164769fb84a8b5e1bee82f765f80d49; __cfruid=ec6550f252328189f303ce677e6755561fd0c197-1707557953; _cfuvid=Vl7MU._NCLu.8yWMPDa31OazZVfwQUNUQGG3bPNCzs8-1707557953856-0-604800000; locale=ja; cf_clearance=kqWagOYVNwKEZ.MjS0y3Hpu9tTiFUszG1GF5A5WE9eY-1707557954-1-AZZXx6QuboQ6R91apiTbG64J0OtKsl95OaAF6gqrKgz+l6HwWl5bvaWHItWuTqNhLEKFJv2wGBUZcKsnRjlVWNc=; _gcl_au=1.1.1824395559.1707557957; _ga=GA1.1.9495129.1707557957; OptanonConsent=isIABGlobal=false&datestamp=Sat+Feb+10+2024+18%3A39%3A43+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _ga_Q149DFWHT7=GS1.1.1707557956.1.1.1707558008.0.0.0',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-fingerprint': '1205810202897678416.U8FJVuN19tuoVLfQta_AAxV1QuY',
        'x-track': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImphIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
    }

    json_data = {
        'consent': True,
        'fingerprint': '1205810202897678416.U8FJVuN19tuoVLfQta_AAxV1QuY',
        'global_name': userID,
        'unique_username_registration': True,
    }

    response = requests.post('https://discord.com/api/v9/auth/register', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==400:
        print('continue to hCaptcha')
        captcha_solver()
    elif response.status_code==201:
        print('register 2')
        register_2()
    else:
        print('failed to register 1')
        return False

def register_2():
    cookies = {
        '__dcfduid': '403b77c0c7f811ee997dd9507364c78c',
        '__sdcfduid': '403b77c1c7f811ee997dd9507364c78c567ebfcb2d040d2732be566be96d6ccd4164769fb84a8b5e1bee82f765f80d49',
        '__cfruid': 'ec6550f252328189f303ce677e6755561fd0c197-1707557953',
        '_cfuvid': 'Vl7MU._NCLu.8yWMPDa31OazZVfwQUNUQGG3bPNCzs8-1707557953856-0-604800000',
        'locale': 'ja',
        'cf_clearance': 'kqWagOYVNwKEZ.MjS0y3Hpu9tTiFUszG1GF5A5WE9eY-1707557954-1-AZZXx6QuboQ6R91apiTbG64J0OtKsl95OaAF6gqrKgz+l6HwWl5bvaWHItWuTqNhLEKFJv2wGBUZcKsnRjlVWNc=',
        '_gcl_au': '1.1.1824395559.1707557957',
        '_ga': 'GA1.1.9495129.1707557957',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Sat+Feb+10+2024+18%3A46%3A11+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
        '_ga_Q149DFWHT7': 'GS1.1.1707557956.1.1.1707558378.0.0.0',
    }

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'ja',
        'content-type': 'application/json',
        # 'cookie': '__dcfduid=403b77c0c7f811ee997dd9507364c78c; __sdcfduid=403b77c1c7f811ee997dd9507364c78c567ebfcb2d040d2732be566be96d6ccd4164769fb84a8b5e1bee82f765f80d49; __cfruid=ec6550f252328189f303ce677e6755561fd0c197-1707557953; _cfuvid=Vl7MU._NCLu.8yWMPDa31OazZVfwQUNUQGG3bPNCzs8-1707557953856-0-604800000; locale=ja; cf_clearance=kqWagOYVNwKEZ.MjS0y3Hpu9tTiFUszG1GF5A5WE9eY-1707557954-1-AZZXx6QuboQ6R91apiTbG64J0OtKsl95OaAF6gqrKgz+l6HwWl5bvaWHItWuTqNhLEKFJv2wGBUZcKsnRjlVWNc=; _gcl_au=1.1.1824395559.1707557957; _ga=GA1.1.9495129.1707557957; OptanonConsent=isIABGlobal=false&datestamp=Sat+Feb+10+2024+18%3A46%3A11+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _ga_Q149DFWHT7=GS1.1.1707557956.1.1.1707558378.0.0.0',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-fingerprint': '1205811920251134016.o3WcRsp6gzB-PLWdx9S06iWhhQM',
        'x-track': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImphIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
    }

    json_data = {
        'consent': True,
        'fingerprint': '1205811920251134016.o3WcRsp6gzB-PLWdx9S06iWhhQM',
        'captcha_key': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQYFvIrhrHAlbD84S249XhFbypF9zB02JR4cCjLQAsZxc5Z0i-ny8dxiPAtB_IV-tus01lCleKYM0jh04dM22nYA6RRU-JrYwJRJaquNPrYT42hyZsMQ_yI-151jJjpYsUk_rpKFq3z2_8IIJ7c6Iw5nXFtiQ6ieDvtz_sPpKu9gFjLNKd8HUWLfOn5jBusT2tmH-Ax7Uz9kKoRMOHQ4Mq6hPsjiVPoj0smRMn5HwzszEH40qBTRt4WLy-Lj8x8UU601OwlLHeykYs44HDcJyh04fjo4cCQA9nDZQV6hkUzyz5BMpQevOxd0VIcvaX_1J-Qfxw6aeMNX6D7pWLC2rwN5a7wjBYNn7nQk47qxFL6oqk7kaYD5mFpHpaYV9CEvg4kimUY6jU3z-ZErA-Oym57rKiEw1m94B0Jdxci9fK-ps-uDMAgoBSSPHv4876V4x8uFnuTwH5HJSuEANA6Ne3z362rD6fdDy7gwLrFZNA2tplYQA9Ap2YA_wzWeqtO2wWI14QGSNGIsatUtsh8phuO7hWOoOM1sV6w5DUvo2D4iEeCvz9yXqQBIkQXxOCIDRIzf0ROmhvAbFYScZDBUnqeo1uBVtuDSb_3ZH1qiPlh23Jht5ZY9BPu5aU7hJ4DAuyg1JVvySHogX4IPaeEW5wHQSJNIOZGdnBdOsf7i-pTY76QoIH-g0K_i2-ulWdVx-R640MbOR1wKCNnT5GzCt1FFxcuvPmQO3kEXSJD6kc5i9z7U1RpkvtRXlqcwiPN9TngcvXZNPFobmetNix2UK2pkszf9nzQMfbEkKsXMCFe_KcmiRe8yRwsr0IeQgQSxLJjY-zgx6IKWzRFHSmeNlMiVktFZVgz1aISN2ZQbHH5fkqHECCBkx-NKMLDhcvhBWven6a238ZaFWnkgjdS3527s29HeZPR8co_p5iGx7bhbu5Zh5-wwxL4lAhZZeMwcGq5Pfn8FQAVIKz7GvQPXIVfA65DGR5YYHf2p-EQyyILNjyzR-5VtE1Nw9ou7yvt92U8AOmAEFGv3tPEgdW3hc2fpUeCNXgYvXg-aYpiUCzEK8Mct7bUTZzhRaml6-RPx1nwOrfhYN4dePiNco1FmlVVUd5YvMLoIxCIOFGgfma3k1tQLNmbXSJtAB6BpWHbCRQNfqZLTkmgao_T3JYq-SVlJufzXND3-oJBdbUXSREq1OYiwidZ7-Qw219WRP2FjBtX0m1E2ErJnEhqC1hVU4eXCMt23ChFlgdTO6bXKM4lMKlaNOekeTEFh0bddUD-zzoURn50NkzmGLajo7tR2ez87dWOfaYr-aXySAFiYdcAObTOr5dsK5CxpD9RbN4qq-2ee2igLHUd3D4mGglA_d0CkM6hgwameXPMfi_jNyHPdMLY4SvpNPOUJrv7fRUEzvqS9jIUPMwEITl7QN4rTEjk0S1UbQWzKYC1DvCrP3QfBkRGAEYjVkUddbMmZZ5IibgoDihv10y4ROWUg5JpKnqkEBIXVKJciZYQeat0ClPtbA_qlcYNO1xBfSNcsdZINMiKaZKY_gLGMfmH7RxeR6UvZuf9F3IXiXqCoarB8sbzAq0esC3-x5sbXKgJo2AzSFM6OruffLwB6i5A56Eg-xB1JX6q6KZ2xGBwgLKM78Mmt7S34zwHCSxuKMryz_VvL4X9X4ubMGsViVofeZ0ifq2jS2j4mboLGepmx6KeuvEWoh0h-vk7zyiRga2VjikH41AeMP5r6wshnBQTwuugD76aBce_PO037clDHTJKKqtc4cWQWCWG6IiFQ5wqqABUfA8YyQAj8zwFq5PL52S_XR4FmIsvrXA6z7KnPxkBEdJ5D5apA8JymNIJbNRczxhHrzY1kyWK3oYps82Jb7f9Wkp9h8FbcKc1_zj4lCvw3zNSaBK0si6jv1i-C__Go1WG78vzGBTWIzge_LDAetau6d4Bg7wWZteKMfPS1REu81iLp3LbOZy8vezAAMBpLYSRuArK6DWLfaX4-eiNTjaOhy826PG4zuVyqCr2EKvJ1cTjtXS8ESRs8rI6-25ob72CyIUI0FP105lSjZXhwzmXHR-ioc2hhcmRfaWTOFZnkVKJwZAA.XkxsKh6ZBTlDcm33mP36QK6r8O8b_fq5whEdcbiUnSA',
        'global_name': userID,
        'unique_username_registration': True,
    }

    response = requests.post('https://discord.com/api/v9/auth/register', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==201:
        print('success register 2')
        get_token()
    else:
        print('failed to register 2')
        return False

def get_token():
    cookies = {
        '__dcfduid': '403b77c0c7f811ee997dd9507364c78c',
        '__sdcfduid': '403b77c1c7f811ee997dd9507364c78c567ebfcb2d040d2732be566be96d6ccd4164769fb84a8b5e1bee82f765f80d49',
        '__cfruid': 'ec6550f252328189f303ce677e6755561fd0c197-1707557953',
        '_cfuvid': 'Vl7MU._NCLu.8yWMPDa31OazZVfwQUNUQGG3bPNCzs8-1707557953856-0-604800000',
        'locale': 'ja',
        'cf_clearance': 'kqWagOYVNwKEZ.MjS0y3Hpu9tTiFUszG1GF5A5WE9eY-1707557954-1-AZZXx6QuboQ6R91apiTbG64J0OtKsl95OaAF6gqrKgz+l6HwWl5bvaWHItWuTqNhLEKFJv2wGBUZcKsnRjlVWNc=',
        '_gcl_au': '1.1.1824395559.1707557957',
        '_ga': 'GA1.1.9495129.1707557957',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Sat+Feb+10+2024+18%3A46%3A11+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
        '_ga_Q149DFWHT7': 'GS1.1.1707557956.1.1.1707558772.0.0.0',
    }

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'ja',
        # 'authorization': 'MTIwNTgxMTkyMDI1MTEzNDAxNg.GKJs8P.U8zGCVTN9lXtgRuHc4iBhuGSWCS6KWPa_MvmXw',
        'content-type': 'application/json',
        # 'cookie': '__dcfduid=403b77c0c7f811ee997dd9507364c78c; __sdcfduid=403b77c1c7f811ee997dd9507364c78c567ebfcb2d040d2732be566be96d6ccd4164769fb84a8b5e1bee82f765f80d49; __cfruid=ec6550f252328189f303ce677e6755561fd0c197-1707557953; _cfuvid=Vl7MU._NCLu.8yWMPDa31OazZVfwQUNUQGG3bPNCzs8-1707557953856-0-604800000; locale=ja; cf_clearance=kqWagOYVNwKEZ.MjS0y3Hpu9tTiFUszG1GF5A5WE9eY-1707557954-1-AZZXx6QuboQ6R91apiTbG64J0OtKsl95OaAF6gqrKgz+l6HwWl5bvaWHItWuTqNhLEKFJv2wGBUZcKsnRjlVWNc=; _gcl_au=1.1.1824395559.1707557957; _ga=GA1.1.9495129.1707557957; OptanonConsent=isIABGlobal=false&datestamp=Sat+Feb+10+2024+18%3A46%3A11+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _ga_Q149DFWHT7=GS1.1.1707557956.1.1.1707558772.0.0.0',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me',
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
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImphIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI2NDkxMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
    }

    json_data = {
        'date_of_birth': '2000-01-23',
    }

    response = requests.patch('https://discord.com/api/v9/users/@me', cookies=cookies, headers=headers, json=json_data)

    if response.status_code==200:
        print(f'get token:',response.json()['token'])
        return response.json()['token']
    else:
        print('failed to get token')
        return False

for i in range(threadCount):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=threadCount)
    for i in range(threadCount):
        userID = random_code(8)
        print(f'trying... (ID: {userID})')
        executor.submit(send_first)