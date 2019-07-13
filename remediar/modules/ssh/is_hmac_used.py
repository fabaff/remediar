"""Support for getting details about the used MAC ciphers of a SSH server."""
from remediar.helper import Check
from ..ssh import SshRawClient


class CheckSshIsHmacUsed(Check):
    """Representation of a check for MAC ciphers of a SSH server."""

    def __init__(self, server, **kwargs):
        """Initialize the check."""
        self._server = server
        if kwargs:
            self._port = kwargs['port'] or 22
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
        if self._output:
            return True
        elif self._output is False or not self._output:
            return False
        else:
            return None

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return self._output

    def run_check(self):
        """Run the check."""
        ssh_client = SshRawClient(self._server, self._port)
        ssh_client.get_data()

        if ssh_client.weak_macs is None:
            self._output = False
            return

        self._output = ", ".join(ssh_client.weak_macs)
