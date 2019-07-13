"""Support for getting details about the compression of a SSH server."""
from remediar.helper import Check
from ..ssh import SshClient, SshRawClient

import sys
import socket


class CheckSshIsCompressionPresent(Check):
    """Representation of a check for server-side SSH compression."""

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
        return self._output

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return self._output

    def run_check(self):
        """Run the check."""
        ssh_client = SshRawClient(self._server, self._port)
        ssh_client.get_data()

        if ssh_client.compression is None:
            self._output = False
            return

        self._output = ssh_client.compression
