"""Support for checking TCP ports."""
from remediar.helper import Check
import socket


class CheckTcpIsPortOpen(Check):
    """Representation of a check for open TCP ports."""

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
        """Return the state of the entity."""
        return self._output

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return "Port {} open".format(self._port) if self._output is True else "Port {} closed".format(self._port)

    def run_check(self):
        """."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self._server, int(self._port)))
            self._output = True
        except socket.error:
            self._output = False
        except OverflowError:
            self._output = False

        #import random
        from scapy.all import ICMP, IP, sr1, TCP

        # Define end host and TCP port range
        #host = "192.168.122.164"
        #ports = [22, 23, 80, 443, 3389]

        # # Send SYN with random Src Port for each Dst port
        # for dst_port in port_range:
        #     src_port = random.randint(1025, 65534)
        #     resp = sr1(
        #         IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="S"),
        #         timeout=1,
        #         verbose=0,
        #     )
        #
        #     if resp is None:
        #         print(f"{host}:{dst_port} is filtered (silently dropped).")
        #
        #     elif resp.haslayer(TCP):
        #         if resp.getlayer(TCP).flags == 0x12:
        #             # Send a gratuitous RST to close the connection
        #             send_rst = sr(
        #                 IP(dst=host) / TCP(sport=src_port, dport=dst_port,
        #                                    flags='R'),
        #                 timeout=1,
        #                 verbose=0,
        #             )
        #             print(f"{host}:{dst_port} is open.")
        #
        #         elif resp.getlayer(TCP).flags == 0x14:
        #             print(f"{host}:{dst_port} is closed.")
        #
        #     elif resp.haslayer(ICMP):
        #         if (
        #                 int(resp.getlayer(ICMP).type) == 3 and
        #                 int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]
        #         ):
        #             print(f"{host}:{dst_port} is filtered (silently dropped).")

        # import masscan
        #
        # ports = '22,80'
        #
        # mas = masscan.PortScanner()
        # mas.scan(host, ports=ports)
        # return mas.scan_result
