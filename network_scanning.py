import socket
import threading
import nmap

def scan_port(target_ip, port, open_ports):
    """
    Thread function to scan a single port and append it to the open_ports list if it's open.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set timeout to 1 second
        result = s.connect_ex((target_ip, port))
        if result == 0:  # Port is open
            open_ports.append(port)

def scan_open_ports(target_ip, port_range=(1, 1024)):
    """
    Perform a parallel port scan on the target IP address using threading.

    Parameters:
        target_ip (str): The IP address to scan.
        port_range (tuple): A tuple specifying the range of ports to scan (default is 1–1024).

    Returns:
        list: A list of open ports detected during the scan.
    """
    open_ports = []
    threads = []  # List to hold thread objects

    print(f"Scanning ports {port_range[0]}–{port_range[1]} on {target_ip} in parallel...")
    
    # Create a thread for each port in the range
    for port in range(port_range[0], port_range[1] + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port, open_ports))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print(f"Open ports for {target_ip}: {sorted(open_ports)}")
    return open_ports

def perform_nmap_scan(target_ip):
    """
    Perform an advanced scan on the target IP address using the Nmap library.

    Parameters:
        target_ip (str): The IP address to scan.

    Returns:
        None: Prints the results of the scan directly.
    """
    nm = nmap.PortScanner()
    print(f"Performing Nmap scan on {target_ip}...")

    try:
        # Run an Nmap scan with service version detection (-sV)
        nm.scan(hosts=target_ip, arguments="-sV -p 1-1024 -T4")  # -T4 aggressive timing
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            for proto in nm[host].all_protocols():  # Iterate through protocols
                ports = nm[host][proto].keys()
                for port in sorted(ports):  # List ports detected by Nmap
                    service_info = nm[host][proto][port]  # Get service details
                    print(f"Port {port}: {service_info}")
    except Exception as e:
        print(f"Error performing Nmap scan: {e}")