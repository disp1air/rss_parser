import json
from datetime import datetime

path_to_store = 'rssparser/data/store.json'


def rss_to_json(child_exept_items, items):
    result_dict = rss_to_dict(child_exept_items, items)
    json_object = json.dumps(result_dict, indent=4)
    store_data(json_object)
    print(json_object)


def rss_to_dict(child_exept_items, items):
    result = {}

    for child in child_exept_items:
        if child.text and child.text.rstrip():
            result[child.tag] = child.text
        else:
            result[child.tag] = {}
            for i in child:
                result[child.tag][i.tag] = i.text

    for index, item in enumerate(items):
        result[f'item{index}'] = {}
        for i in item:
            result[f'item{index}'][i.tag] = i.text if i.text else ''

    return result


def store_data(data):
    with open(path_to_store, 'w') as ff:
        ff.write(data)


def fetchDataFromStore(requested_date):
    result = {}

    with open(path_to_store) as f:
        data = json.load(f)

    for key, value in data.items():
        if isinstance(value, dict) and value.get('pubDate'):
            date_obj = datetime.strptime(
                value.get('pubDate'),
                '%a, %d %b %Y %H:%M:%S %z'
            )
            print(date_obj)

            if requested_date == date_obj.date().strftime('%Y%m%d'):
                result[key] = value

    print(result)
