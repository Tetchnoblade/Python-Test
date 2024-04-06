import requests
import time
import concurrent.futures

print('ラーメンを啜ります')

base_ramen = 0

def ramen():
    cookies = {
        '_ga_52HKHPQQED': 'GS1.1.1712414099.1.0.1712414099.0.0.0',
        '_ga': 'GA1.2.890191871.1712414099',
        '_gid': 'GA1.2.249636978.1712414099',
        '_gat_gtag_UA_48286578_9': '1',
        '__gads': 'ID=9dff4f20bb5008d5:T=1712414098:RT=1712414098:S=ALNI_MbEHUjrGr6FOxJODfSmI6PVGLqkaQ',
        '__gpi': 'UID=00000de3060e66e1:T=1712414098:RT=1712414098:S=ALNI_MZ99pekju0f-c3BczuWFFBAiPmPuQ',
        '__eoi': 'ID=8d538e80b6693f08:T=1712414098:RT=1712414098:S=AA-AfjZzIpXcfFes23pzgklNr0D3',
        'FCNEC': '%5B%5B%22AKsRol-b4fuElUL2SfIpVxKpEx6xBCVFJGdwPiFx_uZ1suhtRqfhxRiIHJ062Q8b1OsQskyicdbDFzb-gYWkg-u20jq3eefqWvwu8b9uFfpB9tuNtdWzGc6ZpPzasAMq00ng2kQr-T2xnKBxcRd2hcledv4_2jjVlA%3D%3D%22%5D%5D',
        'XSRF-TOKEN': 'eyJpdiI6ImhCcysrMkUzZjFCMkRvMVlVVTdzVnc9PSIsInZhbHVlIjoic1Q2UUJsUHJKWHJNamJWS1hIS09DS0tDeStHZGxlUHF5TTRCNVlYSm9SczJBemprYU9VcVZQb0Ria2xGUXAxZiIsIm1hYyI6IjhiZDdiMDM2YWUwNGNlMTAzZDg0YTUzNDllOGM3ODBlYjdlM2RhNjRmOGUyYzk3NTk4NWM2YmE3MDUyOWM1MzkifQ%3D%3D',
        'laravel_session': 'eyJpdiI6IlFOU3Y4Q2dkQUR6XC93QkNZYTZDOU1BPT0iLCJ2YWx1ZSI6IkFvUWVMbVBQd1hPVHMrZTJhTU50YllHWktsVEd2dXJJM2dld3lJclEyN3NhSm5WRTdYS2hwcmo5bXRUUkhaS0E1d1YzRlprK0dvQjdKK0VXdm52ek52UGZBcGFqNStxaUZPa3AwSUlBN2QwVHFOVVdpMlwvWTllU29iRUpzblMybyIsIm1hYyI6IjQxMmNmMjc4OTdhZDdiNDIwMDY2YmIyZmQzZGE3N2M0N2ViNjdkZTUzZGY2MTY4NWQxYTAzYjY4MDhlM2NkZWMifQ%3D%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://tuber-review.com',
        'referer': 'https://tuber-review.com/youtubers/567',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'parent_id': '1133',
        'entry_id': '567',
        'commentator': 'Aspw',
        'sex': 'male',
        'age': '20',
        'content': 'へずまりゅうさんはラーメン作って改心したんだから許せ（●｀ε´●）',
        '_token': 'bbZzmx0Py2Xb36IGDIErP7MK8W02krkr3sVkJMcc',
    }

    response = requests.post('https://tuber-review.com/comments/child', cookies=cookies, headers=headers, data=data)

    if response.status_code==200:
        print(f'募金成功 ({base_ramen}円)')
        return True
    else:
        print('募金失敗')
        return False

while True:
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    for i in range(8):
        executor.submit(ramen)
        base_ramen+=1
    time.sleep(1.5)