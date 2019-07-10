"""Support for checking TCP port."""
import socket

from remediar.helper import Check


class CheckTcpIsPortOpen(Check):
    """Representation of a check for an open TCP port."""

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
    def result(self) -> str:
        """Return the state of the entity."""
        return self._output

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return (
            "Port {} open".format(self._port)
            if self._output is True
            else "Port {} closed".format(self._port)
        )

    def run_check(self):
        """Check if a TCP port is open."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self._server, int(self._port)))
            self._output = True
        except socket.error:
            self._output = False
        except OverflowError:
            self._output = False
