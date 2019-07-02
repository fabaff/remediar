"""The version helper of Remediar."""
from cement.utils.version import get_version as cement_get_version

VERSION = (0, 0, 1, 'alpha', 0)


def get_version(version=VERSION):
    """Return the current version."""
    return cement_get_version(version)
