import socket
import threading
import queue


# Defines ports
SERVICE_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
}


def scan_ports(target_ip, port_queue, open_ports):
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((target_ip, port)) == 0:
                # Get service name from dictionary
                service = SERVICE_PORTS.get(port, "Unknown")
                print(f"Port {port} is open ({service})")
                open_ports.append(port)
            s.close()

        except socket.gaierror:
            print("Host is unreachable")
            break

        except Exception as e:
            print(f"Error scanning port {port}: {e}")


def main():
    NUMBER_OF_THREADS = 10

    try:
        target_host = input("Enter Target Host: ")
        ports = input("Enter Target Ports (e.g., 1-1000): ")

        start_port, end_port = map(int, ports.split("-"))
        range_for_ports = range(start_port, end_port + 1)

        # Resolve hostname to IP
        try:
            target_ip = socket.gethostbyname(target_host)
            print(f"Scanning {target_host} ({target_ip})...\n")
        except socket.gaierror:
            print(f"Could not resolve hostname: {target_host}")
            return

        port_queue = queue.Queue()
        for port in range_for_ports:
            port_queue.put(port)

        open_ports = []
        thread_list = []

        # Create and start threads
        for _ in range(NUMBER_OF_THREADS):
            thread = threading.Thread(target=scan_ports, args=(target_ip, port_queue, open_ports))
            thread_list.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in thread_list:
            thread.join()

        # Print summary
        if open_ports:
            print("\n" + "="*50)
            print("SCAN SUMMARY")
            print("="*50)
            for port in sorted(open_ports):
                service = SERVICE_PORTS.get(port, "Unknown")
                print(f"Port {port:5d} — {service}")
        else:
            print("\nNo open ports found")

    except KeyboardInterrupt:
        print("\nPort scanning interrupted")
    except ValueError:
        print("Invalid input format. Use format like: 1-1000")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()