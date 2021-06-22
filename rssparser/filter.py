from datetime import datetime


def filter_by_date(list, requested_date):
    result = []

    for item in list:
        if isinstance(item, dict) and item.get('pubDate'):
            date_obj = datetime.strptime(
                item.get('pubDate'),
                '%Y-%m-%dT%H:%M:%SZ'
            )

            if requested_date == date_obj.date().strftime('%Y%m%d'):
                result.append(item)

    return result


def filter_by_limit(list, limit):
    return list[:limit]
