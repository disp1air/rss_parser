def get_rss_items(rss_tree, limit):
    # get rss tag
    channel = rss_tree[0]
    all_items = []

    for item in channel:
        if item.tag == 'item':
            all_items.append(item)

    if limit:
        return all_items[:limit]
    else:
        return all_items
