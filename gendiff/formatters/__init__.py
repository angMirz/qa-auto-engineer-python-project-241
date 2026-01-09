from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def get_formatter(name):
    if name == 'stylish':
        return format_stylish
    if name == 'plain':
        return format_plain
    if name == 'json':
        return format_json

    raise ValueError(f'Unknown format: {name}')

