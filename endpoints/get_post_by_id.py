import requests
import json


class GetPostById:
    title = None
    body = None
    user_id = None
    status = None
    post_id = None

    def get_post_by_id(self, post_id):
        url = "https://jsonplaceholder.typicode.com/posts/" + post_id
        payload = {}
        headers = {}
        response = requests.request("Get", url, headers=headers, data=payload)
        data = response.json()
        self.title = data['title']
        self.body = data['body']
        self.user_id = data['userId']
        self.post_id = data['id']
        self.status = response.status_code
        return response

    def check_post_by_title(self, title):
        return self.title == title

    def check_post_by_body(self, body):
        return self.body == body

    def check_post_by_user_id(self, user_id):
        return self.user_id == user_id

    def check_responce_status_is_ok(self):
        return self.status == 200
