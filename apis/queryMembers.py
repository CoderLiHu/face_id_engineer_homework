import time

from apis import delUser
from config import *
from apis.client import client

def getAllUsers():
    """ 调用获取用户列表 """
    result = client.getGroupUsers(groupId)
    result_for_fe =[]
    if result['error_msg'] == 'SUCCESS':
        result = result['result']['user_id_list']
        # for singleResult in result :
            # delUser.delUser(singleResult)
            # try:
            #     user_info = client.getUser(user_id=singleResult,group_id=groupId)
            #     # user_info = client.getUser(user_id='dd,ddf',group_id=groupId)
            #     user_info_new = user_info['result']['user_list'][0]
            #     user_name = user_info_new['user_info']
            #     if user_name != '':
            #         singleResult = user_name
            #     # time.sleep(0.1)
            # except Exception as e:
            #     # e.with_traceback()
            #     i = 1
            # finally:
            #     result_for_fe.append(singleResult)
    else:
        result_for_fe = '出现错误请重试'
    return result
getAllUsers()