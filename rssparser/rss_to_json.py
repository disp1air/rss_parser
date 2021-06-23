import json
import sys
import pdfkit


def to_json(items):
    result_dict = rss_to_dict(items)
    json_object = json.dumps(result_dict, indent=4)
    sys.stdout.write(json_object)


def rss_to_dict(items):
    result = {}

    for index, item in enumerate(items):
        result[f'item{index + 1}'] = {}
        for i in item:
            result[f'item{index + 1}'][i] = item[i]

    return result


def to_html(items, path_to_save_html):
    result_str = ''
    result_dict = rss_to_dict({}, items)
    html_header = '''<!DOCTYPE html><html lang="en"><head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head><body>'''

    for key, value in result_dict.items():
        result_str += f'<h2>{key}</h2>'
        for k, v in value.items():
            if k and v:
                if k == 'link':
                    result_str += f'<a href="{v}">Related link</a>'
                else:
                    result_str += f'<p><b>{k}</b>: {v}</p>'

    html_bottom = '''</body></html>'''

    with open(path_to_save_html, 'w') as ff:
        ff.write(html_header)
        ff.write(result_str)
        ff.write(html_bottom)


def to_pdf(items, path_to_save_pdf):
    result_dict = rss_to_dict({}, items)
    json_object = json.dumps(result_dict, indent=4)
    pdfkit.from_string(json_object, path_to_save_pdf)