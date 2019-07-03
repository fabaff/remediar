"""Helper for the output."""


def add_row(rows, target, group, check, result):
    """Format a single row for the output."""
    _result = '1' if result.result is True else '0'
    output = '-' if result.output is False else result.output

    rows.append([target, group, check, _result, output])
