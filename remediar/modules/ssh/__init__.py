"""Support for handling SSH connections."""
import paramiko


class SshClient:
    """Wrapper for the SSH connection."""

    def __init__(self, server, port):
        """Initialize the SSH client."""
        self._server = server
        self._port = port
        self.remote_version = None
        self.remote_cipher = None
        self.remote_mac = None
        self.connect()

    def connect(self):
        """Create a connection to the remote server."""
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(
                self._server, port=self._port, username='username',
                password='not-a-valid-password-on-purpose', allow_agent=False,
                look_for_keys=False, timeout=5)
        except (paramiko.ssh_exception.SSHException,
                paramiko.ssh_exception.NoValidConnectionsError):
            self.remote_version = client._transport.remote_version
            self.remote_cipher = client._transport.remote_cipher
            self.remote_mac = client._transport.remote_mac
        client.close()
