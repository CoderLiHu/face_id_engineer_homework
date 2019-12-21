from PyQt5 import QtCore, QtMultimedia
from apis.client import client_audio
from config import mp3_url

async def createMP3(text):
    result  = client_audio.synthesis(text, 'zh', 1, {
        'vol': 5,
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(mp3_url, 'wb') as f:
            f.write(result)

async def speak(player,text):
    await createMP3(text)
    url = QtCore.QUrl.fromLocalFile(mp3_url)
    content = QtMultimedia.QMediaContent(url)
    player.setMedia(content)
    player.setVolume(90.0)
    player.play()
