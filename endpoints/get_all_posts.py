import requests
import json


class GetAllPosts:
    title = None
    body = None
    user_id = None
    status = None
    post_id = None

    def get_post_by_id(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        payload = {}
        headers = {}
        response = requests.request("Get", url, headers=headers, data=payload)
        data = response.json()
        self.status = response.status_code
        return response

    def check_responce_status_is_ok(self):
        return self.status == 200
