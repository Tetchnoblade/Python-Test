import requests
import threading

def first():
    while True:
        cookies = {
            'cf_clearance': 'HUaMQQIJAX9fEQYM3LL0p2.NuAzj4A_j.h08L0tObIc-1714815507-1.0.1.1-XSBvjSdtSfPXOluPQUWAaOmhHYGY4Ook_KPVoKe7bx0Gb_vXMu9OSwBUFk7Vx.dQoSvaQqZyvW6GJI22XMku8Q',
            'cookie_keepalive_insert': '1',
            '_ga': 'GA1.1.787201487.1714815511',
            'cookie_failedSlot': '',
            'cookie_last_page_addrlist': '0',
            'cookie_timezone': 'Asia%2FTokyo',
            '__gads': 'ID=90733eca8951ceeb:T=1714815509:RT=1714815509:S=ALNI_MYyYCbJ0BBVskzhvKcfVN-ASOJjFA',
            '__gpi': 'UID=00000e0b78463fe0:T=1714815509:RT=1714815509:S=ALNI_MYdmr4CJtJBpSAY0Hzwn_7_4Thp-w',
            '__eoi': 'ID=f0b870e0740bb736:T=1714815509:RT=1714815509:S=AA-AfjZQHz458_ws6wo9hI7H1b4S',
            'cookie_csrf_token': '3f1baba6c7387d3ebf7fb02eec7916c6',
            'cookie_sessionhash': 'SHASH%3A402b8bfeae143f7130cdd6053bd827ed',
            '_ga_HMG13DJCGJ': 'GS1.1.1714815510.1.1.1714815514.0.0.0',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'ja',
            'priority': 'u=1, i',
            'referer': 'https://m.kuku.lu/',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"124.0.6367.119"',
            'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'action': 'agreeEULA',
            'nopost': '1',
            'by_system': '1',
            'csrf_token_check': '3f1baba6c7387d3ebf7fb02eec7916c6',
            '_': '1714815513902',
        }

        response = requests.get('https://m.kuku.lu/index.php', params=params, cookies=cookies, headers=headers)

        if response.status_code==200:
            second()

def second():
    cookies = {
        'cf_clearance': 'HUaMQQIJAX9fEQYM3LL0p2.NuAzj4A_j.h08L0tObIc-1714815507-1.0.1.1-XSBvjSdtSfPXOluPQUWAaOmhHYGY4Ook_KPVoKe7bx0Gb_vXMu9OSwBUFk7Vx.dQoSvaQqZyvW6GJI22XMku8Q',
        'cookie_keepalive_insert': '1',
        '_ga': 'GA1.1.787201487.1714815511',
        'cookie_failedSlot': '',
        'cookie_last_page_addrlist': '0',
        'cookie_timezone': 'Asia%2FTokyo',
        '__gads': 'ID=90733eca8951ceeb:T=1714815509:RT=1714815509:S=ALNI_MYyYCbJ0BBVskzhvKcfVN-ASOJjFA',
        '__gpi': 'UID=00000e0b78463fe0:T=1714815509:RT=1714815509:S=ALNI_MYdmr4CJtJBpSAY0Hzwn_7_4Thp-w',
        '__eoi': 'ID=f0b870e0740bb736:T=1714815509:RT=1714815509:S=AA-AfjZQHz458_ws6wo9hI7H1b4S',
        'cookie_csrf_token': '3f1baba6c7387d3ebf7fb02eec7916c6',
        'cookie_sessionhash': 'SHASH%3A402b8bfeae143f7130cdd6053bd827ed',
        '_ga_HMG13DJCGJ': 'GS1.1.1714815510.1.1.1714815514.0.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja',
        'priority': 'u=1, i',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"124.0.6367.119"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'action': 'checkNewMailUser',
        'ip': '126.77.16.16',
        'nopost': '1',
        'csrf_token_check': '3f1baba6c7387d3ebf7fb02eec7916c6',
        'csrf_subtoken_check': '9f2c487a7d958a438f8e0627dee4de84',
        'newdomain': 'uma3.be',
        'newuser': '',
        '_': '1714815513903',
    }

    response = requests.get('https://m.kuku.lu/index.php', params=params, cookies=cookies, headers=headers)

    if response.status_code==200:
        third()

def third():
    cookies = {
        'cf_clearance': 'HUaMQQIJAX9fEQYM3LL0p2.NuAzj4A_j.h08L0tObIc-1714815507-1.0.1.1-XSBvjSdtSfPXOluPQUWAaOmhHYGY4Ook_KPVoKe7bx0Gb_vXMu9OSwBUFk7Vx.dQoSvaQqZyvW6GJI22XMku8Q',
        'cookie_keepalive_insert': '1',
        '_ga': 'GA1.1.787201487.1714815511',
        'cookie_failedSlot': '',
        'cookie_last_page_addrlist': '0',
        'cookie_timezone': 'Asia%2FTokyo',
        '__gads': 'ID=90733eca8951ceeb:T=1714815509:RT=1714815509:S=ALNI_MYyYCbJ0BBVskzhvKcfVN-ASOJjFA',
        '__gpi': 'UID=00000e0b78463fe0:T=1714815509:RT=1714815509:S=ALNI_MYdmr4CJtJBpSAY0Hzwn_7_4Thp-w',
        '__eoi': 'ID=f0b870e0740bb736:T=1714815509:RT=1714815509:S=AA-AfjZQHz458_ws6wo9hI7H1b4S',
        'cookie_csrf_token': '3f1baba6c7387d3ebf7fb02eec7916c6',
        'cookie_sessionhash': 'SHASH%3A402b8bfeae143f7130cdd6053bd827ed',
        '_ga_HMG13DJCGJ': 'GS1.1.1714815510.1.1.1714815514.0.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja',
        'priority': 'u=1, i',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"124.0.6367.119"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'action': 'addMailAddrByManual',
        'nopost': '1',
        'by_system': '1',
        't': '1714815512',
        'csrf_token_check': '3f1baba6c7387d3ebf7fb02eec7916c6',
        'newdomain': 'uma3.be',
        'newuser': '',
        'recaptcha_token': '',
        '_': '1714815513904',
    }

    response = requests.get('https://m.kuku.lu/index.php', params=params, cookies=cookies, headers=headers)

    if response.status_code==200:
        acc = response.text.replace('OK:', '')
        if acc=='NG:メールアドレスの最大数を超過しました。不要なメールアドレスの削除をお願いします。':
            print('Rate Limited!')
            return False
        print(f'Generated {acc}')
        f = open("accounts.txt", "a")
        f.write(f"{acc}\n")

threads = []
for _ in range(30):
    thread = threading.Thread(target=first)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()