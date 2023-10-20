import pytest
import requests
import json
from endpoints.add_new_post import CreateNewPost
from endpoints.change_post_with_put import ChangeNewPostPut
from endpoints.change_post_with_patch import ChangeNewPostPatch
from endpoints.delete_created_post import DeletePost
from endpoints.get_all_posts import GetAllPosts
from endpoints.get_post_by_id import GetPostById


@pytest.fixture()
def post_creator():
    return CreateNewPost()


@pytest.fixture()
def changer_by_put():
    return ChangeNewPostPut()


@pytest.fixture()
def changer_by_patch():
    return ChangeNewPostPatch()


@pytest.fixture()
def post_deletor():
    return DeletePost()

@pytest.fixture()
def get_all_posts():
    return GetAllPosts()


@pytest.fixture()
def get_post_by_id():
    return GetPostById()