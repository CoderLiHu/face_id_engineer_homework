import json
import base64
from config import *
from urllib.parse import urlencode
from apis.utils import addToken,request,read_file


def gettext(text):
    return text
def test_face(faceurl):
    result = ''
    url = addToken(FACE_DETECT)
    file_content = read_file(faceurl)
    response = request(url, urlencode(
    {
        'image': base64.b64encode(file_content),
        'image_type': 'BASE64',
        'face_field': 'gender,age',
        'max_face_num': 10
    }))

    data = json.loads(response)
    num = 65;

    if data["error_code"] == 0:
        face_num = data["result"]["face_num"]
        if face_num == 0:
            # could not find face
            result = result + gettext("no face in the picture")
        else:
            # get face list
            face_list = data["result"]["face_list"]
            for face in face_list:
                # male face
                if face["gender"]["type"] == "male":
                    gender = "男"
                # female face
                if face["gender"]["type"] == "female":
                    gender = "女"

                result = result + gettext("顾客" + chr(num))
                result = result + gettext("   性别: " + gender + " 年龄: " + str(face["age"]))
                num = num + 1

    else:
        # print error response
        result = result + gettext(response)

    return result