import json


def rss_to_json(items):
    resultDict = {}

    for index, item in enumerate(items):
        resultDict[f'item{index}'] = {}
        for i in item:
            resultDict[f'item{index}'][i.tag] = i.text if i.text else ''

    json_object = json.dumps(resultDict, indent=4)
    print(json_object)
