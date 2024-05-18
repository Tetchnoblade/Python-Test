import requests
import threading
from bs4 import BeautifulSoup

def convert_url(html):
    soup = BeautifulSoup(html, 'lxml')
    download_link = None
    for a_tag in soup.find_all('a', href=True):
        if a_tag['href'].startswith("http://terafile.site/download/"):
            download_link = a_tag['href']
            break
    if download_link:
        return download_link
    else:
        return False

def send_file(name):
    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'origin': 'https://terafile.site',
        'referer': 'https://terafile.site/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    files = {
        'file': (name, open(name, 'rb'), 'image/png'),
    }

    response = requests.post('https://terafile.site/upload', headers=headers, files=files)

    if response.status_code == 200:
        link = convert_url(response.text)
        if link:
            print(f'ok {link}')
            return True
        else:
            return False
    else:
        print('failed')
        return False

count = int(input('何回アップロードしますか: '))
name = input('画像名.png: ')

threads = []
for _ in range(count):
    thread = threading.Thread(target=send_file, args=(name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()