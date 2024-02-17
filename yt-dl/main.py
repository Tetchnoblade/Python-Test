from yt_dlp import YoutubeDL

input_url = str(input('URL: '))

config = {
    'format' : 'bestvideo+bestaudio/best'
}

try:
    with YoutubeDL(config) as ydl:
        request = ydl.download([input_url])
    print('Success')
except:
    print('Failed')