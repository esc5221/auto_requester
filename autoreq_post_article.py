import requests
import json
import pprint

headers={
    "content-type":"application/json",
    "Authorization" : "JWT ..."
}

url = "http://wafl.shop/api/v1/" \
    + "board/1/article/"

for i in range(1,60):
    data = {
        'is_anonymous': True,
        'is_question': False,
        'text': f"제목 {i}입니다.",
        'title': f"내용 {i}입니다. 서울대학교 자유게시판에 글을 썼습니다."
    }

    response = requests.post(
        url=url, 
        json=data, 
        headers=headers)
    response.encoding = "utf8"

    #response = requests.get("http://wafl.shop/api/v1/my/")
    json_data = json.loads(response.text)
    pprint.pprint(json_data)
