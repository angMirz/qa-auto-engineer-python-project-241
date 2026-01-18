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


@pytest.fixture
def file1_yaml_path():
    return os.path.join(TEST_DATA_DIR, 'filepath1.yml')


@pytest.fixture
def file2_yaml_path():
    return os.path.join(TEST_DATA_DIR, 'filepath2.yml')


# Функция для чтения содержимого файла
def read_expected_diff(filename):
    with open(
        os.path.join(TEST_DATA_DIR, filename), 'r', encoding='utf-8'
    ) as f:
        return f.read().strip()  # Убираем лишние пробелы в начале и конце


# Нормаk-ем строки по отдел-сти : разбиваем на строки, убираем у каждой пробелы
def normalize(diff: str) -> list[str]:
    return [line.strip() for line in diff.splitlines() if line.strip()]


def test_generate_diff(file1_path, file2_path):
    expected_diff = read_expected_diff('expected_diff.txt')

    result = generate_diff(file1_path, file2_path)
    assert result == expected_diff


def test_generate_diff_identical_files(file1_path):
    """Тест на одинаковые файлы (нет изменений)."""
    result = generate_diff(file1_path, file1_path)
    expected_diff = """{
  host: hexlet.io
  timeout: 50
  proxy: 123.234.53.22
  follow: false
    }""".strip()

    assert sorted(normalize(result)) == sorted(normalize(expected_diff))


def test_generate_diff_missing_key_in_file1(file1_path, file2_path):
    """Тест на отсутствие ключей, которых нет во втором файле, но есть в первом
    сравниванием file1 c file2"""
    expected_diff = """{
  host: hexlet.io
- timeout: 50
- proxy: 123.234.53.22
- follow: false
+ timeout: 20
+ verbose: true
    }""".strip()

    result = generate_diff(file1_path, file2_path)
    assert sorted(normalize(result)) == sorted(normalize(expected_diff))


def test_generate_diff_missing_key_in_file2(file2_path, file1_path):
    """Тест на отсутствие ключей, которых нет в первом файле, но есть во втором
    сравниванием file2 c file1"""
    expected_diff = """{
  host: hexlet.io
- timeout: 20
+ timeout: 50
+ proxy: 123.234.53.22
+ follow: false
- verbose: true
    }""".strip()

    result = generate_diff(file2_path, file1_path)
    assert sorted(normalize(result)) == sorted(normalize(expected_diff))


def test_generate_diff_yaml(file1_yaml_path, file2_yaml_path):
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(file1_yaml_path, file2_yaml_path) == expected
