from config import  *
from apis.client import client


""" 调用用户信息查询 """
def queryMember(userId):
    result = client.getUser(userId, groupId);
    if result['error_msg'] == 'SUCCESS':
        result = result['result']['user_list'][0]
        result = result['user_info'] + "__" + userId
    elif result['error_msg'] == 'user is not exist':
        result = '用户不存在'
    else:
        result = '出现错误请重试'
    return result

""" 删除用户 """
def delUser(userId):
    result = client.deleteUser(groupId, userId);
    if result['error_msg'] == "SUCCESS":
        result = '已删除' + userId + '用户'
    else:
        result = result['error_msg']
    return result