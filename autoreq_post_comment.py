import requests
import json
import pprint

headers={
    "content-type":"application/json",
    "Authorization" : "JWT ..."
}

# url2 = "http://wafl.shop/api/v1/" \
#     + "board/1/article/59/comment/"

url = "http://localhost:8000/api/v1/" \
    + "board/2/article/5/"

for i in range(1,51):
    data = {
        'text': f"{i}번째 댓글 입니다.",   
        "parent": 0,
        "is_anonymous": False
    }

    response = requests.post(
        url=url, 
        json=data, 
        headers=headers)
    response.encoding = "utf8"

    #response = requests.get("http://wafl.shop/api/v1/my/")
    json_data = json.loads(response.text)
    pprint.pprint(json_data)
