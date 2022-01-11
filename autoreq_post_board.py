import requests
import json
import pprint

headers={
    "content-type":"application/json",
    "Authorization" : "JWT ..."
}

url = "http://wafl.shop/api/v1/" \
    + "board/"

for i in range(1,21):
    data = {
        "university" : "연세대학교",
        "allow_anonymous": True,
        "description": f"와플게시판{i}",
        "name": f"와플게시판 {i}번째 입니다. 연세대학교",
        "type": "5"
    }

    response = requests.post(
        url=url, 
        json=data, 
        headers=headers)
    response.encoding = "utf8"

    json_data = json.loads(response.text)
    pprint.pprint(json_data)
