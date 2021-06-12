import requests
from xml.etree import ElementTree
from rssparser.get_args import get_args
from rssparser.rss_to_json import rss_to_json
from rssparser.print_rss_item import print_rss_item, print_child_exept_items
from rssparser.get_rss_items import get_rss_items, get_child_exept_items


def getNewsText(url):
    response = requests.get(url)
    return response.text


def getRssTree(text):
    return ElementTree.fromstring(text)


def main():
    args = get_args()

    if not args.source:
        print(args.version)
        # sys.stdout.write(str(args))
    else:
        textNews = getNewsText(args.source)
        tree = getRssTree(textNews)
        childExeptItems = get_child_exept_items(tree)
        items = get_rss_items(tree, args.limit)

        if args.json:
            rss_to_json(childExeptItems, items)
        else:
            print_child_exept_items(childExeptItems)

            for item in items:
                print_rss_item(item)


if __name__ == '__main__':
    main()
