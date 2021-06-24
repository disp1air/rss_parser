import sys
import requests
from xml.etree import ElementTree
from rssparser.get_args import get_args
from rssparser.convert_module import rss_items_to_list, to_json, to_html, to_pdf
from rssparser.get_rss_items import get_rss_items
from rssparser.filter_data import filter_by_date, filter_by_limit
from rssparser.verbose_module import print_verbose
from rssparser.store_module import store_data_to_local, get_data_from_local


def get_data_from_non_local(url):
    response = requests.get(url)
    tree = ElementTree.fromstring(response.text)
    items = get_rss_items(tree)
    items_list = rss_items_to_list(items)
    store_data_to_local(items_list)
    return items_list


def main():
    args = get_args()

    if args.version:
        sys.exit(args.version)
    if args.source:
        items_list = get_data_from_non_local(args.source)
    else:
        items_list = get_data_from_local()

    if args.date:
        items_list = filter_by_date(items_list, args.date)
    if args.limit:
        items_list = filter_by_limit(items_list, args.limit)
    if args.json:
        to_json(items_list)
    if args.verbose:
        print_verbose(items_list)
    if args.to_html:
        to_html(items_list)
    if args.to_pdf:
        to_pdf(items_list)


if __name__ == '__main__':
    main()
