"""Constants for remediar."""
from cement.utils.version import get_version_banner
from .core.version import get_version

VERSION_BANNER = """
Remediar %s
""" % (
    get_version(),
)

RUN_BANNER = """
    +---+
 -->|   |---> x     Remediar %s
    |   |---> o     
    +---+

Track your issues and vulnerabilities!
""" % (
    get_version(),
)

VERSION_BANNER = """
Details:
%s
""" % (
    get_version_banner(),
)

HEADERS = ["target", "group", "check", "result", "output"]
