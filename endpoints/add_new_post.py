import requests
import json


class CreateNewPost:
    title = None
    body = None
    user_id = None
    status = None
    post_id = None

    def create_new_post(self, title, body, userId):
        url = "https://jsonplaceholder.typicode.com/posts"
        payload = json.dumps({
            "title": title,
            "body": body,
            "userId": userId,
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        self.title = data['title']
        self.body = data['body']
        self.user_id = data['userId']
        self.post_id = data['id']
        self.status = response.status_code
        return response


    def check_new_post_by_title(self, title):
        return self.title == title

    def check_new_post_by_body(self, body):
        return self.body == body

    def check_new_post_by_user_id(self, user_id):
        return self.user_id == user_id

    def check_responce_status_is_ok(self):
        return self.status == 200

    def delete_created_post(self, post_id):
        url = "https://jsonplaceholder.typicode.com/posts/" + post_id
        payload = {}
        headers = {}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response
