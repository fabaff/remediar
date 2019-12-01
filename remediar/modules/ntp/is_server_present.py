"""Support for getting the time from a NTP server."""
from time import ctime

import ntplib

from remediar.helper import Check


class CheckNtpIsServerPresent(Check):
    """Representation of a NTP server check."""

    def __init__(self, server, **kwargs):
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
        return True if self._output is not None else False

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return self._output

    def run_check(self):
        """Run the check."""
        ntp_client = ntplib.NTPClient()
        try:
            response = ntp_client.request(self._server, version=4)
            self._output = ctime(response.tx_time)
        except ntplib.NTPException:
            self._output = False
