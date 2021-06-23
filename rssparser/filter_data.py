from datetime import datetime


def filter_by_date(list, requested_date):
    result = []

    for item in list:
        if isinstance(item, dict) and item.get('pubDate'):
            date_obj = find_format(item.get('pubDate'))

            if requested_date == date_obj.date().strftime('%Y%m%d'):
                result.append(item)

    return result


def filter_by_limit(list, limit):
    return list[:limit]


def find_format(text):
    for fmt in ('%Y-%m-%dT%H:%M:%SZ', '%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M EDT'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')
