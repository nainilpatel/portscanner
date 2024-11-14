import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)  # Set a timeout to prevent hanging on closed ports
    result = scanner.connect_ex((ip, port))  # Connect to the port
    if result == 0:  # 0 indicates the port is open
        print(f"Port {port} is open.")
    scanner.close()

# Function to start scanning a range of ports
def port_scanner(ip, start_port, end_port):
    print(f"Scanning IP: {ip} from port {start_port} to {end_port}")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    print("Scanning complete.")

# Main function to get user input and start the port scanner
def main():
    target_ip = input("Enter the IP address or domain to scan: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    # Convert domain name to IP if a domain is provided
    try:
        ip_address = socket.gethostbyname(target_ip)
        print(f"Resolved IP address: {ip_address}")
        port_scanner(ip_address, start_port, end_port)
    except socket.gaierror:
        print("Invalid domain or IP address. Please check and try again.")

if __name__ == "__main__":
    main()
