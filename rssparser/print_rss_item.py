def print_rss_item(rss_item):
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


def print_child_exept_items(child_exept_items):
    for child in child_exept_items:
        if (child.text.rstrip()):
            print(f'{child.tag}: {child.text}')
        else:
            print(child.tag)
            for i in child:
                print(f'    {i.tag}: {i.text}')
    # just to add a separator before the first item
    print('=============================================')
