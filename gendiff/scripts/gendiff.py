import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description='Compares two configuration files and shows a difference.',
        # formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-f', '--format', 
        # metavar='FORMAT', 
        help='set format of output'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()

    # print(f"Compare two configuration files {args.first_file} and {args.second_file}")

    output = generate_diff(args.first_file, args.second_file)
    print(output)


if __name__ == '__main__':
    main()