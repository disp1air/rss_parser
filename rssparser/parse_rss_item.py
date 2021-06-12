def parse_rss_item(rss_item):
    for item_child in rss_item:
        if (item_child.text):
            print(f'{item_child.tag}: {item_child.text}')
        else:
            print(f'{item_child.tag}')

        # attrib
        if (item_child.attrib):
            for k, v in item_child.attrib.items():
                print(f'    {k}: {v}')

    # just to add a separator between items
    print('=============================================')
