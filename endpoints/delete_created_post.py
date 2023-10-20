import requests
import json

class DeletePost:
    title = None
    body = None
    user_id = None
    status = None
    post_id = None
    new_body = None
    data = None

    def create_new_post(self, title, body, user_id):
        url = "https://jsonplaceholder.typicode.com/posts"
        payload = json.dumps({
            "title": title,
            "body": body,
            "userId": user_id,
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        self.post_id = data['id']
        return response

    def delete_created_post(self, post_id):
        url = "https://jsonplaceholder.typicode.com/posts/" + post_id
        payload = {}
        headers = {}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response

    def delete_by_id(self, post_id):
        url = "https://jsonplaceholder.typicode.com/posts/" + post_id
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.data = response.json()
        return self.data

    def check_delete_post(self, deleted_post):
        return self.data == deleted_post

