from aip import AipFace
from config import *

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 建立连接的超时时间（单位：毫秒)
# client.setConnectionTimeoutInMillis()

# 通过打开的连接传输数据的超时时间（单位：毫秒）
# client.setSocketTimeoutInMillis()
from aip import AipSpeech
client_audio = AipSpeech(APP_ID, API_KEY, SECRET_KEY)