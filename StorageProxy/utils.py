def get_page_num_and_size(get_params, default_page_num, default_page_size):
    try:
        page_num = int(get_params.get('page_num', ''))
    except ValueError:
        page_num = default_page_num
    try:
        page_size = int(get_params.get('page_size', ''))
    except ValueError:
        page_size = default_page_size
    return (page_num, page_size)
