import json
from config import *
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode

# skip https auth
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

"""
    get token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)

    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)

    result_str = result_str.decode()
    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

"""
    call remote http server
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)

"""
    read file
"""
def read_file(image_path):
    f = None
    try:
        # rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
        # 这是默认模式。一般用于非文本文件如图片等。
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()

"""
    url add token
"""
def addToken(url):
    # get access token
    token = fetch_token()
    return f'{url}?access_token={token}'