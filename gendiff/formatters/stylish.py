def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def format_stylish(diff):
    lines = ['{']

    for key, node in diff.items():
        node_type = node['type']

        if node_type == 'added':
            lines.append(f"  + {key}: {format_value(node['value'])}")
        elif node_type == 'removed':
            lines.append(f"  - {key}: {format_value(node['value'])}")
        elif node_type == 'unchanged':
            lines.append(f"    {key}: {format_value(node['value'])}")
        elif node_type == 'changed':
            lines.append(f"  - {key}: {format_value(node['old_value'])}")
            lines.append(f"  + {key}: {format_value(node['new_value'])}")

    lines.append('}')
    return '\n'.join(lines)
