import requests
import time
import concurrent.futures

print('ラーメンを啜ります')

base_ramen = 0

def ramen():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlFIRlF2WmIzb09HcUJrOFNud2gzMGc9PSIsInZhbHVlIjoieWR4Y1paVTdpUW9JWUVwNWZVajU3VTdTZkg2TEJvRm1RRDVlSEE1OVRURzVxYjRYakZaSENTc2pSUXdPVFRZZyIsIm1hYyI6ImFlNjUwYzcyZWFhMTJlYzY5M2Q1ZGU3NjZkNWYzYjk2MGUzYWZlY2IyNTI5NTBmNTZhM2JlYzRlYjE0NTMzZjMifQ%3D%3D',
        'laravel_session': 'eyJpdiI6IjBJaEtKMGZPbHQzRXN4cUVxMHhOSWc9PSIsInZhbHVlIjoicjZ4eVRqckdLVmV6cXB2NEljSUxncHZUYXJhS3c0Tk5CMzR5OGNtS2l4RDA5M3BDZDViK090MkQwU3JKOWZXVzFHQVJ2NUFUMWthVlVCWEpFcG5nekNuZWJrMklONDNma3k1QWI2OTFwQVN3T1QyT09DS0M2XC9ZXC82a0ltWWZiNSIsIm1hYyI6ImFjODYyMDFlNTlmOTBmYjhmNjU1YmQwMTQxMTE0MzZhMzAzNjdiYWRhN2Q0ZDBiZjQ2ZjZhOWYwZDgyMGUyNmQifQ%3D%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
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
        'parent_id': '4228',
        'entry_id': '567',
        'commentator': 'へずま',
        'sex': 'male',
        'age': '70',
        'content': 'おれへずまらーめんたべてね',
        '_token': 'NI1mXdCr4Z6p8TZJOA1hQ9yevY96Vsma6vvbixDF',
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