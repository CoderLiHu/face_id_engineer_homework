import base64
import json

from apis.client import client
from apis.utils import read_file



imageType = "BASE64"

groupId = "group1"


# """ 调用人脸注册 """
# client.addUser(image, imageType, groupId, userId);

""" 如果有可选参数 """
# options = {}
# options["user_info"] = "user's info"
# options["quality_control"] = "NORMAL"
# options["liveness_control"] = "LOW"
# options["action_type"] = "REPLACE"

""" 带参数调用人脸注册 """
# client.addUser(image, imageType, groupId, userId, options)


def addUser(image,userID,userName):
    options = {}
    options["user_info"] = userName.encode('utf-8').decode('latin-1')
    """ 调用创建用户组 """
    # await client.groupAdd(groupId);
    # image = 'D:/py/face_id/statics/hahaha.jpg'
    # b64encode函数的参数为byte类型，所以'rb'方式读取文件
    file_content = read_file(image)
    file_content = base64.b64encode(file_content)
    if isinstance(file_content, bytes):
        file_content = str(file_content, encoding='utf-8')
    result = client.addUser(file_content, imageType, groupId, userID,options)

    msg = result["error_msg"]
    if msg == "SUCCESS":
        text = "欢迎加入," + userName + "!!!"
    elif msg == 'face is already exist':
        text = '库中存在该脸，请勿重复添加'
    else :
        text = '添加失败，请重试' + msg
    # print(type(result))
    return text

if __name__ == '__main__':
    result = addUser('','group2')
    # print(result)
