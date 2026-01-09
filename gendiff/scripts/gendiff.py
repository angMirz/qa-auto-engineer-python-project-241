import argparse
import os

from gendiff import generate_diff

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TEST_DATA_DIR = os.path.join(PROJECT_ROOT, 'tests', 'test_data')


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument(
        '-f', '--format', 
        default='stylish',
        # metavar='FORMAT', 
        help='set format of output'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()

    # print(f"Compare two configuration files {args.first_file} and {args.second_file}")
    # Всегда берём файлы из tests/test_data
    first_file = os.path.join(TEST_DATA_DIR, args.first_file)
    second_file = os.path.join(TEST_DATA_DIR, args.second_file)

    output = generate_diff(first_file, second_file, args.format)
    print(output)


if __name__ == '__main__':
    main()