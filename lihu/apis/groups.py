from apis.client import client

if __name__ == '__main__':
    # result = client.groupAdd('group1')
    # result = client.getGroupUsers('group1')
    result = client.getGroupList()
    print(result)