#!/usr/bin/env python3
"""
===========================================
  Port Scanner - by Ibrahim Babarinde
===========================================
  Educational tool for scanning open ports
  on a target host.

  DISCLAIMER: Only use on systems you own
  or have explicit written permission to test.
===========================================
"""

import socket
import sys
from datetime import datetime


# ─────────────────────────────────────────
#  BANNER
# ─────────────────────────────────────────

def print_banner():
    print("=" * 50)
    print("        IBRAHIM'S PORT SCANNER")
    print("     Educational Purposes Only")
    print("=" * 50)


# ─────────────────────────────────────────
#  RESOLVE TARGET
# ─────────────────────────────────────────

def resolve_target(target):
    """
    Converts a hostname to an IP address.
    If the user types a domain like google.com,
    this turns it into an IP like 142.250.74.46
    """
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"\n[ERROR] Could not resolve host: {target}")
        print("Check the target name and try again.")
        sys.exit()


# ─────────────────────────────────────────
#  SCAN A SINGLE PORT
# ─────────────────────────────────────────

def scan_port(ip, port):
    """
    Tries to connect to a specific port on the target IP.
    If the connection succeeds, the port is OPEN.
    If it fails, the port is CLOSED or filtered.
    """
    try:
        # Create a fresh socket for each port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout so we don't wait forever on closed ports
        sock.settimeout(1)

        # Try to connect — returns 0 if successful
        result = sock.connect_ex((ip, port))

        sock.close()

        if result == 0:
            return True   # Port is OPEN
        else:
            return False  # Port is CLOSED

    except socket.error:
        return False


# ─────────────────────────────────────────
#  GET SERVICE NAME
# ─────────────────────────────────────────

def get_service(port):
    """
    Tries to identify the service running on a port.
    For example, port 80 = HTTP, port 22 = SSH
    """
    try:
        service = socket.getservbyport(port)
        return service
    except:
        return "Unknown"


# ─────────────────────────────────────────
#  MAIN SCANNER
# ─────────────────────────────────────────

def run_scanner(target, start_port, end_port):
    """
    Loops through the port range and scans each one.
    Prints results as it goes.
    """
    ip = resolve_target(target)

    print(f"\n[*] Target   : {target}")
    print(f"[*] IP       : {ip}")
    print(f"[*] Ports    : {start_port} - {end_port}")
    print(f"[*] Started  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        # Show progress every 100 ports so user knows it's running
        if port % 100 == 0:
            print(f"[*] Scanning port {port}...", end="\r")

        if scan_port(ip, port):
            service = get_service(port)
            print(f"[OPEN]  Port {port:<6} —  {service}")
            open_ports.append(port)

    # Summary
    print("-" * 50)
    print(f"\n[✓] Scan complete.")
    print(f"[✓] Open ports found: {len(open_ports)}")

    if open_ports:
        print(f"[✓] Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("[✓] No open ports found in this range.")

    print(f"\n[*] Finished : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


# ─────────────────────────────────────────
#  INPUT & ENTRY POINT
# ─────────────────────────────────────────

def main():
    print_banner()

    # Get target from user
    target = input("\nEnter target (IP or hostname): ").strip()

    if not target:
        print("[ERROR] No target entered.")
        sys.exit()

    # Get port range
    try:
        start_port = int(input("Start port (default 1): ").strip() or 1)
        end_port   = int(input("End port (default 1024): ").strip() or 1024)
    except ValueError:
        print("[ERROR] Ports must be numbers.")
        sys.exit()

    # Validate port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[ERROR] Invalid port range. Use 1–65535.")
        sys.exit()

    # Run the scan
    run_scanner(target, start_port, end_port)


if __name__ == "__main__":
    main()
