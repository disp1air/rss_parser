def print_verbose(items):
    for item in items:
        for key, value in item.items():
            print(f'{key}: {value}')
        print('===================================')
