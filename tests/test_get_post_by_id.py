
def test_get_post_by_id(get_post_by_id):
    post_id = '10'
    user_id = 1
    body = "optio molestias id quia eum"
    title = "quo et expedita modi cum officia vel magni\n" \
            "doloribus qui repudiandae\n" \
            "vero nisi sit\n" \
            "uos veniam quod sed accusamus veritatis error"

    get_post_by_id.get_post_by_id(post_id)
    get_post_by_id.check_post_by_user_id(user_id)
    get_post_by_id.check_post_by_body(body)
    get_post_by_id.check_post_by_title(title)
    get_post_by_id.check_responce_status_is_ok()