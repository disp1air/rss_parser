import requests
from xml.etree import ElementTree
from rssparser.get_args import getArgs
from rssparser.rss_to_json import rss_to_json
from rssparser.parse_rss_item import parse_rss_item
from rssparser.get_rss_items import get_rss_items


def getNewsText(url):
    response = requests.get(url)
    return response.text


def getRssTree(text):
    return ElementTree.fromstring(text)


def main():
    args = getArgs()
    textNews = getNewsText('https://news.yahoo.com/rss/')
    tree = getRssTree(textNews)
    items = get_rss_items(tree, args.limit)

    if args.json:
        rss_to_json(items)

    for item in items:
        parse_rss_item(item)


if __name__ == '__main__':
    main()
