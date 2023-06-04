import socket
import subprocess
import sys
import os


def get_host_ip():
    """Get the IP address of the local machine."""
    try:
        # Create a temporary socket to get the IP address
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(('8.8.8.8', 80))
        host_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return host_ip
    except socket.error:
        return "Unable to get IP address"


def scan_port(host, port):
    """Scan a specific port on a given host."""
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to connect to the host and port
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        s.close()
    except socket.error:
        print("Unable to connect to the host")


def ping(host):
    """Ping a given host to check its availability."""
    try:
        # Execute the ping command
        response = subprocess.call(['ping', '-c', '1', host])
        if response == 0:
            print(f"Host {host} is reachable")
        else:
            print(f"Host {host} is unreachable")
    except OSError:
        print("Ping command failed")


def traceroute(host):
    """Perform a traceroute to a given host."""
    try:
        # Execute the traceroute command
        response = subprocess.check_output(['traceroute', host])
        print(f"Traceroute to {host}:\n{response.decode()}")
    except subprocess.CalledProcessError:
        print("Traceroute command failed")


def main():
    # Get the IP address of the local machine
    host_ip = get_host_ip()
    print(f"Local IP Address: {host_ip}")

    # Perform reconnaissance tasks
    while True:
        print("\n--- Reconnaissance Menu ---")
        print("1. Scan a port")
        print("2. Ping a host")
        print("3. Traceroute to a host")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            host = input("Enter the host to scan: ")
            port = int(input("Enter the port to scan: "))
            scan_port(host, port)
        elif choice == "2":
            host = input("Enter the host to ping: ")
            ping(host)
        elif choice == "3":
            host = input("Enter the host to traceroute: ")
            traceroute(host)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
