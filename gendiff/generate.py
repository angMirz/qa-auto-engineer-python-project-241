import json


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_diff(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)
    keys = sorted(set(data1) | set(data2))
    lines = []

    for key in keys:
        if key not in data1:
            lines.append(f"+ {key}: {data2[key]}")
        elif key not in data2:
            lines.append(f"- {key}: {data1[key]}")
        elif data1[key] != data2[key]:
            lines.append(f"- {key}: {data1[key]}")
            lines.append(f"+ {key}: {data2[key]}")
        else:
            lines.append(f"  {key}: {data1[key]}") 

    return "\n".join(lines)
