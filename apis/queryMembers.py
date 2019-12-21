from config import *
from apis.client import client

def getAllUsers():
    """ 调用获取用户列表 """
    result = client.getGroupUsers(groupId)
    if result['error_msg'] == 'SUCCESS':
        result = result['result']['user_id_list']
    else:
        result = '出现错误请重试'
    return result