"""Support for checking if a TCP port is using TLS."""
import socket
import ssl

from remediar.helper import Check


class CheckTcpIsTlsUsed(Check):
    """Representation of a check for open TCP port is using TLS."""

    def __init__(self, server, **kwargs):
        """Initialize the check."""
        self._server = server
        if kwargs:
            self._port = kwargs["port"]
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
        """Check if a TCP port is using TLS."""
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        try:
            with socket.create_connection((self._server, self._port), 5) as sock:
                with context.wrap_socket(sock, server_hostname=self._server) as ssock:
                    self._output = ssock.version()

        except socket.timeout:
            self._output = False
