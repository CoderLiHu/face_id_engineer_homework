from PyQt5 import QtCore, QtMultimedia
from apis.client import client_audio
import asyncio

async def createMP3(text):
    result  = client_audio.synthesis(text, 'zh', 1, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(r'D:\myPython\face_id_engineer_homework\statics\auido.mp3', 'wb') as f:
            f.write(result)

async def speak(text):
    await createMP3(text)
    url = QtCore.QUrl.fromLocalFile(
        r"D:\myPython\face_id_engineer_homework\statics\auido.mp3")
    content = QtMultimedia.QMediaContent(url)
    player = QtMultimedia.QMediaPlayer()
    player.setMedia(content)
    player.setVolume(50.0)
    player.play()