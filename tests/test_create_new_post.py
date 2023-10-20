def test_create_new_post(post_creator):

    title = "Irina's Post"
    body = "Creating new post by Irina Elf"
    user_id = 312
    post_creator.create_new_post(title, body, user_id)
    post_creator.check_responce_status_is_ok()
    post_creator.check_new_post_by_title(title)
    post_creator.check_new_post_by_user_id(user_id)
    post_creator.check_new_post_by_body(body)


