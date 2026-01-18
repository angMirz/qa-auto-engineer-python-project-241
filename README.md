### Hexlet tests and linter status:
[![Actions Status](https://github.com/angMirz/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/angMirz/qa-auto-engineer-python-project-241/actions)

### asciinema
[Record1](https://asciinema.org/a/OAysR8222MRv69Cm)
[Record2](https://asciinema.org/a/I4m2JrYbTRTwr378)
[Record3](https://asciinema.org/a/9ck3FSOXKGyIwptG)

### badges
[![hexlet-check](https://github.com/angMirz/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/angMirz/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=angMirz_qa-auto-engineer-python-project-241&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=angMirz_qa-auto-engineer-python-project-241)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=angMirz_qa-auto-engineer-python-project-241&metric=coverage)](https://sonarcloud.io/summary/new_code?id=angMirz_qa-auto-engineer-python-project-241)

## Project structure
**`gendiff/scripts/generate.py`** - функция `generate_diff` формирует структуру различий (diff) между двумя файлами.
**`gendiff/scripts/parser.py`**  - модуль для чтения и парсинга файлов формата json и yml.
**`gendiff/scripts/diff_builder.py`** - модуль для формирования структуры diff между двумя объектами.  
**`gendiff/formatters/..`** - форматеры json, plain, stylish.
**`gendiff/scripts/gendiff.py`** — CLI-скрипт

**`tests/test_data/..`** - тестовые данные.
**`tests/test_genearate.py`** - тесты на генерации.
**`tests/test_format.py`** - тесты на форматы.

### Usage command

Сравнение двух файлов в формате **json** (Сравнение плоских файлов и Вывод в JSON): 
gendiff --format json file1.json file2.json

Сравнение двух файлов в формате **plain** (Плоский формат):
gendiff --format plain file1.json file2.json

Сравнение двух файлов в формате **yml** (Сравнение плоских файлов (yaml)):
gendiff filepath1.yml filepath2.yml
