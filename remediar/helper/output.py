"""Helper for the output."""


def add_row(rows, target, group, check, result):
    """Format a single row for the output."""
    if result.result is True:
        _result = True
    elif result.result is False:
        _result = False
    else:
        _result = "-"

    if isinstance(result.output, str):
        output = result.output
    elif result.output is False:
        output = "-"
    elif result.output is True:
        output = True
    else:
        output = "Not checked!"

    rows.append([target, group, check, _result, output])
