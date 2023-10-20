def test_change_post_by_put(changer_by_patch):

    title = "Updated Post"
    body = "Changing post by Irina Elf"
    user_id = 1
    new_body = "Patching post by Irina Elf"

    changer_by_patch.create_new_post(title, body, user_id)
    changer_by_patch.check_responce_status_is_ok()
    changer_by_patch.check_patching_post_by_body(new_body)
