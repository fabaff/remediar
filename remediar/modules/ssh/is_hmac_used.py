"""Support for getting the service banner of a SSH server."""
from remediar.helper import Check
from ..ssh import SshClient


class CheckSshIsHmacUsed(Check):
    """Representation of a HTTP banner check."""

    def __init__(self, server, port):
        """Initialize the check."""
        self._server = server
        self._port = port
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
        return True if self._output is not False else False

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return self._output

    def run_check(self):
        """Run the check."""
        ssh_client = SshClient(self._server, self._port)

        if "hmac-md5" in ssh_client.remote_cipher:
            self._output = "HMAC is used"
        else:
            self._output = False