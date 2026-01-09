def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, parent_path=''):
    lines = []

    for key, node in diff.items():
        property_path = f"{parent_path}.{key}" if parent_path else key
        node_type = node['type']

        if node_type == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{property_path}' was added with value: {value}"
            )

        elif node_type == 'removed':
            lines.append(
                f"Property '{property_path}' was removed"
            )

        elif node_type == 'changed':
            old = format_value(node['old_value'])
            new = format_value(node['new_value'])
            lines.append(
                f"Property '{property_path}' was updated. From {old} to {new}"
            )

        elif node_type == 'nested':
            lines.append(
                format_plain(node['children'], property_path)
            )

        # unchanged — игнорируем

    return '\n'.join(filter(None, lines))
