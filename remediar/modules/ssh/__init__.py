"""Support for handling SSH connections."""
import socket

import paramiko

from remediar.constants import (
    SSH_CIPHERS, SSH_KEXS, SSH_MACS, SSH_WEAK_CIPHERS, SSH_WEAK_KEXS,
    SSH_WEAK_MACS)


class SshClient:
    """Wrapper for the SSH connection."""

    def __init__(self, server, port):
        """Initialize the SSH client."""
        self._server = server
        self._port = port
        self.remote_version = None
        self.remote_cipher = None
        self.remote_mac = None
        self.login = None
        self.connect()

    def connect(self):
        """Create a connection to the remote server."""
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(
                self._server,
                port=self._port,
                username="username",
                password="not-a-valid-password-on-purpose",
                allow_agent=False,
                look_for_keys=False,
                timeout=10,
            )
        except (paramiko.ssh_exception.NoValidConnectionsError, OSError):
            pass
        except paramiko.ssh_exception.AuthenticationException:
            self.login = False

        try:
            self.remote_version = client._transport.remote_version
            self.remote_cipher = client._transport.remote_cipher
            self.remote_mac = client._transport.remote_mac
            self.login = True
        except AttributeError:
            pass

        client.close()


class SshRawClient:
    """Wrapper for the socket-based SSH connection."""

    def __init__(self, server, port):
        """Initialize the SSH client."""
        self._server = server
        self._port = port
        self.weak_ciphers = None
        self.weak_macs = None
        self.compression = None
        self.weak_kex = None
        self._sock = None
        self._data = None
        self.raw_connect()

    def raw_connect(self):
        """Create a socket connection."""
        try:
            self._sock = socket.create_connection((self._server, self._port), 5)
        except socket.timeout:
            return False
        except socket.error as e:
            if e.errno == 61:
                return None
            else:
                return None

    def get_data(self):
        """Get the data from the SSH server."""
        try:
            self._sock.recv(50).decode("utf-8").split("\n")[0]
        except AttributeError:
            return
        self._sock.send(b"SSH-2.0-remediar\r\n")
        self._data = self._sock.recv(2000)
        self.weak_ciphers = self.parse_elements(
            SSH_CIPHERS, SSH_WEAK_CIPHERS, self._data
        )
        self.weak_macs = self.parse_elements(SSH_MACS, SSH_WEAK_MACS, self._data)
        self.weak_kex = self.parse_elements(SSH_KEXS, SSH_WEAK_KEXS, self._data)
        self.compression = (
            True
            if self._data.decode("utf-8", errors="ignore").rfind("zlib@openssh.com")
            >= 0
            else False
        )

    @staticmethod
    def parse_elements(elements, weak_elements, data):
        """Browse and compare the available entries against given lists."""
        weak_elements_found = []
        for entry in elements:
            element_found = data.decode("utf-8", errors="ignore").rfind(entry)
            if element_found >= 0:
                if entry in weak_elements:
                    weak_elements_found.append(entry)
        return weak_elements_found
