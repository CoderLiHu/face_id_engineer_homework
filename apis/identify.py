import base64

from apis.client import client
from apis.utils import read_file

imageType = "BASE64"

groupIdList = "group1"
# image = 'D:/py/face_id/statics/hahaha.jpg'
# # b64encode函数的参数为byte类型，所以'rb'方式读取文件
# file_content = read_file(image)
# file_content = base64.b64encode(file_content)
# if isinstance(file_content, bytes):
#     file_content = str(file_content, encoding='utf-8')
#
# """ 调用人脸搜索 """
# result = client.search(file_content, imageType, groupIdList);

# print(result)
def identify(img):
    file_content = read_file(img)
    file_content = base64.b64encode(file_content)
    if isinstance(file_content, bytes):
        file_content = str(file_content, encoding='utf-8')

    """ 调用人脸搜索 """
    result = client.search(file_content, imageType, groupIdList);
    result = result['result']['user_list'][0]
    result = result['user_info']
    return '热烈欢迎' + result
    print(result)