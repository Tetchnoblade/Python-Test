#指定したGitHubリポジトリのReleasesからダウンロード数を取得します

import requests

inputName = str(input('ユーザー名: '))
inputRepo = str(input('レポジトリ名: '))

data = requests.get(f'https://api.github.com/repos/{inputName.lower()}/{inputRepo.lower()}/releases')
counter = 0

if data:
    for i in data.json():
        print(i['name'])
        try:
            print('Downloads:', i["assets"][0]["download_count"])
            counter += i["assets"][0]["download_count"]
        except:
            print('Downloads: NULL')
        print('='*20)
    print('合計:', counter)
    f = open("counts.txt", "a")
    f.write(f"{inputRepo.lower()}: {counter}\n")