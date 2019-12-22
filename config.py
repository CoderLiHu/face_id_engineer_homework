import os
import sys

APP_ID = '17944319'
API_KEY = 'HgpWtLlAY4C3iksGMlW3c1R1'
SECRET_KEY = 'ElE92X48cCqLRxUt8nk3HtzEwyFHBu4E'
FACE_DETECT = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
groupId = 'group1'
# root_dir = os.path.dirname(os.path.abspath(__file__))
# mp3_url = root_dir+os.path.join(r'\statics\auido.mp3')
root_dir = os.path.dirname(os.path.realpath(sys.executable))
mp3_url = root_dir+os.path.join(r'\auido.mp3')
