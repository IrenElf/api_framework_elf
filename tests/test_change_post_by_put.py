def test_change_post_by_put(changer_by_put):

    title = "Updated Post"
    body = "Changing post by Irina Elf"
    user_id = 1
    changer_by_put.create_new_post(title, body, user_id)
    changer_by_put.check_responce_status_is_ok()
    changer_by_put.check_putting_post_by_user_id(user_id)
    changer_by_put.check_putting_post_by_body(body)
    changer_by_put.check_putting_post_by_title(title)
