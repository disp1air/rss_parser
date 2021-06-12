import argparse


def getArgs():
    parser = argparse.ArgumentParser(
        description='Pure Python command-line RSS reader.')
    parser.add_argument(
        'source', type=str, nargs='?', default=None, help='RSS URL')
    parser.add_argument(
        '--version',
        type=str, nargs='?', const='Version 1.0', help='Print version info')
    parser.add_argument(
        '--json',
        type=bool,
        nargs='?', const=True, help='Print result as JSON in stdout')
    parser.add_argument(
        '--limit',
        type=int, help='Limit news topics if this parameter provided')
    parser.add_argument(
        '--verbose', type=bool, help='Outputs verbose status messages')

    args = parser.parse_args()
    # print(args)
    # sys.stdout.write(str(args))
    return args
