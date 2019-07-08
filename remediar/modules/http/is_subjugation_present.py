"""Support for getting the details of a subjugation of a web server.."""
import requests
import urllib3

from remediar.helper import Check

urllib3.disable_warnings()


class CheckHttpIsSubjugationPresent(Check):
    """Representation a HTTP subjugation check."""

    def __init__(self, server):
        """Initialize the check."""
        self._server = server
        self._name = ""
        self._output = None

    @property
    def name(self) -> str:
        """Return the name of the check."""
        return self._name

    @property
    def result(self) -> bool:
        """Return the state of the check."""
        if isinstance(self._output, str):
            return True
        elif self._output is False:
            return False
        else:
            return None

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return self._output

    def run_check(self):
        """Run the check."""
        url = "http://{}".format(self._server)

        try:
            response = requests.head(
                url, allow_redirects=False, verify=False, timeout=5
            )
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.MissingSchema,
        ):
            self._output = None

        if "Location" in response.headers:
            self._output = response.headers["Location"]
        else:
            self._output = False
