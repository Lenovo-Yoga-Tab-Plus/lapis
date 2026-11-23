#!/usr/bin/env python3
"""Build the ZUI sn.img for one Lenovo Yoga Tab Plus.

The image is the offline unlock record used by fastboot on TB520FU.
Pass the serial from `fastboot getvar serialno`. The script writes
sn_<serial>.img in the current directory.

Unlocking erases Android data. The file is signed for the serial you
type and is not a universal key.
"""

import argparse
import base64
import sys
from pathlib import Path

HEADERS = base64.b64decode(
    "QU5EUk9JRCEKAAAAAIAAEAAAAAAAAAARAAAAAAAA8BAAAQAQAAgAAA=="
)
CONTENT = base64.b64decode("6r3GZB6a41IwAADzLHLILPET1TE=")
SIGNATURE = base64.b64decode(
    "MIIFBgIBATCCA+EwggLJoAMCAQICCQCiAISzMuYMgDANBgkqhkiG9w0BAQsFADCBhjELMAkGA1UEBhMCQ04xCzAJBgNVBAgMAkJKMRUwEwYDVQQHDAxCZWlqaW5nIFZpZXcxDzANBgNVBAoMBkxFTk9WTzEPMA0GA1UECwwGTW9iaWxlMQ8wDQYDVQQDDAZMRU5PVk8xIDAeBgkqhkiG9w0BCQEWEWxlbm92b0BsZW5vdm8uY29tMB4XDTE4MDEwNTA3MjEzM1oXDTQ1MDUyMzA3MjEzM1owgYYxCzAJBgNVBAYTAkNOMQswCQYDVQQIDAJCSjEVMBMGA1UEBwwMQmVpamluZyBWaWV3MQ8wDQYDVQQKDAZMRU5PVk8xDzANBgNVBAsMBk1vYmlsZTEPMA0GA1UEAwwGTEVOT1ZPMSAwHgYJKoZIhvcNAQkBFhFsZW5vdm9AbGVub3ZvLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOFGyTPBefCQCBb5hrU3r8O9XofI6XoP7Rj5rJeD9eVikRjShvSAVIaKZWsxZXEfRgNndL70pM9L24qdpbWvOKfN4lUSbkpHdOw7ldaRjznB5I32zgRnzMrgKsM6MR9ePC+tx8lrC5BbJnMtr2ocuMY+xO5A2QlhUg2gujhksdFvX8mUf0yUS2SScEfO32tN8YU27oJUi9RQ6/eVCVMJ3HvEo9T/CV51Nqzdo7Ehd9bWndbE6A+TSicN4/QxNi7DjwC2qjPgp6m4+peNTqxwBMqkb8Q5ll2TgeglrmYA4M+kRlWsPhchR/BFTnUEOf/naM+xs90TzjN/RGs92YvuutkCAwEAAaNQME4wHQYDVR0OBBYEFHjfVJF3GxRNUk/7NLyabPMhwVrfMB8GA1UdIwQYMBaAFHjfVJF3GxRNUk/7NLyabPMhwVrfMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBANpz4bY3CQ3w9tIFl+/1VenrgLVD++sRAQxz2wIXRGAjmmOQzvTgJYXHNwywHHwC/QOqXp08ZFbrAhi6dbL0xyIVkvAeE/+Ji78IZrupfYccw6xNuUI1flJVfxDWDofp0YluQ45rme6VZRlRYxvqEvozAvNapfiLleFMEW68orWDxW3ahAK6aop9Y5DarmeZeNHBvN1l2kecdfGjrZIrcA7dFYFS4pfKUjRWp7QIdju55C0fFIhg2gBZU6cWUSjy12pHyor6E6QcrH8W49fBLI/IgvUGqvNk77xqrStw9n2jbyKBLu3Q7l7aOwlxTTrCfZfYioToRiAfry+w7X1fXIUwCwYJKoZIhvcNAQELMAsTBS9ib290AgIQAASCAQCB1hNRsL2Ocko2KTvJd0/IhdPXTqYf1mErWUwIcl2uvkKxi42xcxUUgH/67yIw77l4hmrxAFqdQD9sKtC7VmY8yvl2l0rU4hSwa0rbYT/ij39Ww+cANh19Qohpx16QQbc2OsvAoz+/IBL/ftqt+9C3wZJHM5tr/BN5AMS1ebPf5Xtg8RgAcMU1iBVR5psGWsaaBKDmkGHqtiRBTGeWqJzSp6NV85CB9aH/EJR9CPzVMOApCHc3Ek3Gj+n+X+j64bxSphdob1R0Rnn2q2Dud1A6JlG5t6tX0iP5exHdJMLfLC8mDkKfCkVkZjeVFnX/75i3LdkR0dLuHAHYXzDD+8Uo"
)


def pad(content, padding, length):
    if len(content) >= length or not padding:
        return content
    need = length - len(content)
    repeats = (need + len(padding) - 1) // len(padding)
    return content + (padding * repeats)[:need]


def build_zui_image(serial):
    if not serial.isalnum() or not 1 <= len(serial) <= 16:
        raise ValueError("serial must be 1 to 16 letters or digits")
    encoded = pad(serial.encode("ascii"), b"0", 8)
    encoded = pad(encoded, b"\0", 16)
    return b"".join(
        (
            pad(HEADERS, b"\0", 576),
            pad(CONTENT, b"\0", 1472),
            pad(encoded, b"\0", 2048),
            SIGNATURE,
        )
    )


def main(argv):
    parser = argparse.ArgumentParser(description="Build a TB520FU ZUI unlock image")
    parser.add_argument("serial", help="serial from fastboot getvar serialno")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="output path (default: sn_<serial>.img)",
    )
    args = parser.parse_args(argv)
    serial = args.serial.strip()
    image = build_zui_image(serial)
    if image[2048:2048 + len(serial)] != serial.encode("ascii"):
        raise RuntimeError("serial was not written at offset 2048")
    output = args.output or Path(f"sn_{serial}.img")
    output.write_bytes(image)
    print(f"wrote {output} ({len(image)} bytes)")
    print("fastboot flash unlock", output)
    print("fastboot flashing unlock")
    print("If flashing unlock is rejected: fastboot oem unlock-go")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except ValueError as error:
        print(f"unlock-bootloader: {error}", file=sys.stderr)
        sys.exit(1)
