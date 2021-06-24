import os
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
    html_header = '''<!DOCTYPE html><html lang="en"><head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head><body>'''

    for item in items:
        for k, v in item.items():
            if k and v and isinstance(v, str):
                if k == 'link':
                    result_str += f'<a href="{v}">Related link</a>'
                else:
                    result_str += f'<p style="margin:0"><b>{k}</b>: {v}</p>'
            if k and v and isinstance(v, dict):
                for key, value in v.items():
                    if key == 'url' and k != 'source_attrib':
                        result_str += f'<img src="{value}">'
                    else:
                        result_str += f'<p style="margin:0"><b>{key}</b>: {value}</p>'

    html_bottom = '''</body></html>'''

    with open(path_to_save_html, 'w') as ff:
        ff.write(html_header)
        ff.write(result_str)
        ff.write(html_bottom)


def to_pdf(items, path_to_save_pdf):
    to_html(items, 'rssparser/data/html_to_pdf.html')
    pdfkit.from_file('rssparser/data/html_to_pdf.html', path_to_save_pdf)
    os.remove('rssparser/data/html_to_pdf.html')
