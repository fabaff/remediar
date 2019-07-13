"""Constants for remediar."""
from cement.utils.version import get_version_banner
from .core.version import get_version

VERSION_BANNER = """
Remediar %s
""" % (
    get_version(),
)

RUN_BANNER = """
    +---+
 -->|   |---> x     Remediar %s
    |   |---> o     
    +---+

Track your issues and vulnerabilities!
""" % (
    get_version(),
)

VERSION_BANNER = """
Details:
%s
""" % (
    get_version_banner(),
)

HEADERS = ["target", "group", "check", "result", "output"]

# Source: https://csrc.nist.gov/csrc/media/publications/fips/140/2/final/documents/fips1402annexa.pdf

SSH_CIPHERS = [
    "3des-cbc",
    "aes128-cbc",
    "aes192-cbc",
    "aes256-cbc",
    "aes128-ctr",
    "aes192-ctr",
    "aes256-ctr",
    "aes128-gcm@openssh.com",
    "aes256-gcm@openssh.com",
    "arcfour",
    "arcfour128",
    "arcfour256",
    "blowfish-cbc",
    "cast128-cbc",
    "chacha20-poly1305@openssh.com",
]

SSH_WEAK_CIPHERS = [
    "3des-cbc",
    "aes128-cbc",
    "aes192-cbc",
    "aes256-cbc",
    "blowfish-cbc",
    "cast128-cbc",
    "rijndael-cbc@lysator.liu.se",
]

SSH_MACS = [
    "hmac-md5",
    "hmac-md5-96",
    "hmac-ripemd160",
    "hmac-sha1",
    "hmac-sha1-96",
    "hmac-sha2-256",
    "hmac-sha2-512",
    "umac-64",
    "umac-128",
    "hmac-md5-etm@openssh.com",
    "hmac-md5-96-etm@openssh.com",
    "hmac-ripemd160-etm@openssh.com",
    "hmac-sha1-etm@openssh.com",
    "hmac-sha1-96-etm@openssh.com",
    "hmac-sha2-256-etm@openssh.com",
    "hmac-sha2-512-etm@openssh.com",
    "umac-64-etm@openssh.com",
    "umac-128-etm@openssh.com",
    "arcfour",
    "arcfour128",
    "arcfour256",
]

SSH_WEAK_MACS = [
    "hmac-md5",
    "hmac-md5-96",
    "hmac-sha1-96",
    "arcfour",
    "arcfour128",
    "arcfour256",
]

SSH_KEXS = [
    "curve25519-sha256@libssh.org",
    "diffie-hellman-group1-sha1",
    "diffie-hellman-group14-sha1",
    "diffie-hellman-group-exchange-sha1",
    "diffie-hellman-group-exchange-sha256",
    "ecdh-sha2-nistp256",
    "ecdh-sha2-nistp384",
    "ecdh-sha2-nistp521",
    "ecdsa-sha2-nistp256-cert-v01@openssh.com",
    "ecdsa-sha2-nistp384-cert-v01@openssh.com",
    "ecdsa-sha2-nistp521-cert-v01@openssh.com",
]

SSH_WEAK_KEXS = [
    "diffie-hellman-group1-sha1",
    "diffie-hellman-group-exchange-sha1",
    "diffie-hellman-group14-sha1",
]
