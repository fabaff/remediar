"""Helper to handle the checks."""
import importlib


def get_check(check_group, check_type):
    """Get the check class."""
    check_module = importlib.import_module(
        "remediar.modules.{}.{}".format(check_group, check_type)
    )
    check_class_name = "Check{}{}".format(
        check_group.capitalize(), check_type.title().replace("_", "")
    )
    CheckClass = getattr(check_module, check_class_name)

    return CheckClass
