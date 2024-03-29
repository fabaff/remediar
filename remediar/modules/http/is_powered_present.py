"""Support for getting the service banner of a web server."""
import requests
import urllib3

from remediar.helper import Check

urllib3.disable_warnings()


class CheckHttpIsPoweredPresent(Check):
    """Representation of a HTTP banner check."""

    def __init__(self, server, **kwargs):
        """Initialize the check."""
        self._server = server
        if kwargs:
            self._port = kwargs['port']
        self._name = ""
        self._output = None
        self.run_check()

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
            return

        if "X-Powered-By" in response.headers:
            self._output = response.headers["X-Powered-By"]
        else:
            self._output = False
