import json


def store_data_to_local(data):
    with open('rssparser/data/store.txt', 'w') as ff:
        ff.write(json.dumps(data))


def get_data_from_local():
    with open('rssparser/data/store.txt') as f:
        data = f.read()
    return json.loads(data)