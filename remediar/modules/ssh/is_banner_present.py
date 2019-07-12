"""Support for getting the service banner of a SSH server."""
from remediar.helper import Check
from ..ssh import SshClient


class CheckSshIsBannerPresent(Check):
    """Representation of a SSH banner check."""

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
        ssh_client = SshClient(self._server, self._port)

        if ssh_client.remote_version:
            self._output = ssh_client.remote_version
        else:
            self._output = False
