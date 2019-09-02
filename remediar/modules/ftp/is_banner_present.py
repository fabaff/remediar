"""Support for getting the service banner of a FTP server."""
from remediar.helper import Check


class CheckFtpIsBannerPresent(Check):
    """Representation of a FTP banner check."""

    def __init__(self, server, **kwargs):
        """Initialize the check."""
        self._server = server
        if kwargs:
            self._port = kwargs['port'] or 21
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
        from ftplib import FTP

        try:
            ftp = FTP()
            ftp.connect(host=self._server, port=self._port, timeout=10)
            self._output = ftp.getwelcome()
        except OSError:
            self._output = None
