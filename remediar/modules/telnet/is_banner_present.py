"""Support for getting the service banner of a telnet server."""
import requests
import urllib3

from remediar.helper import Check


class CheckTelnetIsBannerPresent(Check):
    """Representation of a telnet banner check."""

    def __init__(self, server):
        """Initialize the check."""
        self._server = server
        self._name = ""
        self._output = None
        self.run_check()

    @property
    def name(self) -> str:
        """Return the name of the check."""
        return self._name

    @property
    def result(self) -> str:
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
        import telnetlib

        try:
            tn = telnetlib.Telnet(self._server, timeout=5)
            banner_start = tn.read_until(b"\r\n")
            banner_end = tn.read_until(b"\r\n")
            self._output = banner_end.decode('ascii').strip()
        except OSError:
            self._output = None
