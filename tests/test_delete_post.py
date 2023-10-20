def test_change_post_by_put(post_deletor):

    title = "Updated Post"
    body = "Changing post by Irina Elf"
    user_id = 1
    deleted_post = ''

    post_deletor.create_new_post(title, body, user_id)
    post_deletor.check_delete_post(deleted_post)
