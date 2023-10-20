import requests
import json


class ChangeNewPostPatch:
    title = None
    body = None
    user_id = None
    status = None
    post_id = None
    new_body = None

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

    def patch_changes_into_post(self, new_body, post_id):
        url = "https://jsonplaceholder.typicode.com/posts/" + post_id

        payload = json.dumps({
            "body": new_body
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("PUT", url, headers=headers, data=payload)
        data = response.json()
        self.new_body = data['body']
        self.status = response.status_code
        return response

    def check_patching_post_by_body(self, new_body):
        return self.new_body == new_body

    def check_responce_status_is_ok(self):
        return self.status == 200

    def delete_created_post(self, post_id):
        url = "https://jsonplaceholder.typicode.com/posts/" + post_id
        payload = {}
        headers = {}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response
