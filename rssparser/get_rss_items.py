def get_rss_items(rss_tree):
    # get the rss tag from a rss_tree
    channel = rss_tree[0]
    items = []

    for item in channel:
        if item.tag == 'item':
            items.append(item)

    return items
