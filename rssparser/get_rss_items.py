def get_rss_items(rss_tree, limit):
    # get the rss tag from a rss_tree
    channel = rss_tree[0]
    items = []

    if limit:
        for item in channel:
            if len(items) == limit:
                return items

            if item.tag == 'item':
                items.append(item)
    else:
        for item in channel:
            if item.tag == 'item':
                items.append(item)

    return items
