import re
import sys
import json
import requests
from xml.etree import ElementTree
from rssparser.get_args import get_args
from rssparser.rss_to_json import to_json, to_html, to_pdf
from rssparser.get_rss_items import get_rss_items
from rssparser.filter_data import filter_by_date, filter_by_limit


def get_data_from_non_local(url):
    response = requests.get(url)
    tree = ElementTree.fromstring(response.text)
    items = get_rss_items(tree)
    items_list = rss_items_to_list(items)
    store_data_to_local(items_list)
    return items_list


def store_data_to_local(data):
    with open('rssparser/data/store.txt', 'w') as ff:
        ff.write(json.dumps(data))


def get_data_from_local():
    with open('rssparser/data/store.txt') as f:
        data = f.read()
    return json.loads(data)


def rss_items_to_list(list_of_items):
    result = []
    for item in list_of_items:
        parsed_item = item_to_dict(item)
        result.append(parsed_item)
    return result


def item_to_dict(item):
    result_item = {}

    for element in item:
        if element.tag and element.text:
            if re.match(r'\s*{.*}\s*', element.tag):
                result_item[re.sub(r'\s*{.*}\s*', '', element.tag)] = element.text
            else:
                result_item[element.tag] = element.text
        if element.attrib:
            result_item[f'{element.tag}_attrib'] = {}
            for attrib in element.attrib:
                result_item[f'{element.tag}_attrib'][attrib] = element.attrib[attrib]

    return result_item


def print_verbose(items):
    for item in items:
        for key, value in item.items():
            print(f'{key}: {value}')
        print('===================================')


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
