import json


def rss_to_json(child_exept_items, items):
    resultDict = {}

    for child in child_exept_items:
        if (child.text and child.text.rstrip()):
            resultDict[child.tag] = child.text
        else:
            resultDict[child.tag] = {}
            for i in child:
                resultDict[child.tag][i.tag] = i.text

    for index, item in enumerate(items):
        resultDict[f'item{index}'] = {}
        for i in item:
            resultDict[f'item{index}'][i.tag] = i.text if i.text else ''

    json_object = json.dumps(resultDict, indent=4)
    print(json_object)
