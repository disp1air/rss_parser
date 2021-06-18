import json
import pickle


def rss_to_json(child_exept_items, items):
    result_dict = rss_to_dict(child_exept_items, items)
    store_data(result_dict)
    json_object = json.dumps(result_dict, indent=4)
    print(json_object)


def rss_to_dict(child_exept_items, items):
    result = {}

    for child in child_exept_items:
        if (child.text and child.text.rstrip()):
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
    with open("dict.pickle", "wb") as file:
        pickle.dump(data, file)
