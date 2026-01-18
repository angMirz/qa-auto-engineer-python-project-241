import json
from pathlib import Path

import yaml


def get_format(path):
    return Path(path).suffix.lstrip('.')


def parse_file(filepath):
    file_format = get_format(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if file_format == 'json':
        return json.loads(content)
    if file_format in ('yml', 'yaml'):
        return yaml.safe_load(content)

    raise ValueError(f'Unknown file format: {file_format}')
