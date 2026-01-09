import json
import os

import pytest

from gendiff import generate_diff

# Указываем путь до тестовых данных
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


@pytest.fixture
def file1_path():
    return os.path.join(TEST_DATA_DIR, 'file1.json')


@pytest.fixture
def file2_path():
    return os.path.join(TEST_DATA_DIR, 'file2.json')


def test_plain_format(file1_path, file2_path):
    expected = (
        "Property 'follow' was removed\n"
        "Property 'proxy' was removed\n"
        "Property 'timeout' was updated. From 50 to 20\n"
        "Property 'verbose' was added with value: true"
    )

    assert generate_diff(file1_path, file2_path, 'plain') == expected


@pytest.mark.parametrize("format_name", ["stylish", "plain", "json"])
def test_generate_diff_formats(file1_path, file2_path, format_name):
    """
    Проверяем generate_diff для всех поддерживаемых форматов.
    """
    output = generate_diff(file1_path, file2_path, format_name)

    # Проверяем, что вывод не пустой
    assert output
    assert isinstance(output, str)

    # Для json проверяем корректность структуры
    if format_name == "json":
        diff = json.loads(output)
        # Проверяем наличие ключей верхнего уровня
        for key in ["timeout", "proxy", "verbose", "follow", "host", "host"]:
            assert key in diff

        # Проверяем типы изменений
        assert diff["timeout"]["type"] == "changed"
        assert diff["proxy"]["type"] == "removed"
        assert diff["verbose"]["type"] == "added"
