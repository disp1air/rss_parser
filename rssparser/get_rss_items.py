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


def get_child_exept_items(rss_tree):
    channel = rss_tree[0]
    child_exept_items = []

    for child in channel:
        if child.tag != 'item':
            child_exept_items.append(child)

    return child_exept_items
